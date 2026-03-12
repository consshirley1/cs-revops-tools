import streamlit as st

st.set_page_config(page_title="About — Connor Smith", page_icon="👤", layout="wide")

st.markdown("""
<style>
    .page-title { font-size: 2rem; font-weight: 300; margin-bottom: 0.25rem; }
    .page-title span { color: #1d4ed8; }
    .section-label {
        font-size: 0.65rem; font-weight: 500; letter-spacing: 0.15em;
        text-transform: uppercase; color: #9ca3af; margin: 2rem 0 0.75rem;
    }
    .tag {
        display: inline-block;
        background: #eff6ff; color: #1d4ed8;
        font-size: 0.72rem; padding: 0.2rem 0.6rem;
        border-radius: 3px; margin: 0.2rem 0.2rem 0.2rem 0;
    }
    hr { border: none; border-top: 1px solid #e5e7eb; margin: 1.5rem 0; }
    .highlight {
        border-left: 3px solid #1d4ed8;
        padding-left: 1rem;
        color: #374151;
        font-size: 1rem;
        line-height: 1.7;
    }
</style>
""", unsafe_allow_html=True)

col_main, col_side = st.columns([3, 1])

with col_main:
    st.markdown('<div class="page-title">Connor <span>Smith</span></div>', unsafe_allow_html=True)
    st.markdown("**Revenue Operations Leader · GTM Engineer · AI Tooling**")
    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight">
    I build the systems, processes, and tooling that let go-to-market teams scale with precision.
    My background spans CRM architecture, GTM stack rollouts, and AI-powered automation —
    with a consistent focus on closing the gap between strategic intent and operational execution.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-label">What I Do</div>', unsafe_allow_html=True)
    st.markdown("""
    **GTM Stack Architecture** — I've led simultaneous multi-tool rollouts across Sales, Marketing,
    and CS, including an 11-tool deployment spanning Outreach, ZoomInfo, Spiff, Showpad, Nooks,
    LinkedIn Sales Navigator, and more. I own the full lifecycle: vendor selection, implementation,
    enablement, and governance.

    **AI-Powered RevOps Tooling** — I design and ship internal AI tools that actually get used.
    Recent work includes a five-agent automation system on Google Agentspace, a Gemini-powered
    sales Q&A bot backed by a 140-tab knowledge base, and an AI one-pager generator for sales reps.

    **CRM Strategy & Migration** — I've owned complex Salesforce migrations through post-merger
    integrations, including cross-org data reconciliation, field schema design, and executive
    stakeholder communication. I build the tooling that makes these projects visible and de-risked.

    **Data & Reporting Infrastructure** — From BigQuery pipelines to executive dashboards,
    I build the operational infrastructure that gives leadership a real-time pulse on pipeline
    health and GTM execution.
    """)

    st.markdown('<div class="section-label">Recent Work</div>', unsafe_allow_html=True)

    work = [
        ("2024–2025", "Head of Revenue Operations", "LumApps", "Led RevOps across a merged organization post-acquisition of Beekeeper. Owned CRM migration, GTM stack unification, and AI tooling strategy."),
    ]
    for year, title, company, desc in work:
        st.markdown(f"**{title}** · {company} · *{year}*")
        st.markdown(f"{desc}")
        st.markdown("")

    st.markdown('<div class="section-label">What I\'m Looking For</div>', unsafe_allow_html=True)
    st.markdown("""
    A senior RevOps or GTM Engineering role at a Series A–C SaaS company where I can:
    - Own the full GTM systems stack, not just administer it
    - Build AI-powered tooling that gives revenue teams a real edge
    - Work cross-functionally with Sales, Marketing, and Finance leadership
    - Have meaningful influence on how the company scales its go-to-market motion

    Remote-first or hybrid. Compensation commensurate with scope.
    """)

with col_side:
    st.markdown('<div class="section-label">Core Skills</div>', unsafe_allow_html=True)

    skills = [
        "Salesforce", "BigQuery", "Google Apps Script", "Python",
        "Outreach", "ZoomInfo", "Spiff", "Showpad", "Nooks",
        "Syncari", "Salesforce CPQ", "Planhat", "6sense",
        "Google Agentspace", "Gemini API", "Claude / Anthropic",
        "GTM Architecture", "CRM Migration", "RevOps Strategy",
        "Executive Reporting", "Data Governance",
    ]
    tags_html = "".join(f'<span class="tag">{s}</span>' for s in skills)
    st.markdown(tags_html, unsafe_allow_html=True)

    st.markdown('<div class="section-label">Domain Expertise</div>', unsafe_allow_html=True)
    st.markdown("""
    - Intranet / Digital Workplace SaaS
    - B2B Mid-Market & Enterprise
    - Post-merger GTM integration
    - French market (INSEE, SIREN)
    """)

    st.markdown('<div class="section-label">Contact</div>', unsafe_allow_html=True)
    st.markdown("""
    📧 connor@example.com  
    💼 [LinkedIn](https://linkedin.com/in/connor)  
    🐙 [GitHub](https://github.com/connor)
    """)
    st.info("👉 Update contact details before deploying.")
