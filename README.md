# ⚡ Wallace 2049 — Living Wiki

Wallace 2049 turns a folder of textbook PDFs into a searchable, chattable "living wiki." It converts each PDF into Markdown, then lets you ask questions about it through a Gemini-powered agent that can search across every ingested book and append its own notes/insights back into the file you're currently viewing — via a Streamlit dashboard.

## How it works

```
raw_data/*.pdf  ──ingest──▶  processed_data/<book>/<book>.md  ──▶  Streamlit UI ──▶  Gemini agent
```

| File | Role |
|---|---|
| `ingest.py` | Converts PDFs to Markdown via Gemini vision, preserving equations as LaTeX. Slower, but handles scanned/complex layouts and math-heavy books well. Resumable if it crashes mid-book. |
| `ingest_fast.py` | Converts PDFs to Markdown locally using PyMuPDF (no API calls). Much faster, but plain text only — no equation formatting. |
| `wiki_tools.py` | Tools the agent can call: search across all books, read the currently-selected book, and append notes to it. |
| `agent.py` | Wraps the Gemini API with tool-calling and a retry/fallback cascade across models. |
| `app.py` | The Streamlit UI — chat on the left, live markdown viewer on the right. |
| `cleanup.py` | Deletes any files left over on Google's servers from interrupted `ingest.py` runs. |

## Setup

**1. Clone and install dependencies**

```bash
git clone https://github.com/nandy2uy/wallace-2049-workspace.git
cd wallace-2049-workspace
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Ingestion additionally needs `pypdf` (for `ingest.py`) and `pymupdf` (for `ingest_fast.py`):

```bash
pip install pypdf pymupdf
```

**2. Set your Gemini API key**

Copy `.env.example` to `.env` and fill in your key, then export it before running anything:

```bash
cp .env.example .env
# edit .env and add your key
export GEMINI_API_KEY=your_key_here     # Windows: set GEMINI_API_KEY=your_key_here
```

Get a key from [Google AI Studio](https://aistudio.google.com/apikey).

**3. Add your source PDFs**

```bash
mkdir raw_data
# drop your textbook PDFs into raw_data/
```

**4. Run ingestion**

Pick one depending on whether you need equation formatting:

```bash
python ingest_fast.py   # fast, plain text — good first pass
python ingest.py        # slower, LaTeX-formatted equations via Gemini vision
```

Each PDF produces a folder under `processed_data/` containing a single `.md` file.

**5. Launch the app**

```bash
streamlit run app.py
```

Select a book in the sidebar, then ask questions in the chat. When you share an insight or connection the agent finds worth keeping, it will append it to the currently-selected book's markdown file.

## Notes

- `cleanup.py` is a standalone utility — run `python cleanup.py` if `ingest.py` was interrupted and you want to clear any files left uploaded on Google's servers.
- The agent only ever reads/writes within `processed_data/`.
- No tests or CI yet — contributions welcome.

## License

MIT — see [LICENSE](LICENSE).