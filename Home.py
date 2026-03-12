import streamlit as st

st.set_page_config(
    page_title="Connor Shirley — RevOps Tools",
    page_icon="⚙️",
    layout="wide",
)

st.markdown("""
<style>
    .stApp { background-color: #ffffff; }
    section[data-testid="stSidebar"] { background-color: #f8fafc; }

    .hero-name { font-size: 3rem; font-weight: 300; line-height: 1.1; margin-bottom: 0.5rem; color: #111827; }
    .hero-name span { color: #1d4ed8; }
    .hero-sub { font-size: 1.1rem; color: #6b7280; font-weight: 300; margin-bottom: 1rem; }
    .section-label {
        font-size: 0.65rem; font-weight: 500; letter-spacing: 0.15em;
        text-transform: uppercase; color: #9ca3af; margin-bottom: 1rem;
    }
    .stat-num { font-size: 2rem; font-weight: 300; color: #1d4ed8; line-height: 1; }
    .stat-label { font-size: 0.75rem; color: #9ca3af; margin-top: 0.2rem; }
    hr { border: none; border-top: 1px solid #e5e7eb; margin: 2rem 0; }
    .tool-meta { font-size: 0.75rem; color: #9ca3af; margin-top: 0.2rem; }
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div class="hero-name">Connor <span>Shirley</span></div>
    <div class="hero-sub">Revenue Operations · GTM Architecture · AI-Powered Tooling</div>
    """, unsafe_allow_html=True)
    st.markdown("""
    A live collection of tools I've built to solve real RevOps problems —
    from email infrastructure intelligence to AI-powered company research.
    Use the sidebar to navigate, or jump in below.
    """)

with col2:
    st.markdown("<div style='height: 0.5rem'></div>", unsafe_allow_html=True)
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="stat-num">11</div><div class="stat-label">GTM tools launched</div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="stat-num">5+</div><div class="stat-label">AI tools shipped</div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="stat-num">2</div><div class="stat-label">Orgs unified</div>', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<div class="section-label">Tools & Demos</div>', unsafe_allow_html=True)

t1, t2, t3 = st.columns(3)

with t1:
    st.markdown("**📡 MX Lookup**")
    st.markdown('<div class="tool-meta">Live · No API key required</div>', unsafe_allow_html=True)
    st.caption("Identify any company's email provider via live DNS/MX record lookup. Detects Google Workspace, M365, Mimecast, Proofpoint, and more.")
    st.markdown('<a href="/3_MX_Lookup" target="_self" style="display:inline-block;padding:0.4rem 1rem;background:#1d4ed8;color:#fff;border-radius:4px;text-decoration:none;font-size:0.85rem;">Open MX Lookup →</a>', unsafe_allow_html=True)

with t2:
    st.markdown("**🤖 Company Summarizer**")
    st.markdown('<div class="tool-meta">AI-Powered · Gemini API</div>', unsafe_allow_html=True)
    st.caption("Enter a company name or domain and get an AI-generated GTM one-pager: overview, ICP, tech stack signals, and RevOps relevance.")
    st.markdown('<a href="/4_Company_Summarizer" target="_self" style="display:inline-block;padding:0.4rem 1rem;background:#1d4ed8;color:#fff;border-radius:4px;text-decoration:none;font-size:0.85rem;">Open Summarizer →</a>', unsafe_allow_html=True)

with t3:
    st.markdown("**🇫🇷 INSEE Gap Detector**")
    st.markdown('<div class="tool-meta">Demo · Mock Data</div>', unsafe_allow_html=True)
    st.caption("Salesforce account coverage gap analysis for the French market. Uses SIREN numbers to surface accounts missing from CRM.")
    st.markdown('<a href="/5_INSEE_Gap_Detector" target="_self" style="display:inline-block;padding:0.4rem 1rem;background:#1d4ed8;color:#fff;border-radius:4px;text-decoration:none;font-size:0.85rem;">Open Gap Detector →</a>', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<div class="section-label">About & Background</div>', unsafe_allow_html=True)

a1, a2 = st.columns(2)

with a1:
    st.markdown("**👤 About Me**")
    st.caption("Background, experience, and what I'm looking for in a senior RevOps role.")
    st.markdown('<a href="/1_About" target="_self" style="display:inline-block;padding:0.4rem 1rem;background:#1d4ed8;color:#fff;border-radius:4px;text-decoration:none;font-size:0.85rem;">View About →</a>', unsafe_allow_html=True)

with a2:
    st.markdown("**📄 Resume**")
    st.caption("View or download my full resume.")
    st.markdown('<a href="/2_Resume" target="_self" style="display:inline-block;padding:0.4rem 1rem;background:#1d4ed8;color:#fff;border-radius:4px;text-decoration:none;font-size:0.85rem;">View Resume →</a>', unsafe_allow_html=True)