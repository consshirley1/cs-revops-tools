import streamlit as st
import google.generativeai as genai
from shared import COMMON_CSS, DARK, TEAL_DARK, TEAL_MID, TEAL_LIGHT, mermaid_chart
from sidebar import render_sidebar

st.set_page_config(page_title="Lead Researcher — AI Brief Generator", page_icon="🔬", layout="wide")
render_sidebar()
st.markdown(COMMON_CSS, unsafe_allow_html=True)

st.markdown(f"""
<style>
    .key-help {{
        background: {TEAL_LIGHT}; border: 1px solid {TEAL_MID}55; border-radius: 6px;
        padding: 0.85rem 1rem; font-size: 0.82rem; color: {DARK}; margin-top: 0.5rem;
    }}
    .key-help a {{ color: {TEAL_DARK}; text-decoration: none; }}
    .brief-section {{
        border: 1px solid {TEAL_LIGHT}; border-radius: 8px;
        padding: 1.1rem 1.25rem; background: #ffffff; margin-bottom: 0.75rem;
    }}
    .brief-label {{
        font-size: 0.62rem; font-weight: 600; letter-spacing: 0.15em;
        text-transform: uppercase; color: {TEAL_MID}; margin-bottom: 0.5rem;
    }}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="page-title">Lead <span>Researcher</span></div>', unsafe_allow_html=True)
st.markdown(f"<p style='color:{DARK};'>Paste a LinkedIn bio or company 'About Us' text to get a RevOps-ready executive brief.</p>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# ── API Key ───────────────────────────────────────────────────────────────────
GEMINI_MODEL = "gemini-2.5-flash"

if "gemini_api_key" not in st.session_state:
    st.session_state.gemini_api_key = None

api_key = None
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    pass

if not api_key:
    api_key = st.session_state.gemini_api_key

if not api_key:
    st.markdown('<div class="section-label">API Key Required</div>', unsafe_allow_html=True)
    key_input = st.text_input(
        "Google Gemini API Key",
        type="password",
        placeholder="AIza...",
    )
    st.markdown(f"""
    <div class="key-help">
        Free key at <a href="https://aistudio.google.com/app/apikey" target="_blank">aistudio.google.com</a>.
        Your key is used only for this session and never stored.
    </div>
    """, unsafe_allow_html=True)
    if key_input:
        st.session_state.gemini_api_key = key_input
        api_key = key_input
        st.rerun()
else:
    col_key, col_clear = st.columns([6, 1])
    with col_key:
        st.success(f"✅ Gemini API key loaded · Model: `{GEMINI_MODEL}`")
    with col_clear:
        if st.button("Clear key", use_container_width=True):
            st.session_state.gemini_api_key = None
            st.rerun()

st.markdown("<hr>", unsafe_allow_html=True)

# ── Input ──────────────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Prospect Information</div>', unsafe_allow_html=True)

raw_text = st.text_area(
    "Paste LinkedIn bio, About Us page, or any prospect context",
    height=180,
    placeholder="e.g. VP of Sales at Acme Corp. Previously led SDR teams at Outreach and SalesLoft. "
                "Focused on enterprise pipeline generation and sales tech stack optimization...",
)

col_l, col_r = st.columns([2, 1])
with col_r:
    context_type = st.selectbox(
        "Context type",
        ["Individual (LinkedIn bio)", "Company (About Us)", "Mixed"],
    )

run = st.button("Generate Brief →", type="primary", disabled=not api_key)

# ── Logic ─────────────────────────────────────────────────────────────────────
PROMPT_TEMPLATE = """You are a RevOps Strategist preparing a brief for an outbound sales rep.
Analyze the following text and return exactly three sections, each clearly labeled:

**3-Sentence Summary**
Summarize who this person/company is, what they do, and their likely organizational role or scale.

**Potential Pain Points**
List 3–5 specific pain points their revenue team likely experiences. Be concrete, not generic.

**Suggested Outreach Hook**
Write one personalized, non-generic opening line for an outbound email based on their background.
Reference something specific from the text.

Context type: {context_type}
Text: {text}"""

if run and raw_text:
    with st.spinner("Analyzing prospect…"):
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel(GEMINI_MODEL)
            prompt = PROMPT_TEMPLATE.format(context_type=context_type, text=raw_text)
            response = model.generate_content(prompt)
            result = response.text

            st.markdown("<hr>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='color:{DARK};'>Executive Brief</h3>", unsafe_allow_html=True)
            st.markdown(result)

        except Exception as e:
            err = str(e)
            if "API_KEY_INVALID" in err or "API key not valid" in err:
                st.error("❌ Invalid API key.")
                st.session_state.gemini_api_key = None
            elif "RESOURCE_EXHAUSTED" in err or "quota" in err.lower():
                st.error("⏱️ Rate limit reached. Wait a moment and try again.")
            else:
                st.error(f"Something went wrong: {err}")

elif run and not raw_text:
    st.error("Please paste some prospect text to analyze.")

# ── How it works ─────────────────────────────────────────────────────────────
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<div class="section-label">How It Works</div>', unsafe_allow_html=True)

mermaid_chart("""
flowchart LR
    A([Paste Prospect Text\\nLinkedIn / About Us]) --> B[Context Classifier\\nIndividual / Company / Mixed]
    B --> C[RevOps Prompt\\nStructured template]
    C --> D[Gemini 2.0 Flash\\ngoogle-generativeai]
    D --> E[3-Sentence Summary]
    D --> F[Pain Points\\nRevenue team specific]
    D --> G[Outreach Hook\\nPersonalized opener]
    E & F & G --> H([Executive Brief])
""", height=240)

st.markdown("<hr>", unsafe_allow_html=True)
st.caption(f"Powered by Google Gemini ({GEMINI_MODEL}). Results reflect model training data and may require verification.")
