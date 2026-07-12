import fitz  # PyMuPDF
from pathlib import Path
import time

RAW_DATA = Path(__file__).resolve().parent / "raw_data"
OUTPUT_DIR = Path(__file__).resolve().parent / "processed_data"

def main():
    pdf_files = sorted(RAW_DATA.glob("*.pdf"))
    if not pdf_files:
        print(f"No PDFs found in {RAW_DATA}")
        return

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    for pdf_path in pdf_files:
        # Strip trailing spaces from the filename (Windows safety check)
        safe_stem = pdf_path.stem.strip()
        
        print(f"\n=== Shredding: {pdf_path.name} ===")
        start_time = time.time()
        
        out_folder = OUTPUT_DIR / safe_stem
        out_folder.mkdir(parents=True, exist_ok=True)
        out_file = out_folder / f"{safe_stem}.md"
        
        # Skip if already processed
        if out_file.exists():
            print(f"⏩ '{safe_stem}.md' already exists. Skipping...")
            continue
            
        # Open the PDF locally
        doc = fitz.open(pdf_path)
        markdown_text = f"# {safe_stem}\n\n"
        
        # Rip through every page instantly
        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text("text")
            markdown_text += f"\n\n## Page {page_num + 1}\n\n{text}"
            
        # Save to disk
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(markdown_text)
            
        elapsed = time.time() - start_time
        print(f"⚡ Done in {elapsed:.2f} seconds. Saved to {out_file}")

if __name__ == "__main__":
    main()