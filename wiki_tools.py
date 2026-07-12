import os
from pathlib import Path

PROCESSED_DIR = Path(__file__).resolve().parent / "processed_data"

def get_all_books():
    """Returns a list of all markdown books in the workspace."""
    md_files = list(PROCESSED_DIR.glob("**/*.md"))
    if not md_files:
        raise FileNotFoundError("No markdown files found in processed_data.")
    return md_files

def read_wiki_context() -> str:
    """Reads the library index and the introduction of available books."""
    try:
        books = get_all_books()
        context = "--- WORKSPACE LIBRARY INDEX ---\n"
        for b in books:
            context += f"- {b.name}\n"
        
        # Give the agent a taste of the first book to anchor its logic
        with open(books[0], "r", encoding="utf-8") as f:
            context += f"\n--- Context from {books[0].name} ---\n" + f.read(15000)
        return context
    except Exception as e:
        return f"Error: {str(e)}"

def search_wiki_content(query: str) -> str:
    """Scans ALL markdown documents in the library for the query."""
    try:
        results = []
        query_lower = query.lower()
        
        for file_path in get_all_books():
            with open(file_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
                
            for idx, line in enumerate(lines):
                if query_lower in line.lower():
                    start = max(0, idx - 3)
                    end = min(len(lines), idx + 4)
                    snippet = "".join(lines[start:end])
                    # Add a tag so the agent knows exactly which book it found the match in
                    results.append(f"📍 Match in `{file_path.name}` (Line {idx}):\n{snippet}")
                    
        if not results:
            return f"No matches found across any textbooks for: '{query}'"
            
        return "\n\n".join(results[:10]) # Return top 10 matches globally
    except Exception as e:
        return f"Error searching text blocks: {str(e)}"

def append_to_wiki(section_title: str, update_content: str) -> str:
    """Appends new insights to the primary active book in the workspace."""
    try:
        file_path = get_all_books()[0]
        formatted_entry = f"\n\n## {section_title} (Agent Dynamic Update)\n{update_content}\n"
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(formatted_entry)
        return f"Successfully updated '{file_path.name}'."
    except Exception as e:
        return f"Failed to execute structural update: {str(e)}"