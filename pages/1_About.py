import streamlit as st
from pathlib import Path
from shared import COMMON_CSS, DARK, TEAL_DARK, TEAL_MID, TEAL_LIGHT

st.set_page_config(page_title="About — Connor Shirley", page_icon=None, layout="wide")
st.markdown(COMMON_CSS, unsafe_allow_html=True)

st.markdown(f"""
<style>
    .tag {{
        display: inline-block; background: {TEAL_LIGHT}; color: {TEAL_DARK};
        font-size: 0.72rem; padding: 0.2rem 0.65rem; border-radius: 3px;
        margin: 0.2rem 0.2rem 0.2rem 0; font-weight: 500;
    }}
    .tag-gray {{
        display: inline-block; background: {TEAL_LIGHT}; color: {DARK};
        font-size: 0.72rem; padding: 0.2rem 0.65rem; border-radius: 3px;
        margin: 0.2rem 0.2rem 0.2rem 0; font-weight: 500;
    }}
    .tag-green {{
        display: inline-block; background: {TEAL_LIGHT}; color: {TEAL_MID};
        font-size: 0.72rem; padding: 0.2rem 0.65rem; border-radius: 3px;
        margin: 0.2rem 0.2rem 0.2rem 0; font-weight: 500;
    }}
    .stat-num {{ font-size: 1.8rem; font-weight: 300; color: {TEAL_DARK}; }}
    .stat-label {{ font-size: 0.78rem; color: {DARK}; margin-top: 0.2rem; }}
</style>
""", unsafe_allow_html=True)

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(f"<div class='section-label'>Core Skills</div>", unsafe_allow_html=True)

    skills_tech = ["Salesforce", "BigQuery", "Google Apps Script", "Python",
                   "Outreach", "ZoomInfo", "Spiff", "Showpad", "Nooks",
                   "Syncari", "Salesforce CPQ", "Planhat", "6sense",
                   "Google Agentspace", "Gemini API", "Claude / Anthropic"]
    skills_ops  = ["CRM Administration", "GTM Architecture", "CRM Migration",
                   "ICP/TAM Analysis", "AI Deployment", "Project Management",
                   "Executive Reporting", "Data Governance", "Corporate Strategy"]
    skills_meth = ["MEDDPIC", "Challenger", "JOLT", "Command of the Message"]

    st.markdown(f"<div class='section-label' style='margin-top:0.5rem;'>Tech & Tools</div>", unsafe_allow_html=True)
    st.markdown("".join(f'<span class="tag">{s}</span>' for s in skills_tech), unsafe_allow_html=True)
    st.markdown(f"<div class='section-label' style='margin-top:0.75rem;'>RevOps & Strategy</div>", unsafe_allow_html=True)
    st.markdown("".join(f'<span class="tag-gray">{s}</span>' for s in skills_ops), unsafe_allow_html=True)
    st.markdown(f"<div class='section-label' style='margin-top:0.75rem;'>Methodologies</div>", unsafe_allow_html=True)
    st.markdown("".join(f'<span class="tag-green">{s}</span>' for s in skills_meth), unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(f"<div class='section-label'>Domain Expertise</div>", unsafe_allow_html=True)
    st.markdown(f"""
<p style='font-size:0.82rem;color:{DARK};line-height:1.6;'>
Intranet / Digital Workplace SaaS<br>
B2B Mid-Market &amp; Enterprise (F500)<br>
Post-merger GTM integration<br>
French market (INSEE / SIREN)<br>
Seed to PE Exit journeys
</p>""", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(f"<div class='section-label'>Education</div>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:0.82rem;color:{DARK};line-height:1.6;'><strong>B.A., MENAS &amp; Criminal Justice</strong><br>University of Arizona, Tucson<br><br><strong>MEDDPICC Academy for Managers</strong><br><br><strong>IBM — RAG &amp; Agentic AI</strong></p>", unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown(f"<div class='section-label'>Contact</div>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size:0.82rem;color:{DARK};line-height:1.8;'><a href='tel:5094967013' style='color:{TEAL_DARK};'>(509) 496-7013</a><br><a href='mailto:consshirley@gmail.com' style='color:{TEAL_DARK};'>consshirley@gmail.com</a><br><a href='https://www.linkedin.com/in/connor-shirley-93986954/' style='color:{TEAL_DARK};'>LinkedIn</a><br><a href='https://github.com/consshirley1' style='color:{TEAL_DARK};'>GitHub</a></p>", unsafe_allow_html=True)

# ── Main content ──────────────────────────────────────────────────────────────
st.markdown('<div class="page-title">Connor <span>Shirley</span></div>', unsafe_allow_html=True)
st.markdown(f"<p style='color:{TEAL_MID};font-size:0.95rem;'>RevOps Leader turned GTM Engineer &nbsp;·&nbsp; AI Deployment &nbsp;·&nbsp; CRM Architecture &nbsp;·&nbsp; $140M Scale</p>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

st.markdown(f"""
<div style='background:{TEAL_LIGHT};border-radius:8px;padding:1.1rem 1.25rem;margin-bottom:1.25rem;font-size:0.9rem;color:{DARK};line-height:1.7;'>
I build the systems that make revenue teams faster — from CRM architecture and tool stack design
to AI agents and custom micro-apps. Seven years scaling B2B SaaS GTM from seed to PE exit, with
hands-on ownership of forecasting, acquisition integrations, and live AI deployment. I sit at the
intersection of GTM and engineering, which means I can design it, build it, and get buy-in on it.
</div>
""", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
for col, num, label in [
    (c1, "7",     "Years in B2B SaaS GTM"),
    (c2, "5",     "Production AI Apps Shipped"),
    (c3, "20+",   "GTM Tools Implemented"),
    (c4, "$140M", "Company Scale Owned"),
]:
    col.markdown(f"""
    <div style='text-align:center;padding:0.75rem 0;'>
        <div class='stat-num'>{num}</div>
        <div class='stat-label'>{label}</div>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ── What I Do ─────────────────────────────────────────────────────────────────
st.markdown(f"<h3 style='color:{DARK};font-weight:400;'>What I Do</h3>", unsafe_allow_html=True)

for title, body in [
    ("GTM Stack Architecture",
     "Led simultaneous multi-tool rollouts across Sales, Marketing, and CS, including 20+ tool deployments over four years spanning Outreach, ZoomInfo, Spiff, Showpad, Nooks, LinkedIn Sales Navigator, and more. I own the full lifecycle: vendor selection, implementation, enablement, and governance."),
    ("AI-Powered RevOps Tooling",
     "I design and ship internal AI tools that actually get used. Recent work includes 5 production AI micro-apps (intent enrichment, custom data enrichment, one-pager generation, inbound SDR, competitor detection) using Claude and Gemini, deployed to a 150-person GTM org in 6 weeks."),
    ("CRM Strategy & Migration",
     "Owned complex Salesforce migrations through post-merger integrations, including cross-org data reconciliation, field schema design, and executive stakeholder communication. I build the tooling that makes these projects visible and de-risked."),
    ("Data & Reporting Infrastructure",
     "From BigQuery pipelines to executive dashboards, I build the operational infrastructure that gives leadership a real-time pulse on pipeline health and GTM execution."),
]:
    st.markdown(f"<p style='color:{DARK};font-size:0.92rem;line-height:1.7;'><strong>{title}</strong> — {body}</p>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ── Experience ────────────────────────────────────────────────────────────────
st.markdown(f"<h3 style='color:{DARK};font-weight:400;'>Experience</h3>", unsafe_allow_html=True)

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
    st.markdown(f"<p style='color:{DARK};margin-bottom:0.1rem;'><strong>{job['title']}</strong><br><span style='color:{TEAL_MID};font-size:0.85rem;'>{job['company']} · {job['dates']}</span></p>", unsafe_allow_html=True)
    if "desc" in job:
        st.markdown(f"<p style='font-size:0.82rem;color:{DARK};opacity:0.75;margin-top:0;'>{job['desc']}</p>", unsafe_allow_html=True)
    for bullet in job["bullets"]:
        st.markdown(f"<p style='font-size:0.88rem;color:{DARK};line-height:1.6;margin:0.2rem 0 0.2rem 1rem;'>— {bullet}</p>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)

# ── What I'm Looking For ──────────────────────────────────────────────────────
st.markdown(f"<h3 style='color:{DARK};font-weight:400;'>What I'm Looking For</h3>", unsafe_allow_html=True)
st.markdown(f"""
<p style='color:{DARK};font-size:0.92rem;line-height:1.7;'>
A senior RevOps or GTM Engineering role at a Series A–C SaaS company where I can:<br>
— Own the full GTM systems stack, not just administer it<br>
— Build AI-powered tooling that gives revenue teams a real edge<br>
— Work cross-functionally with Sales, Marketing, and Finance leadership<br>
— Have meaningful influence on how the company scales its go-to-market motion<br><br>
Remote-first or hybrid. Compensation commensurate with scope.
</p>
""", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
resume_path = Path("assets/resume.pdf")
if resume_path.exists():
    st.download_button(
        label="Download Resume (PDF)",
        data=resume_path.read_bytes(),
        file_name="Connor_Shirley_Resume.pdf",
        mime="application/pdf",
        type="primary",
    )
else:
    st.markdown(f"<p style='font-size:0.85rem;color:{TEAL_MID};'>Resume PDF not available — contact me directly.</p>", unsafe_allow_html=True)
