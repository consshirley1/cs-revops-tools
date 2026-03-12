import streamlit as st
import google.generativeai as genai
from shared import COMMON_CSS, DARK, TEAL_DARK, TEAL_MID, TEAL_LIGHT, mermaid_chart

st.set_page_config(page_title="Company Summarizer", page_icon="🤖", layout="wide")
st.markdown(COMMON_CSS, unsafe_allow_html=True)

st.markdown(f"""
<style>
    .key-help {{
        background: {TEAL_LIGHT}; border: 1px solid {TEAL_MID}55; border-radius: 6px;
        padding: 0.85rem 1rem; font-size: 0.82rem; color: {DARK};
        margin-top: 0.5rem;
    }}
    .key-help a {{ color: {TEAL_DARK}; text-decoration: none; }}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="page-title">Company <span>Summarizer</span></div>', unsafe_allow_html=True)
st.markdown(f"<p style='color:{DARK};'>Enter a company name or domain and get an AI-generated RevOps-focused one-pager.</p>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

GEMINI_MODEL = "gemini-1.5-flash"

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
    st.markdown('<div class="section-label">API Key</div>', unsafe_allow_html=True)
    key_input = st.text_input(
        "Google Gemini API Key",
        type="password",
        placeholder="AIza...",
        label_visibility="visible",
    )
    st.markdown(f"""
    <div class="key-help">
        Get a free API key at
        <a href="https://aistudio.google.com/app/apikey" target="_blank">aistudio.google.com</a>.
        Free tier: 15 requests/min, 1M tokens/day. Your key is used only for this session and never stored.
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

col_left, col_right = st.columns([2, 1])

with col_left:
    company_input = st.text_input(
        "Company name or domain",
        placeholder="e.g. Notion, linear.app, figma.com",
    )

with col_right:
    focus = st.selectbox(
        "Output focus",
        ["GTM & Sales Intel", "General Overview", "Competitive Landscape"],
    )

examples = ["Notion", "Linear", "Figma", "Rippling", "Lattice"]
ex_cols = st.columns(len(examples))
for i, ex in enumerate(examples):
    with ex_cols[i]:
        if st.button(ex, key=f"ex_{ex}", use_container_width=True):
            company_input = ex

run = st.button("Generate Summary →", type="primary", disabled=not api_key)

SYSTEM_PROMPT = """You are a RevOps research assistant. When given a company name or domain,
produce a concise, structured one-pager optimized for GTM and sales intelligence.

Respond ONLY with a structured markdown document using these exact sections:
## Company Overview
## Industry & Category
## Company Size & Stage
## Key Products / Value Prop
## Typical Buyer & ICP
## GTM & Sales Notes
## Tech Stack Signals (if known)
## RevOps Relevance

Keep each section to 2-4 sentences. Be specific and factual.
If uncertain about something, say so rather than guessing.
Do not include any preamble or conclusion outside of these sections."""

FOCUS_ADDENDUM = {
    "GTM & Sales Intel": "Prioritize GTM motion, sales signals, buyer personas, and competitive positioning.",
    "General Overview": "Give a balanced overview across all sections.",
    "Competitive Landscape": "Emphasize competitive positioning, market alternatives, and differentiation.",
}

if run and company_input:
    with st.spinner(f"Researching {company_input}…"):
        try:
            genai.configure(api_key=api_key)
            model = genai.GenerativeModel(
                model_name=GEMINI_MODEL,
                system_instruction=SYSTEM_PROMPT,
            )

            user_msg = f"Company: {company_input}\nFocus: {FOCUS_ADDENDUM[focus]}"
            response = model.generate_content(user_msg)
            result = response.text

            st.markdown("<hr>", unsafe_allow_html=True)
            st.markdown(f"### {company_input} — RevOps One-Pager")
            st.markdown(f"*Focus: {focus} · Model: {GEMINI_MODEL}*")
            st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
            st.markdown(result)

            st.markdown("<hr>", unsafe_allow_html=True)
            st.download_button(
                "Download as Markdown",
                data=f"# {company_input} — RevOps One-Pager\n*Focus: {focus}*\n\n{result}",
                file_name=f"{company_input.lower().replace(' ', '_')}_summary.md",
                mime="text/markdown",
            )

        except Exception as e:
            err = str(e)
            if "API_KEY_INVALID" in err or "API key not valid" in err:
                st.error("❌ Invalid API key. Double-check your key at aistudio.google.com.")
                st.session_state.gemini_api_key = None
            elif "RESOURCE_EXHAUSTED" in err or "quota" in err.lower():
                st.error("⏱️ Rate limit reached. Wait a moment and try again.")
            else:
                st.error(f"Something went wrong: {err}")

elif run and not company_input:
    st.warning("Please enter a company name or domain.")

# ── How it works ─────────────────────────────────────────────────────────────
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<div class="section-label">How It Works</div>', unsafe_allow_html=True)

mermaid_chart("""
flowchart LR
    A([Company Name\\nor Domain]) --> B[Focus Selector\\nGTM / General / Competitive]
    B --> C[System Prompt\\n8-section template]
    C --> D[Gemini 1.5 Flash\\ngoogle-generativeai]
    D --> E[Structured Markdown\\nOne-Pager]
    E --> F[ICP Profile]
    E --> G[Tech Stack Signals]
    E --> H[RevOps Relevance]
    E --> I([⬇️ Download .md])
""", height=240)

st.markdown("<hr>", unsafe_allow_html=True)
st.caption(f"Powered by Google Gemini ({GEMINI_MODEL}). Free tier: 15 req/min, 1M tokens/day. Results reflect model training data.")
