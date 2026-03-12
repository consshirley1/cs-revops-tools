import streamlit as st

st.set_page_config(
    page_title="Connor Smith — RevOps Tools",
    page_icon="⚙️",
    layout="wide",
)

# --- Header ---
st.markdown("""
<style>
    .hero-name { font-size: 3rem; font-weight: 300; line-height: 1.1; margin-bottom: 0.5rem; }
    .hero-name span { color: #1d4ed8; }
    .hero-sub { font-size: 1.1rem; color: #6b7280; font-weight: 300; margin-bottom: 2rem; }
    .tool-card {
        border: 1px solid #e5e7eb;
        border-radius: 6px;
        padding: 1.25rem 1.5rem;
        margin-bottom: 0.75rem;
        transition: border-color 0.2s;
    }
    .tool-card:hover { border-color: #1d4ed8; }
    .tool-title { font-size: 1rem; font-weight: 500; margin-bottom: 0.25rem; }
    .tool-desc { font-size: 0.875rem; color: #6b7280; }
    .section-label {
        font-size: 0.65rem;
        font-weight: 500;
        letter-spacing: 0.15em;
        text-transform: uppercase;
        color: #9ca3af;
        margin-bottom: 1rem;
    }
    .stat-num { font-size: 2rem; font-weight: 300; color: #111827; line-height: 1; }
    .stat-label { font-size: 0.75rem; color: #9ca3af; margin-top: 0.2rem; }
    hr { border: none; border-top: 1px solid #e5e7eb; margin: 2rem 0; }
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div class="hero-name">Connor Smith<br><span>Revenue Operations</span></div>
    <div class="hero-sub">GTM Architecture · AI-Powered Tooling · CRM Strategy</div>
    """, unsafe_allow_html=True)
    st.markdown("""
    This is a live collection of tools I've built to solve real RevOps problems —
    from email infrastructure intelligence to AI-powered company research.
    Use the sidebar to navigate, or explore below.
    """)

with col2:
    st.markdown("<div style='height: 1rem'></div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="stat-num">11</div><div class="stat-label">GTM tools launched</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="stat-num">5+</div><div class="stat-label">AI tools shipped</div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="stat-num">2</div><div class="stat-label">Orgs unified</div>', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# --- Tools ---
st.markdown('<div class="section-label">Tools & Demos</div>', unsafe_allow_html=True)

tools = [
    {
        "icon": "📡",
        "title": "MX Lookup — Email Provider Identifier",
        "desc": "Enter any domain to identify its email provider via live DNS/MX record lookup. Detects Google Workspace, Microsoft 365, Mimecast, Proofpoint, and more. Also checks SPF and DMARC configuration.",
        "page": "3_MX_Lookup",
        "tag": "Live · No API key required",
    },
    {
        "icon": "🤖",
        "title": "Company Summarizer",
        "desc": "Enter a company name or domain and get an AI-generated one-pager: overview, industry, size, key products, and GTM relevance. Powered by Claude.",
        "page": "4_Company_Summarizer",
        "tag": "AI-Powered · Claude API",
    },
    {
        "icon": "🇫🇷",
        "title": "INSEE Gap Detector",
        "desc": "A demo of the Salesforce account coverage gap analysis tool I built for the French market. Uses SIREN numbers to surface accounts missing from CRM.",
        "page": "5_INSEE_Gap_Detector",
        "tag": "Demo · Mock Data",
    },
]

for tool in tools:
    with st.container():
        st.markdown(f"""
        <div class="tool-card">
            <div style="display:flex; justify-content:space-between; align-items:flex-start;">
                <div>
                    <div class="tool-title">{tool['icon']} {tool['title']}</div>
                    <div class="tool-desc">{tool['desc']}</div>
                </div>
                <div style="font-size:0.65rem; color:#9ca3af; white-space:nowrap; margin-left:1rem; margin-top:0.2rem;">{tool['tag']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<div class="section-label">About & Background</div>', unsafe_allow_html=True)

col_a, col_b = st.columns(2)
with col_a:
    st.markdown("""
    <div class="tool-card">
        <div class="tool-title">👤 About Me</div>
        <div class="tool-desc">Background, experience, and what I'm looking for in a senior RevOps role.</div>
    </div>
    """, unsafe_allow_html=True)
with col_b:
    st.markdown("""
    <div class="tool-card">
        <div class="tool-title">📄 Resume</div>
        <div class="tool-desc">View or download my full resume.</div>
    </div>
    """, unsafe_allow_html=True)
