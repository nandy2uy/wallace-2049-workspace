import streamlit as st
import time
from pathlib import Path
from dotenv import load_dotenv
import agent
import wiki_tools

load_dotenv()

# Page Configuration for a sleek, widescreen OS feel
st.set_page_config(layout="wide", page_title="Wallace OS", page_icon="⚡", initial_sidebar_state="expanded")

# --- THE WALLACE 2049 DESIGN SYSTEM (CSS INJECTION) ---
# We bypass Streamlit's default theme entirely to hit those exact hex tokens and typography rules.
st.markdown("""
<style>
    /* Import Premium Typography */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

    /* 1. The Kashmir Atmosphere (Global Background) */
    .stApp {
        background-image: linear-gradient(rgba(10, 15, 20, 0.85), rgba(10, 15, 20, 0.85)), url('https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=2070&auto=format&fit=crop');
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        font-family: 'Inter', sans-serif !important;
        color: #F8F9FA !important;
    }

    /* 2. Apple Liquid Glass for Sidebar */
    [data-testid="stSidebar"] {
        background: rgba(18, 24, 28, 0.4) !important;
        backdrop-filter: blur(24px) saturate(150%) !important;
        -webkit-backdrop-filter: blur(24px) saturate(150%) !important;
        border-right: 1px solid rgba(255, 255, 255, 0.08) !important;
    }

    /* 3. Glass Containers (Chat & Markdown Viewer) */
    div[data-testid="stVerticalBlock"] > div[style*="border"],
    .stChatFloatingInputContainer,
    .streamlit-expanderHeader {
        background: rgba(20, 28, 35, 0.45) !important;
        backdrop-filter: blur(16px) saturate(150%) !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 12px !important;
        box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3) !important;
    }

    /* 4. Buttons (Smooth, minimal borders) */
    .stButton>button {
        background: rgba(255, 255, 255, 0.05) !important;
        color: #F8F9FA !important;
        border: 1px solid rgba(255, 255, 255, 0.1) !important;
        border-radius: 8px !important;
        transition: all 0.2s ease;
    }
    .stButton>button:hover {
        background: rgba(255, 255, 255, 0.1) !important;
        border-color: rgba(255, 255, 255, 0.2) !important;
    }

    /* Text & Accents (Warm Ivory & Soft Greens) */
    h1, h2, h3 {
        color: #F8F9FA !important;
        font-weight: 600 !important;
        letter-spacing: -0.02em;
    }
    p, .st-emotion-cache-1104q6c {
        color: #D1D5DB !important; /* Soft gray for readability */
    }

    /* Hide Streamlit Branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)


if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# --- SIDEBAR: System Controls & Stats ---
with st.sidebar:
    st.title("⚙️ Workspace")
    st.caption("Agentic Knowledge Interface")
    st.divider()

    try:
        all_books = wiki_tools.get_all_books()
        book_map = {b.name: b for b in all_books}

        st.metric(label="Active Knowledge Bases", value=len(all_books))
        st.divider()
        st.subheader("Target Context")

        selected_book = st.selectbox("Select Active Document:", list(book_map.keys()), label_visibility="collapsed")
        target_path = book_map[selected_book]

    except Exception:
        st.warning("No processed data found. Run the ingestion pipeline.")
        target_path = None

# --- MAIN LAYOUT: Split View (Linear/Stripe spacing) ---
st.title("⚡ Wallace 2049: Living Wiki")
# Generous whitespace and gap sizing
left_col, right_col = st.columns([1.2, 1], gap="large")

# --- LEFT COLUMN: The Agent Interface ---
with left_col:
    st.subheader("Terminal")

    chat_container = st.container(height=550, border=True)
    with chat_container:
        for role, text in st.session_state.chat_history:
            if role == "user":
                st.chat_message("user").write(text)
            else:
                st.chat_message("assistant").write(text)

    if user_input := st.chat_input("Synthesize concepts, update files, or query the wiki..."):
        chat_container.chat_message("user").write(user_input)

        with st.spinner("Processing request..."):
            formatted_history = [(role, text) for role, text in st.session_state.chat_history[-4:]]

            try:
                response_text = agent.get_agent_response(
                    user_input,
                    chat_history=formatted_history,
                    active_book_path=target_path,
                )
                st.session_state.chat_history.append(("user", user_input))
                st.session_state.chat_history.append(("model", response_text))
                st.rerun()
            except Exception as e:
                st.error(f"Execution error: {str(e)}")

# --- RIGHT COLUMN: The File System ---
with right_col:
    st.subheader("Active State")
    if target_path:
        st.info(f"📍 Watching: `{target_path.name}`")
        with open(target_path, "r", encoding="utf-8") as f:
            current_markdown = f.read()

        with st.expander("Expand to view full raw markdown", expanded=True):
            st.markdown(current_markdown[:4000] + "\n\n... [Truncated for UI optimization] ...")
