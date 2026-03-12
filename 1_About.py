import streamlit as st

st.set_page_config(page_title="About — Connor Shirley", page_icon="👤", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #ffffff; }
    section[data-testid="stSidebar"] { background-color: #f8fafc; }

    .page-title { font-size: 2.2rem; font-weight: 300; margin-bottom: 0.15rem; color: #111827; }
    .page-title span { color: #1d4ed8; }
    .page-sub { font-size: 0.95rem; color: #6b7280; font-weight: 400; margin-bottom: 0.25rem; }

    .section-label {
        font-size: 0.62rem; font-weight: 600; letter-spacing: 0.18em;
        text-transform: uppercase; color: #9ca3af; margin: 2rem 0 0.75rem;
    }

    .highlight {
        border-left: 3px solid #1d4ed8;
        padding: 0.75rem 1rem;
        background: #f8fafc;
        color: #374151;
        font-size: 1rem;
        line-height: 1.75;
        border-radius: 0 4px 4px 0;
        margin-bottom: 0.5rem;
    }

    .job-card {
        border: 1px solid #e5e7eb;
        border-radius: 6px;
        padding: 1rem 1.25rem;
        margin-bottom: 0.85rem;
        background: #ffffff;
    }
    .job-card:hover { border-color: #93c5fd; }
    .job-title { font-size: 0.95rem; font-weight: 600; color: #111827; margin-bottom: 0.1rem; }
    .job-meta { font-size: 0.78rem; color: #6b7280; margin-bottom: 0.6rem; }
    .job-desc { font-size: 0.85rem; color: #374151; line-height: 1.6; }
    .job-bullet { font-size: 0.84rem; color: #374151; line-height: 1.6; padding-left: 0.2rem; }

    .tag {
        display: inline-block;
        background: #eff6ff; color: #1d4ed8;
        font-size: 0.72rem; padding: 0.2rem 0.65rem;
        border-radius: 3px; margin: 0.2rem 0.2rem 0.2rem 0;
        font-weight: 500;
    }
    .tag-gray {
        display: inline-block;
        background: #f3f4f6; color: #4b5563;
        font-size: 0.72rem; padding: 0.2rem 0.65rem;
        border-radius: 3px; margin: 0.2rem 0.2rem 0.2rem 0;
        font-weight: 500;
    }
    .tag-green {
        display: inline-block;
        background: #ecfdf5; color: #065f46;
        font-size: 0.72rem; padding: 0.2rem 0.65rem;
        border-radius: 3px; margin: 0.2rem 0.2rem 0.2rem 0;
        font-weight: 500;
    }

    .project-card {
        background: #f8fafc;
        border: 1px solid #e5e7eb;
        border-radius: 6px;
        padding: 0.85rem 1rem;
        margin-bottom: 0.6rem;
    }
    .project-title { font-size: 0.88rem; font-weight: 600; color: #1d4ed8; margin-bottom: 0.2rem; }
    .project-desc { font-size: 0.82rem; color: #4b5563; line-height: 1.5; }

    .edu-item { font-size: 0.85rem; color: #374151; margin-bottom: 0.4rem; line-height: 1.5; }
    .edu-item strong { color: #111827; }

    hr { border: none; border-top: 1px solid #e5e7eb; margin: 1.5rem 0; }
    .stat-row { display: flex; gap: 1.5rem; margin: 1rem 0; }
    .stat-item { text-align: center; }
    .stat-num { font-size: 1.6rem; font-weight: 300; color: #1d4ed8; line-height: 1; }
    .stat-lbl { font-size: 0.7rem; color: #9ca3af; margin-top: 0.1rem; }
</style>
""", unsafe_allow_html=True)

col_main, col_side = st.columns([3, 1])

with col_main:
    st.markdown('<div class="page-title">Connor <span>Shirley</span></div>', unsafe_allow_html=True)
    st.markdown('<div class="page-sub">RevOps Leader turned GTM Engineer &nbsp;·&nbsp; AI Deployment &nbsp;·&nbsp; CRM Architecture &nbsp;·&nbsp; $140M Scale</div>', unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

    st.markdown("""
    <div class="highlight">
    I build the systems that make revenue teams faster — from CRM architecture and tool stack design
    to AI agents and custom micro-apps. Seven years scaling B2B SaaS GTM from seed to PE exit, with
    hands-on ownership of forecasting, acquisition integrations, and live AI deployment. I sit at the
    intersection of GTM and engineering, which means I can design it, build it, and get buy-in on it.
    </div>
    """, unsafe_allow_html=True)

    # Quick stats
    st.markdown("""
    <div class="stat-row">
        <div class="stat-item"><div class="stat-num">7</div><div class="stat-lbl">Years in B2B SaaS GTM</div></div>
        <div class="stat-item"><div class="stat-num">5</div><div class="stat-lbl">Production AI Apps Shipped</div></div>
        <div class="stat-item"><div class="stat-num">20+</div><div class="stat-lbl">GTM Tools Implemented</div></div>
        <div class="stat-item"><div class="stat-num">$140M</div><div class="stat-lbl">Company Scale Owned</div></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-label">What I Do</div>', unsafe_allow_html=True)
    st.markdown("""
    **GTM Stack Architecture** — I've led simultaneous multi-tool rollouts across Sales, Marketing,
    and CS, including 20+ tool deployments over four years spanning Outreach, ZoomInfo, Spiff, Showpad,
    Nooks, LinkedIn Sales Navigator, and more. I own the full lifecycle: vendor selection, implementation,
    enablement, and governance.

    **AI-Powered RevOps Tooling** — I design and ship internal AI tools that actually get used.
    Recent work includes 5 production AI micro-apps (intent enrichment, custom data enrichment,
    one-pager generation, inbound SDR, competitor detection) using Claude and Gemini, deployed to a
    150-person GTM org in 6 weeks.

    **CRM Strategy & Migration** — I've owned complex Salesforce migrations through post-merger
    integrations, including cross-org data reconciliation, field schema design, and executive
    stakeholder communication. I build the tooling that makes these projects visible and de-risked.

    **Data & Reporting Infrastructure** — From BigQuery pipelines to executive dashboards,
    I build the operational infrastructure that gives leadership a real-time pulse on pipeline
    health and GTM execution.
    """)

    st.markdown('<div class="section-label">Experience</div>', unsafe_allow_html=True)

    experience = [
        {
            "title": "Deputy VP RevOps, Head of Strategy & Analytics",
            "company": "LumApps — B2B SaaS",
            "dates": "January 2026 – Present",
            "bullets": [
                "Developed company AI roadmap connecting agent layer, CRM data layer, and API mesh across 11-tool GTM stack, identifying $200k in tool spend optimization.",
                "Built 5 production AI micro-apps (intent enrichment, custom data enrichment, one-pager generation, inbound SDR, competitor detection) using Claude and Gemini — deployed to 150-person GTM org in 6 weeks.",
            ]
        },
        {
            "title": "GTM Sales Strategy Director",
            "company": "LumApps — B2B SaaS",
            "dates": "December 2021 – December 2025",
            "desc": "Head of Revenue Operations for an Intranet B2B SaaS company selling to the F500.",
            "bullets": [
                "Led RevOps through $60M to $140M company growth across all parts of the revenue lifecycle — standardized roadmap, built documentation and approval processes, implemented 20+ tools over 4 years.",
                "Standardized MEDDPIC methodology and process across an 80-person international sales org, improving forecast accuracy by over 60%.",
                "Designed and hired NORAM GTM teams that drove the largest quarters in company history, including a successful exit to PE.",
                "Established Account Management function that led to $2M+ in additional bookings the following fiscal year.",
                "Owned multiple acquisition integration projects, including a 400-person, $40M acquisition spanning multiple ERP/CRM/MAP platforms.",
            ]
        },
        {
            "title": "Sales Operations Manager",
            "company": "Acquire.io — B2B SaaS",
            "dates": "May 2021 – December 2021",
            "desc": "Owned both Enablement and RevOps at a customer support platform for enterprise companies.",
            "bullets": [
                "Built SDR improvement training focused on outbound strategy — improved Stage 1 Opp performance by 120% in 2 quarters and helped land a $1.1M Enterprise deal.",
            ]
        },
        {
            "title": "Sales Strategy & Enablement Manager",
            "company": "Chili Piper — B2B SaaS",
            "dates": "November 2020 – May 2021",
            "desc": "Owned strategy and enablement in the RevOps department at a calendar scheduling SaaS company.",
            "bullets": [
                "TAM/ICP analysis and strategy that unlocked new potential verticals and use cases, generating ~$250k in additional pipeline in the next two fiscal quarters.",
            ]
        },
        {
            "title": "Manager, Sales Operations & Enablement · SDR",
            "company": "Bright.md — Healthcare B2B SaaS",
            "dates": "August 2018 – November 2020",
            "desc": "Second GTM hire at a telehealth company selling to enterprise healthcare systems.",
            "bullets": [
                "Grew the sales team from 4 to 15 and 3x'd company revenue (0 to $10M).",
                "Developed and owned all RevOps/Enablement functions from the ground up (CRM implementation, MAP).",
                "As the first SDR hire, generated $7.86M in pipeline (131% of quota).",
            ]
        },
    ]

    for job in experience:
        bullets_html = "".join(f'<div class="job-bullet">• {b}</div>' for b in job["bullets"])
        desc_html = f'<div class="job-desc" style="margin-bottom:0.4rem;font-style:italic;">{job["desc"]}</div>' if "desc" in job else ""
        st.markdown(f"""
        <div class="job-card">
            <div class="job-title">{job['title']}</div>
            <div class="job-meta">{job['company']} &nbsp;·&nbsp; {job['dates']}</div>
            {desc_html}
            {bullets_html}
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="section-label">Key Projects</div>', unsafe_allow_html=True)

    projects = [
        ("LA3.0 — GTM Stack Unification", "Merged 15 tools into a unified stack post-acquisition, including 2 CRMs and 2 MAPs. Owned architecture, migration sequencing, and org-wide enablement."),
        ("INSEE × SFDC Gap Detector", "Custom data tool for Sales targeting French market accounts. Built using BigQuery + Salesforce API + Google Apps Script to surface accounts missing from CRM."),
        ("Competitive Intelligence Pipeline", "Python script that scrapes DNS, MX, CRT, and CNAME records to identify competitor tech deployments — used by SDRs for precision outbound targeting."),
    ]
    for title, desc in projects:
        st.markdown(f"""
        <div class="project-card">
            <div class="project-title">{title}</div>
            <div class="project-desc">{desc}</div>
        </div>
        """, unsafe_allow_html=True)

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

    skills_tech = [
        "Salesforce", "BigQuery", "Google Apps Script", "Python",
        "Outreach", "ZoomInfo", "Spiff", "Showpad", "Nooks",
        "Syncari", "Salesforce CPQ", "Planhat", "6sense",
        "Google Agentspace", "Gemini API", "Claude / Anthropic",
    ]
    skills_ops = [
        "CRM Administration", "GTM Architecture", "CRM Migration",
        "ICP/TAM Analysis", "AI Deployment", "Project Management",
        "Executive Reporting", "Data Governance", "Corporate Strategy",
    ]
    skills_method = [
        "MEDDPIC", "Challenger", "JOLT", "Command of the Message",
    ]

    st.markdown("**Tech & Tools**")
    st.markdown("".join(f'<span class="tag">{s}</span>' for s in skills_tech), unsafe_allow_html=True)

    st.markdown("<div style='margin-top:0.75rem'><strong>RevOps & Strategy</strong></div>", unsafe_allow_html=True)
    st.markdown("".join(f'<span class="tag-gray">{s}</span>' for s in skills_ops), unsafe_allow_html=True)

    st.markdown("<div style='margin-top:0.75rem'><strong>Methodologies</strong></div>", unsafe_allow_html=True)
    st.markdown("".join(f'<span class="tag-green">{s}</span>' for s in skills_method), unsafe_allow_html=True)

    st.markdown('<div class="section-label">Domain Expertise</div>', unsafe_allow_html=True)
    st.markdown("""
    - Intranet / Digital Workplace SaaS
    - B2B Mid-Market & Enterprise (F500)
    - Post-merger GTM integration
    - French market (INSEE / SIREN)
    - Seed → PE Exit journeys
    """)

    st.markdown('<div class="section-label">Education</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="edu-item">
        <strong>B.A., MENAS & Criminal Justice</strong><br>
        University of Arizona, Tucson
    </div>
    <div class="edu-item">
        <strong>MEDDPICC Academy for Managers</strong>
    </div>
    <div class="edu-item">
        <strong>IBM — RAG & Agentic AI</strong>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-label">Interests</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="edu-item">Fountain pen enthusiast &amp; avid literature reader</div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-label">Contact</div>', unsafe_allow_html=True)
    st.markdown("""
📞 [(509) 496-7013](tel:5094967013)
📧 [consshirley@gmail.com](mailto:consshirley@gmail.com)
💼 [LinkedIn](https://www.linkedin.com/in/connor-shirley-93986954/)
🐙 [GitHub](https://github.com/consshirley1)
    """)
