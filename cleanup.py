import os
from google import genai

# Hardcode it right here just to force this script through
API_KEY = os.environ.get("GEMINI_API_KEY")

def nuke_ghost_files():
    if API_KEY == "YOUR_API_KEY_HERE":
        print("Bruh, you forgot to paste your API key in the script.")
        return
        
    client = genai.Client(api_key=API_KEY)
    
    print("Scanning Google's servers for abandoned files...")
    try:
        files = list(client.files.list())
        
        if not files:
            print("Server is already clean. No ghost files found.")
            return
            
        for file in files:
            print(f"Executing deletion on: {file.name}")
            client.files.delete(name=file.name)
            
        print("\nAll ghost files wiped. Server storage is at 0%.")
    except Exception as e:
        print(f"Failed to clear server: {str(e)}")

if __name__ == "__main__":
    nuke_ghost_files()