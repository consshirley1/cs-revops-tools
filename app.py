import streamlit as st


def home_page():
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
        .hero-body { font-size: 0.95rem; color: #374151; line-height: 1.7; max-width: 600px; margin-bottom: 1rem; }

        .section-label {
            font-size: 0.62rem; font-weight: 600; letter-spacing: 0.18em;
            text-transform: uppercase; color: #9ca3af; margin-bottom: 0.75rem;
        }
        .stat-box {
            background: #f8fafc; border: 1px solid #e5e7eb;
            border-radius: 6px; padding: 1rem 0.75rem; text-align: center;
        }
        .stat-num { font-size: 1.8rem; font-weight: 300; color: #1d4ed8; line-height: 1; }
        .stat-label { font-size: 0.72rem; color: #6b7280; margin-top: 0.3rem; line-height: 1.3; }

        .tool-card {
            border: 1px solid #e5e7eb; border-radius: 6px;
            padding: 1.25rem 1.25rem 0.75rem 1.25rem; background: #ffffff;
        }
        .tool-name { font-size: 1rem; font-weight: 600; color: #111827; margin-bottom: 0.2rem; }
        .tool-badge {
            display: inline-block; font-size: 0.68rem; font-weight: 500;
            padding: 0.15rem 0.55rem; border-radius: 99px; margin-bottom: 0.65rem;
        }
        .badge-live { background: #ecfdf5; color: #065f46; }
        .badge-ai   { background: #eff6ff; color: #1e40af; }
        .badge-demo { background: #fef9c3; color: #713f12; }
        .tool-desc { font-size: 0.83rem; color: #4b5563; line-height: 1.55; margin-bottom: 0.5rem; }

        .info-card {
            border: 1px solid #e5e7eb; border-radius: 6px;
            padding: 1.1rem 1.25rem 0.75rem 1.25rem; background: #ffffff;
        }
        .info-title { font-size: 0.95rem; font-weight: 600; color: #111827; margin-bottom: 0.35rem; }
        .info-desc { font-size: 0.82rem; color: #4b5563; line-height: 1.5; margin-bottom: 0.5rem; }

        hr { border: none; border-top: 1px solid #e5e7eb; margin: 2rem 0; }

        div.stButton > button[kind="primary"] {
            background-color: #1d4ed8 !important; color: white !important;
            border: none !important; font-size: 0.83rem !important;
            font-weight: 500 !important; border-radius: 4px !important;
        }
        div.stButton > button[kind="primary"]:hover { background-color: #1e40af !important; }
        div.stButton > button[kind="secondary"] {
            background-color: #374151 !important; color: white !important;
            border: none !important; font-size: 0.83rem !important;
            font-weight: 500 !important; border-radius: 4px !important;
        }
        div.stButton > button[kind="secondary"]:hover {
            background-color: #1f2937 !important; color: white !important;
        }
    </style>
    """, unsafe_allow_html=True)

    # ── Hero ──────────────────────────────────────────────────────────────────
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

        b1, b2 = st.columns(2)
        with b1:
            if st.button("👤 About Me →", key="hero_about", type="primary", use_container_width=True):
                st.switch_page("pages/1_About.py")
        with b2:
            if st.button("📄 View Resume →", key="hero_resume", type="secondary", use_container_width=True):
                st.switch_page("pages/2_Resume.py")

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

    # ── Tools ─────────────────────────────────────────────────────────────────
    st.markdown('<div class="section-label">Tools & Demos</div>', unsafe_allow_html=True)

    t1, t2, t3 = st.columns(3)

    with t1:
        st.markdown("""
        <div class="tool-card">
            <div class="tool-name">📡 MX Lookup</div>
            <span class="tool-badge badge-live">● Live · No API Key</span>
            <div class="tool-desc">Identify any company's email provider via live DNS/MX record lookup.
            Detects Google Workspace, M365, Mimecast, Proofpoint, and 10+ more —
            with confidence scoring and CRM context.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open MX Lookup →", key="tool_mx", type="primary", use_container_width=True):
            st.switch_page("pages/3_MX_Lookup.py")

    with t2:
        st.markdown("""
        <div class="tool-card">
            <div class="tool-name">🤖 Company Summarizer</div>
            <span class="tool-badge badge-ai">✦ AI-Powered · Gemini</span>
            <div class="tool-desc">Enter a company name or domain and get an AI-generated GTM one-pager:
            overview, ICP, tech stack signals, buyer persona, and RevOps relevance.
            Built for sales reps who need fast, structured intel.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Summarizer →", key="tool_summarizer", type="primary", use_container_width=True):
            st.switch_page("pages/4_Company_Summarizer.py")

    with t3:
        st.markdown("""
        <div class="tool-card">
            <div class="tool-name">🇫🇷 INSEE Gap Detector</div>
            <span class="tool-badge badge-demo">◎ Demo · Mock Data</span>
            <div class="tool-desc">Salesforce account coverage gap analysis for the French market.
            Uses SIREN numbers to surface companies missing from your CRM —
            built on BigQuery + Salesforce API.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Gap Detector →", key="tool_insee", type="primary", use_container_width=True):
            st.switch_page("pages/5_INSEE_Gap_Detector.py")

    st.markdown("<hr>", unsafe_allow_html=True)

    # ── Projects ──────────────────────────────────────────────────────────────
    st.markdown('<div class="section-label">Strategic Projects</div>', unsafe_allow_html=True)

    p1, p2, p3, _ = st.columns([2, 2, 2, 1])

    with p1:
        st.markdown("""
        <div class="tool-card">
            <div class="tool-name">🗂️ GTM Stack Unification</div>
            <span class="tool-badge badge-live">● LumApps · 2024–2025</span>
            <div class="tool-desc">Merged 15 tools into a single unified stack post-acquisition,
            including 2 CRMs and 2 MAPs — across a 150-person GTM org.</div>
        </div>
        """, unsafe_allow_html=True)

    with p2:
        st.markdown("""
        <div class="tool-card">
            <div class="tool-name">🤖 AI Micro-App Suite</div>
            <span class="tool-badge badge-ai">✦ AI-Powered · Claude + Gemini</span>
            <div class="tool-desc">5 production AI apps shipped in 6 weeks: intent enrichment,
            data enrichment, one-pager generation, inbound SDR, and competitor detection.</div>
        </div>
        """, unsafe_allow_html=True)

    with p3:
        st.markdown("""
        <div class="tool-card">
            <div class="tool-name">📈 MEDDPIC & Forecast Rebuild</div>
            <span class="tool-badge badge-live">● LumApps · 2022–2023</span>
            <div class="tool-desc">Standardized MEDDPIC across an 80-person international org
            and rebuilt forecast infrastructure — improving accuracy by 60%+.</div>
        </div>
        """, unsafe_allow_html=True)

    if st.button("View All Projects →", key="card_projects", type="primary"):
        st.switch_page("pages/6_Projects.py")

    st.markdown("<hr>", unsafe_allow_html=True)

    # ── About & Resume ────────────────────────────────────────────────────────
    st.markdown('<div class="section-label">About & Background</div>', unsafe_allow_html=True)

    a1, a2, _ = st.columns([2, 2, 1])

    with a1:
        st.markdown("""
        <div class="info-card">
            <div class="info-title">👤 About Me</div>
            <div class="info-desc">Seven years scaling B2B SaaS GTM from seed to PE exit.
            Background spans CRM architecture, AI tooling, multi-tool stack rollouts,
            and post-merger integrations. Currently open to senior RevOps &amp; GTM Engineering roles.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View Background →", key="card_about", type="primary", use_container_width=True):
            st.switch_page("pages/1_About.py")

    with a2:
        st.markdown("""
        <div class="info-card">
            <div class="info-title">📄 Resume</div>
            <div class="info-desc">Full work history including LumApps, Acquire.io, Chili Piper, and Bright.md.
            View inline or download the PDF directly.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View Resume →", key="card_resume", type="secondary", use_container_width=True):
            st.switch_page("pages/2_Resume.py")


# ── Navigation shell ──────────────────────────────────────────────────────────
pg = st.navigation(
    {
        "": [
            st.Page(home_page, title="Home", icon="🏠", default=True),
        ],
        "Background": [
            st.Page("pages/1_About.py", title="About", icon="👤"),
            st.Page("pages/2_Resume.py", title="Resume", icon="📄"),
        ],
        "Tools": [
            st.Page("pages/3_MX_Lookup.py", title="MX Lookup", icon="📡"),
            st.Page("pages/4_Company_Summarizer.py", title="Company Summarizer", icon="🤖"),
            st.Page("pages/5_INSEE_Gap_Detector.py", title="INSEE Gap Detector", icon="🇫🇷"),
        ],
        "Projects": [
            st.Page("pages/6_Projects.py", title="Projects", icon="🗂️"),
        ],
    }
)
pg.run()
