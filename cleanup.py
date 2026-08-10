"""Deletes any files left uploaded on Google's servers from an interrupted
ingest.py run (ingest.py normally cleans up after itself, but a crash or
Ctrl+C mid-upload can leave orphaned files behind)."""

import os
import sys
from dotenv import load_dotenv
from google import genai

load_dotenv()


def delete_uploaded_files():
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        print("ERROR: GEMINI_API_KEY missing. Set it in your .env file or environment.")
        sys.exit(1)

    client = genai.Client(api_key=api_key)

    print("Scanning for files left on the server...")
    try:
        files = list(client.files.list())

        if not files:
            print("Nothing to clean up - no files found.")
            return

        for file in files:
            print(f"Deleting: {file.name}")
            client.files.delete(name=file.name)

        print(f"\nDone. Removed {len(files)} file(s).")
    except Exception as e:
        print(f"Failed to clean up server files: {str(e)}")
        sys.exit(1)


if __name__ == "__main__":
    delete_uploaded_files()
