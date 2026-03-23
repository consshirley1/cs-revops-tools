import streamlit as st
import streamlit.components.v1 as components
from shared import COMMON_CSS, DARK, TEAL_DARK, TEAL_MID, TEAL_LIGHT
from sidebar import render_sidebar


def home_page():
    st.set_page_config(
        page_title="Connor Shirley — RevOps Portfolio",
        page_icon="⚙️",
        layout="wide",
    )
    render_sidebar()

    st.markdown(COMMON_CSS, unsafe_allow_html=True)

    st.markdown(f"""
    <style>
        .hero-name  {{ font-size: 3rem; font-weight: 300; line-height: 1.1; margin-bottom: 0.4rem; color: {DARK}; }}
        .hero-name span {{ color: {TEAL_DARK}; }}
        .hero-sub   {{ font-size: 1rem; color: {TEAL_MID}; font-weight: 400; margin-bottom: 0.75rem; }}
        .hero-body  {{ font-size: 0.95rem; color: {DARK}; line-height: 1.7; max-width: 600px; margin-bottom: 1rem; }}

        .stat-box   {{
            background: {TEAL_LIGHT}; border: 1px solid {TEAL_MID}44;
            border-radius: 8px; padding: 1rem 0.75rem; text-align: center;
        }}
        .stat-num   {{ font-size: 1.8rem; font-weight: 300; color: {TEAL_DARK}; line-height: 1; }}
        .stat-label {{ font-size: 0.72rem; color: {DARK}; margin-top: 0.3rem; line-height: 1.3; }}
    </style>
    """, unsafe_allow_html=True)

    # ── Hero ──────────────────────────────────────────────────────────────────
    col_hero, col_stats = st.columns([3, 2])

    with col_hero:
        st.markdown(f"""
        <div class="hero-name">Connor <span>Shirley</span></div>
        <div class="hero-sub">RevOps Leader &nbsp;·&nbsp; GTM Engineer &nbsp;·&nbsp; AI Deployment &nbsp;·&nbsp; CRM Architecture</div>
        <div class="hero-body">
            I build the systems that make revenue teams more efficient and profitable — from CRM architecture and tool stack
            design to AI agents and custom micro-apps. Seven years scaling B2B SaaS from seed to PE exit.
            Browse the tools below or learn more about my background.
        </div>
        """, unsafe_allow_html=True)

        if st.button("About Me", key="hero_about", type="primary"):
            st.switch_page("pages/1_About.py")

    with col_stats:
        st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
        s1, s2 = st.columns(2)
        with s1:
            st.markdown(f'<div class="stat-box"><div class="stat-num">7</div><div class="stat-label">Years in<br>B2B SaaS GTM</div></div>', unsafe_allow_html=True)
            st.markdown("<div style='height:0.6rem'></div>", unsafe_allow_html=True)
            st.markdown(f'<div class="stat-box"><div class="stat-num">20+</div><div class="stat-label">GTM Tools<br>Implemented</div></div>', unsafe_allow_html=True)
        with s2:
            st.markdown(f'<div class="stat-box"><div class="stat-num">5</div><div class="stat-label">Production<br>Apps Shipped</div></div>', unsafe_allow_html=True)
            st.markdown("<div style='height:0.6rem'></div>", unsafe_allow_html=True)
            st.markdown(f'<div class="stat-box"><div class="stat-num">$140M</div><div class="stat-label">ARR<br>RevOps<br>Ownership</div></div>', unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)

    # ── Tools — Row 1 ─────────────────────────────────────────────────────────
    # ── Projects ──────────────────────────────────────────────────────────────
    st.markdown('<div class="section-label">Strategic Projects</div>', unsafe_allow_html=True)

    p1, p2, p3 = st.columns(3)

    with p1:
        st.markdown(f"""
        <div class="tool-card">
            <div class="tool-name">GTM Stack Unification</div>
            <span class="tool-badge badge-live">LumApps · 2024–2025</span>
            <div class="tool-desc">Merged 15 tools into a single unified stack post-acquisition,
            including 2 CRMs and 2 MAPs — across a 150-person GTM org.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View Project", key="proj_la3", type="primary", use_container_width=True):
            st.switch_page("pages/6_Projects.py")

    with p2:
        st.markdown(f"""
        <div class="tool-card">
            <div class="tool-name">AI Micro-App Suite</div>
            <span class="tool-badge badge-ai">AI-Powered · Claude + Gemini</span>
            <div class="tool-desc">5 production AI apps shipped in 6 weeks: intent enrichment,
            data enrichment, one-pager generation, inbound SDR, and competitor detection.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View Project", key="proj_ai", type="primary", use_container_width=True):
            st.switch_page("pages/6_Projects.py")

    with p3:
        st.markdown(f"""
        <div class="tool-card">
            <div class="tool-name">MEDDPIC & Forecast Rebuild</div>
            <span class="tool-badge badge-live">LumApps · 2022–2023</span>
            <div class="tool-desc">Standardized MEDDPIC across an 80-person international org
            and rebuilt forecast infrastructure — improving accuracy by 60%+.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View Project", key="proj_meddpic", type="primary", use_container_width=True):
            st.switch_page("pages/6_Projects.py")

    if st.button("View All Projects", key="card_projects", type="secondary"):
        st.session_state.pop("selected_project_id", None)
        st.switch_page("pages/6_Projects.py")

    st.markdown("<hr>", unsafe_allow_html=True)

    # ── Tools ─────────────────────────────────────────────────────────────────
    st.markdown('<div class="section-label">Tools & Demos</div>', unsafe_allow_html=True)

    t1, t2, t3 = st.columns(3)

    with t1:
        st.markdown(f"""
        <div class="tool-card">
            <div class="tool-name">MX Lookup</div>
            <span class="tool-badge badge-live">Live · No API Key</span>
            <div class="tool-desc">Identify any company's email provider via live DNS/MX record lookup.
            Detects Google Workspace, M365, Mimecast, Proofpoint, and 10+ more —
            with confidence scoring and CRM context.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open MX Lookup", key="tool_mx", type="primary", use_container_width=True):
            st.switch_page("pages/3_MX_Lookup.py")

    with t2:
        st.markdown(f"""
        <div class="tool-card">
            <div class="tool-name">Company Summarizer</div>
            <span class="tool-badge badge-ai">AI-Powered · Gemini</span>
            <div class="tool-desc">Enter a company name or domain and get an AI-generated GTM one-pager:
            overview, ICP, tech stack signals, buyer persona, and RevOps relevance.
            Built for sales reps who need fast, structured intel.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Summarizer", key="tool_summarizer", type="primary", use_container_width=True):
            st.switch_page("pages/4_Company_Summarizer.py")

    with t3:
        st.markdown(f"""
        <div class="tool-card">
            <div class="tool-name">INSEE Gap Detector</div>
            <span class="tool-badge badge-demo">Demo · Mock Data</span>
            <div class="tool-desc">Salesforce account coverage gap analysis for the French market.
            Uses SIREN numbers to surface companies missing from your CRM —
            built on BigQuery + Salesforce API.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Gap Detector", key="tool_insee", type="primary", use_container_width=True):
            st.switch_page("pages/5_INSEE_Gap_Detector.py")

    # ── Tools — Row 2 ─────────────────────────────────────────────────────────
    t4, t5, t6, t7 = st.columns(4)

    with t4:
        st.markdown(f"""
        <div class="tool-card">
            <div class="tool-name">Lead Researcher</div>
            <span class="tool-badge badge-ai">AI-Powered · Gemini</span>
            <div class="tool-desc">Paste a LinkedIn bio or About Us text to get a RevOps-ready brief:
            3-sentence summary, revenue team pain points, and a personalized outreach hook.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Researcher", key="tool_research", type="primary", use_container_width=True):
            st.switch_page("pages/7_Lead_Researcher.py")

    with t5:
        st.markdown(f"""
        <div class="tool-card">
            <div class="tool-name">White Space Mapper</div>
            <span class="tool-badge badge-sfdc">Salesforce · Demo</span>
            <div class="tool-desc">Simulates a Salesforce white space analysis — identifying cross-sell
            gaps in your account base by product penetration and industry,
            with recommended next plays per account.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Mapper", key="tool_mapper", type="primary", use_container_width=True):
            st.switch_page("pages/8_SFDC_Account_Mapper.py")

    with t6:
        st.markdown(f"""
        <div class="tool-card">
            <div class="tool-name">Permission Auditor</div>
            <span class="tool-badge badge-sfdc">Salesforce · Demo</span>
            <div class="tool-desc">Identifies permission creep by auditing Salesforce user rights
            against a defined security baseline — surfacing high-risk violations
            and recommending a least-privilege remediation model.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Auditor", key="tool_perm", type="primary", use_container_width=True):
            st.switch_page("pages/9_SFDC_Perm.py")

    with t7:
        st.markdown(f"""
        <div class="tool-card">
            <div class="tool-name">SOQL Translator</div>
            <span class="tool-badge badge-ai">AI-Powered · Gemini</span>
            <div class="tool-desc">Converts natural language to Salesforce SOQL — and includes a
            visual query builder so non-technical stakeholders can understand
            the queries running their business.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Open Translator", key="tool_soql", type="primary", use_container_width=True):
            st.switch_page("pages/10_SOQL_to_Human.py")

    st.markdown("<hr>", unsafe_allow_html=True)

    # ── About & Background ────────────────────────────────────────────────────
    st.markdown('<div class="section-label">About & Background</div>', unsafe_allow_html=True)

    a1, a2 = st.columns(2)

    with a1:
        st.markdown(f"""
        <div class="info-card">
            <div class="info-title">About Me</div>
            <div class="info-desc">Seven years scaling B2B SaaS GTM from seed to PE exit.
            Background spans CRM architecture, AI tooling, multi-tool stack rollouts,
            and post-merger integrations. Currently open to senior RevOps &amp; GTM Engineering roles.</div>
        </div>
        """, unsafe_allow_html=True)
        if st.button("View Background", key="card_about", type="primary", use_container_width=True):
            st.switch_page("pages/1_About.py")

    with a2:
        st.markdown(f"""
        <div class="info-card">
            <div class="info-title">Get In Touch</div>
            <div class="info-desc">Open to senior RevOps and GTM Engineering opportunities.
            Based in the US — available for remote or hybrid roles.</div>
        </div>
        """, unsafe_allow_html=True)
        st.link_button(
            "Connect on LinkedIn",
            "https://www.linkedin.com/in/connor-shirley-93986954/",
            use_container_width=True,
        )

    components.html("""
<script>
(function() {
    var doc = window.parent.document;
    function eq() {
        doc.querySelectorAll('.stHorizontalBlock').forEach(function(row) {
            var cards = Array.from(row.querySelectorAll('.tool-card'));
            if (cards.length < 2) return;
            cards.forEach(function(c) { c.style.minHeight = ''; });
            var maxH = Math.max.apply(null, cards.map(function(c) { return c.offsetHeight; }));
            cards.forEach(function(c) { c.style.minHeight = maxH + 'px'; });
        });
    }
    var timer;
    var obs = new MutationObserver(function() {
        clearTimeout(timer);
        timer = setTimeout(eq, 100);
    });
    obs.observe(doc.body, {childList: true, subtree: true});
    eq();
    setTimeout(function() { obs.disconnect(); }, 10000);
}());
</script>
""", height=0)


# ── Navigation shell ──────────────────────────────────────────────────────────
pg = st.navigation(
    {
        "": [
            st.Page(home_page, title="Home", default=True),
        ],
        "Background": [
            st.Page("pages/1_About.py", title="About"),
            st.Page("pages/ask_connor.py", title="Ask Connor"),
        ],
        "Projects": [
            st.Page("pages/6_Projects.py", title="Projects"),
        ],
        "Tools": [
            st.Page("pages/3_MX_Lookup.py",          title="MX Lookup"),
            st.Page("pages/4_Company_Summarizer.py",  title="Company Summarizer"),
            st.Page("pages/5_INSEE_Gap_Detector.py",  title="INSEE Gap Detector"),
            st.Page("pages/7_Lead_Researcher.py",     title="Lead Researcher"),
            st.Page("pages/8_SFDC_Account_Mapper.py", title="White Space Mapper"),
            st.Page("pages/9_SFDC_Perm.py",           title="Permission Auditor"),
            st.Page("pages/10_SOQL_to_Human.py",      title="SOQL Translator"),
        ],
    }
)
pg.run()
