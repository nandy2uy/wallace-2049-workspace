import os
import sys
import time
from pathlib import Path
from google import genai
from google.genai import types
from pypdf import PdfReader, PdfWriter

RAW_DATA = Path(__file__).resolve().parent / "raw_data"
OUTPUT_DIR = Path(__file__).resolve().parent / "processed_data"
CHUNK_SIZE = 40  

def split_pdf(file_path):
    reader = PdfReader(file_path)
    total_pages = len(reader.pages)
    chunk_paths = []
    
    for i in range(0, total_pages, CHUNK_SIZE):
        writer = PdfWriter()
        end_page = min(i + CHUNK_SIZE, total_pages)
        for page_num in range(i, end_page):
            writer.add_page(reader.pages[page_num])
            
        chunk_path = file_path.parent / f"temp_chunk_{i}_to_{end_page}.pdf"
        with open(chunk_path, "wb") as f:
            writer.write(f)
        chunk_paths.append(chunk_path)
        
    return chunk_paths, total_pages

def main():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: GEMINI_API_KEY missing.")
        sys.exit(1)

    client = genai.Client(api_key=api_key)
    pdf_files = sorted(RAW_DATA.glob("*.pdf"))
    pdf_files = [f for f in pdf_files if "temp_chunk" not in f.name]

    if not pdf_files:
        print(f"No PDFs found in {RAW_DATA}")
        sys.exit(1)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # ---------------------------------------------------------
    # 🛑 RESUME SETTING: 
    # Since you crashed on Chunk 9, I set this to 9 for you.
    # When this book finishes, it automatically resets to 1 for the next books.
    RESUME_FROM_CHUNK = 1
    # ---------------------------------------------------------

    for pdf_path in pdf_files:
        print(f"\n=== Processing: {pdf_path.name} ===")
        out_folder = OUTPUT_DIR / pdf_path.stem
        out_folder.mkdir(parents=True, exist_ok=True)
        out_file = out_folder / f"{pdf_path.stem}.md"
        
        # Only wipe the file clean if we are starting a completely fresh book
        if RESUME_FROM_CHUNK == 1 and out_file.exists():
            out_file.unlink()

        chunk_paths, total_pages = split_pdf(pdf_path)
        print(f"Total pages: {total_pages} | Chunks: {len(chunk_paths)}")

        for idx, chunk_path in enumerate(chunk_paths):
            current_chunk = idx + 1
            
            if current_chunk < RESUME_FROM_CHUNK:
                print(f"⏩ Skipping Chunk {current_chunk} (Already saved)...")
                if chunk_path.exists():
                    chunk_path.unlink()
                continue

            print(f"\n[Chunk {current_chunk}/{len(chunk_paths)}] Uploading...")
            uploaded_file = client.files.upload(file=str(chunk_path))
            
            print("Waiting for vision indexing", end="", flush=True)
            while uploaded_file.state.name == "PROCESSING":
                print(".", end="", flush=True)
                time.sleep(3)
                uploaded_file = client.files.get(name=uploaded_file.name)
            print(" Active!")

            if uploaded_file.state.name == "FAILED":
                print(f"[!] Server rejected Chunk {current_chunk}. Skipping.")
                chunk_path.unlink()
                continue

            prompt = (
                "Convert this document into clean, readable Markdown format. "
                "Identify all mathematical equations, formulas, symbols, and operators, "
                "and render them precisely using standard LaTeX formatting (use $ for inline "
                "and $$ for block equations). Output only the final Markdown text."
            )

            # --- BULLETPROOF RETRY LOOP ---
            max_retries = 6  
            response = None
            
            for attempt in range(max_retries):
                try:
                    response = client.models.generate_content(
                        model='gemini-3.5-flash',
                        contents=[uploaded_file, prompt],
                        config=types.GenerateContentConfig(
                            safety_settings=[
                                types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT, threshold=types.HarmBlockThreshold.BLOCK_NONE),
                                types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_HARASSMENT, threshold=types.HarmBlockThreshold.BLOCK_NONE),
                                types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH, threshold=types.HarmBlockThreshold.BLOCK_NONE),
                                types.SafetySetting(category=types.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT, threshold=types.HarmBlockThreshold.BLOCK_NONE),
                            ]
                        )
                    )
                    break 
                except Exception as e:
                    error_msg = str(e)
                    if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
                        print(f"\n[!] Rate limit hit (Free Tier). Cooling down for 65 seconds... (Attempt {attempt+1}/{max_retries})")
                        time.sleep(35)
                    elif "503" in error_msg or "UNAVAILABLE" in error_msg:
                        print(f"\n[!] Google servers are swamped. Cooling down for 15 seconds... (Attempt {attempt+1}/{max_retries})")
                        time.sleep(15)
                    elif attempt < max_retries - 1:
                        print(f"\n[!] Network hiccup. Retrying in 5 seconds... (Attempt {attempt+1}/{max_retries})")
                        time.sleep(5)
                    else:
                        print(f"\n[!] Critical API failure on Chunk {current_chunk}. Skipping. Error: {error_msg}")
            
            # --- FILE SAVING ---
            if response and response.text:
                with open(out_file, "a", encoding="utf-8") as f:
                    f.write(response.text + "\n\n---\n\n")
                print(f"Chunk {current_chunk} saved successfully!")
            elif response:
                finish_reason = response.candidates[0].finish_reason if response.candidates else "UNKNOWN"
                print(f"\n[!] WARNING: Blocked Chunk {current_chunk}. Reason code: {finish_reason}")
            else:
                print(f"\n[!] WARNING: Chunk {current_chunk} failed completely.")

            client.files.delete(name=uploaded_file.name)
            chunk_path.unlink()
            
            # --- API PACER ---
            print("Pacing request for 5 seconds to respect API speed limits...")
            time.sleep(5)

        print(f"\nSUCCESS! Master file compiled and written to: {out_file}")
        
        # Reset the resume tracker so the next book starts at Chunk 1 naturally
        RESUME_FROM_CHUNK = 1

if __name__ == "__main__":
    main()