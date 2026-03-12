"""Shared CSS, colors, and utilities used across all portfolio pages."""
import streamlit.components.v1 as components

# ── Palette ──────────────────────────────────────────────────────────────────
DARK       = "#17252A"
TEAL_DARK  = "#2B7A78"
TEAL_MID   = "#3AAFA9"
TEAL_LIGHT = "#DEF2F1"

# ── Global CSS (inject on every page) ────────────────────────────────────────
COMMON_CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:ital,wght@0,300;0,400;0,500;0,600;1,400&display=swap');

html, body, [class*="css"], .stMarkdown, .stText, p, li, span, div {{
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
}}
.stApp {{ background-color: #ffffff; }}
section[data-testid="stSidebar"] {{
    background-color: {TEAL_LIGHT};
    border-right: 1px solid {TEAL_MID}33;
}}

/* ── Typography ── */
.page-title {{ font-size: 2rem; font-weight: 300; color: {DARK}; margin-bottom: 0.25rem; line-height: 1.2; }}
.page-title span {{ color: {TEAL_DARK}; }}
.section-label {{
    font-size: 0.62rem; font-weight: 600; letter-spacing: 0.18em;
    text-transform: uppercase; color: {TEAL_MID}; margin-bottom: 0.7rem;
}}
hr {{ border: none; border-top: 1px solid {TEAL_LIGHT}; margin: 1.75rem 0; }}

/* ── Buttons ── */
div.stButton > button[kind="primary"] {{
    background-color: {TEAL_DARK} !important; color: white !important;
    border: none !important; font-size: 0.83rem !important;
    font-weight: 500 !important; border-radius: 4px !important;
    transition: background 0.15s ease;
}}
div.stButton > button[kind="primary"]:hover {{ background-color: {DARK} !important; }}
div.stButton > button[kind="secondary"] {{
    background-color: {TEAL_MID} !important; color: white !important;
    border: none !important; font-size: 0.83rem !important;
    font-weight: 500 !important; border-radius: 4px !important;
}}
div.stButton > button[kind="secondary"]:hover {{ background-color: {DARK} !important; }}

/* ── Cards ── */
.tool-card {{
    border: 1px solid {TEAL_LIGHT}; border-radius: 8px;
    padding: 1.25rem 1.25rem 0.75rem 1.25rem; background: #ffffff;
}}
.tool-name {{ font-size: 1rem; font-weight: 600; color: {DARK}; margin-bottom: 0.2rem; }}
.tool-badge {{
    display: inline-block; font-size: 0.68rem; font-weight: 500;
    padding: 0.15rem 0.55rem; border-radius: 99px; margin-bottom: 0.65rem;
}}
.badge-live  {{ background: {TEAL_LIGHT}; color: {TEAL_DARK}; }}
.badge-ai    {{ background: {TEAL_LIGHT}; color: {TEAL_MID};  }}
.badge-demo  {{ background: #fef9c3;      color: #713f12;     }}
.badge-sfdc  {{ background: {TEAL_LIGHT}; color: {DARK};      }}
.tool-desc   {{ font-size: 0.83rem; color: {DARK}; line-height: 1.55; margin-bottom: 0.5rem; }}

.info-card {{
    border: 1px solid {TEAL_LIGHT}; border-radius: 8px;
    padding: 1.1rem 1.25rem 0.75rem 1.25rem; background: #ffffff;
}}
.info-title {{ font-size: 0.95rem; font-weight: 600; color: {DARK}; margin-bottom: 0.35rem; }}
.info-desc  {{ font-size: 0.82rem; color: {DARK}; line-height: 1.5; margin-bottom: 0.5rem; }}

/* ── Tag chips ── */
.tag-chip {{
    display: inline-block;
    background: {TEAL_LIGHT}; color: {TEAL_DARK};
    font-size: 0.72rem; padding: 0.2rem 0.65rem; border-radius: 3px;
    margin: 0.2rem 0.2rem 0.2rem 0; font-weight: 500;
}}

/* ── Streamlit overrides ── */
.stTextInput > label, .stSelectbox > label, .stTextArea > label,
.stMultiselect > label {{ color: {DARK} !important; font-weight: 500; }}
.stAlert {{ border-radius: 6px; }}
</style>
"""


def mermaid_chart(diagram: str, height: int = 360):
    """Render a Mermaid diagram using the CDN inside an st.components iframe."""
    components.html(
        f"""
        <script src="https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.min.js"></script>
        <script>
          mermaid.initialize({{
            startOnLoad: true,
            theme: 'base',
            themeVariables: {{
              primaryColor: '{TEAL_LIGHT}',
              primaryTextColor: '{DARK}',
              primaryBorderColor: '{TEAL_MID}',
              lineColor: '{TEAL_DARK}',
              secondaryColor: '{TEAL_LIGHT}',
              tertiaryColor: '#ffffff',
              fontFamily: 'Inter, sans-serif',
              fontSize: '13px',
              edgeLabelBackground: '#ffffff',
              clusterBkg: '{TEAL_LIGHT}'
            }}
          }});
        </script>
        <div class="mermaid" style="background: white; padding: 1rem 0.5rem; border-radius: 6px;">
{diagram}
        </div>
        """,
        height=height,
        scrolling=False,
    )
