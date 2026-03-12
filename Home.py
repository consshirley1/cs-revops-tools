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

    .hero-name { font-size: 3rem; font-weight: 300; line-height: 1.1; margin-bottom: 0.4rem; color: #111827; }
    .hero-name span { color: #1d4ed8; }
    .hero-sub { font-size: 1rem; color: #6b7280; font-weight: 400; margin-bottom: 0.75rem; }
    .hero-body { font-size: 0.95rem; color: #374151; line-height: 1.7; max-width: 600px; }

    .section-label {
        font-size: 0.62rem; font-weight: 600; letter-spacing: 0.18em;
        text-transform: uppercase; color: #9ca3af; margin-bottom: 1rem;
    }

    .stat-box {
        background: #f8fafc;
        border: 1px solid #e5e7eb;
        border-radius: 6px;
        padding: 1rem 0.75rem;
        text-align: center;
    }
    .stat-num { font-size: 1.8rem; font-weight: 300; color: #1d4ed8; line-height: 1; }
    .stat-label { font-size: 0.72rem; color: #6b7280; margin-top: 0.3rem; line-height: 1.3; }

    .tool-card {
        border: 1px solid #e5e7eb;
        border-radius: 6px;
        padding: 1.25rem;
        height: 100%;
        background: #ffffff;
        transition: border-color 0.15s;
    }
    .tool-card:hover { border-color: #93c5fd; }
    .tool-name { font-size: 1rem; font-weight: 600; color: #111827; margin-bottom: 0.2rem; }
    .tool-badge {
        display: inline-block;
        font-size: 0.68rem; font-weight: 500;
        padding: 0.15rem 0.55rem;
        border-radius: 99px;
        margin-bottom: 0.65rem;
    }
    .badge-live { background: #ecfdf5; color: #065f46; }
    .badge-ai   { background: #eff6ff; color: #1e40af; }
    .badge-demo { background: #fef9c3; color: #713f12; }
    .tool-desc { font-size: 0.83rem; color: #4b5563; line-height: 1.55; margin-bottom: 1rem; }

    .btn-primary {
        display: inline-block;
        padding: 0.4rem 1.1rem;
        background: #1d4ed8;
        color: #fff !important;
        border-radius: 4px;
        text-decoration: none !important;
        font-size: 0.83rem;
        font-weight: 500;
    }
    .btn-primary:hover { background: #1e40af; }

    .info-card {
        border: 1px solid #e5e7eb;
        border-radius: 6px;
        padding: 1.1rem 1.25rem;
        background: #ffffff;
    }
    .info-card:hover { border-color: #93c5fd; }
    .info-title { font-size: 0.95rem; font-weight: 600; color: #111827; margin-bottom: 0.35rem; }
    .info-desc { font-size: 0.82rem; color: #4b5563; line-height: 1.5; margin-bottom: 0.75rem; }

    hr { border: none; border-top: 1px solid #e5e7eb; margin: 2rem 0; }
</style>
""", unsafe_allow_html=True)

# ── Hero ─────────────────────────────────────────────────────────────────────
col_hero, col_stats = st.columns([3, 2])

with col_hero:
    st.markdown("""
    <div class="hero-name">Connor <span>Shirley</span></div>
    <div class="hero-sub">RevOps Leader turned GTM Engineer &nbsp;·&nbsp; AI Deployment &nbsp;·&nbsp; CRM Architecture</div>
    <div class="hero-body">
        I build the systems that make revenue teams faster — from CRM architecture and tool stack
        design to AI agents and custom micro-apps. Seven years scaling B2B SaaS from seed to PE exit.
        Browse the tools below or learn more about my background.
    </div>
    """, unsafe_allow_html=True)
    st.markdown("<div style='margin-top:1rem'></div>", unsafe_allow_html=True)
    c1, c2 = st.columns(2)
    with c1:
        st.markdown('<a class="btn-primary" href="/1_About" target="_self">👤 About Me →</a>', unsafe_allow_html=True)
    with c2:
        st.markdown('<a class="btn-primary" href="/2_Resume" target="_self" style="background:#374151;">📄 View Resume →</a>', unsafe_allow_html=True)

with col_stats:
    st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
    s1, s2 = st.columns(2)
    with s1:
        st.markdown('<div class="stat-box"><div class="stat-num">7</div><div class="stat-label">Years in<br>B2B SaaS GTM</div></div>', unsafe_allow_html=True)
        st.markdown("<div style='height:0.6rem'></div>", unsafe_allow_html=True)
        st.markdown('<div class="stat-box"><div class="stat-num">20+</div><div class="stat-label">GTM Tools<br>Implemented</div></div>', unsafe_allow_html=True)
    with s2:
        st.markdown('<div class="stat-box"><div class="stat-num">5</div><div class="stat-label">Production AI<br>Apps Shipped</div></div>', unsafe_allow_html=True)
        st.markdown("<div style='height:0.6rem'></div>", unsafe_allow_html=True)
        st.markdown('<div class="stat-box"><div class="stat-num">$140M</div><div class="stat-label">Company Scale<br>Owned</div></div>', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ── Tools ─────────────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Tools & Demos</div>', unsafe_allow_html=True)

t1, t2, t3 = st.columns(3)

with t1:
    st.markdown("""
    <div class="tool-card">
        <div class="tool-name">📡 MX Lookup</div>
        <span class="tool-badge badge-live">● Live · No API Key</span>
        <div class="tool-desc">
            Identify any company's email provider via live DNS/MX record lookup.
            Detects Google Workspace, M365, Mimecast, Proofpoint, and 10+ more providers —
            with confidence scoring and CRM context.
        </div>
        <a class="btn-primary" href="/3_MX_Lookup" target="_self">Open MX Lookup →</a>
    </div>
    """, unsafe_allow_html=True)

with t2:
    st.markdown("""
    <div class="tool-card">
        <div class="tool-name">🤖 Company Summarizer</div>
        <span class="tool-badge badge-ai">✦ AI-Powered · Gemini</span>
        <div class="tool-desc">
            Enter a company name or domain and get an AI-generated GTM one-pager:
            overview, ICP, tech stack signals, buyer persona, and RevOps relevance.
            Built for sales reps who need fast, structured intel.
        </div>
        <a class="btn-primary" href="/4_Company_Summarizer" target="_self">Open Summarizer →</a>
    </div>
    """, unsafe_allow_html=True)

with t3:
    st.markdown("""
    <div class="tool-card">
        <div class="tool-name">🇫🇷 INSEE Gap Detector</div>
        <span class="tool-badge badge-demo">◎ Demo · Mock Data</span>
        <div class="tool-desc">
            Salesforce account coverage gap analysis for the French market.
            Uses SIREN numbers to surface companies that should be in your CRM
            but aren't — built on BigQuery + Salesforce API.
        </div>
        <a class="btn-primary" href="/5_INSEE_Gap_Detector" target="_self">Open Gap Detector →</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ── About & Resume ────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">About & Background</div>', unsafe_allow_html=True)

a1, a2, _ = st.columns([2, 2, 1])

with a1:
    st.markdown("""
    <div class="info-card">
        <div class="info-title">👤 About Me</div>
        <div class="info-desc">
            Seven years scaling B2B SaaS GTM from seed to PE exit.
            Background spans CRM architecture, AI tooling, multi-tool stack rollouts,
            and post-merger integrations. Currently open to senior RevOps &amp; GTM Engineering roles.
        </div>
        <a class="btn-primary" href="/1_About" target="_self">View Background →</a>
    </div>
    """, unsafe_allow_html=True)

with a2:
    st.markdown("""
    <div class="info-card">
        <div class="info-title">📄 Resume</div>
        <div class="info-desc">
            Full work history including LumApps, Acquire.io, Chili Piper, and Bright.md.
            View inline or download the PDF directly.
        </div>
        <a class="btn-primary" href="/2_Resume" target="_self" style="background:#374151;">View Resume →</a>
    </div>
    """, unsafe_allow_html=True)
