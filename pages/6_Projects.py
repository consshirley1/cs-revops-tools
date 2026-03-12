import streamlit as st

st.set_page_config(page_title="Projects — Connor Shirley", page_icon="🗂️", layout="wide")

# ── Project data (STAR format) ────────────────────────────────────────────────
projects = [
    {
        "id": "la3",
        "name": "LA3.0 — GTM Stack Unification",
        "context": "LumApps · Head of RevOps · 2024–2025",
        "tags": ["CRM Migration", "Tool Consolidation", "Post-Merger Integration"],
        "star": {
            "situation": (
                "Following LumApps' acquisition of Beekeeper, the combined organization was running "
                "two parallel GTM stacks — 2 CRMs, 2 MAPs, and 15 overlapping tools across Sales, "
                "Marketing, and CS. Duplicate data, conflicting processes, and split reporting were "
                "creating friction for a 150-person unified GTM org and obscuring executive visibility "
                "into pipeline health."
            ),
            "task": (
                "As Head of RevOps, I needed to architect and execute a full GTM stack unification "
                "within the fiscal year — without disrupting live pipeline or the day-to-day of a "
                "combined sales org still learning to operate together."
            ),
            "action": (
                "Led the end-to-end LA3.0 initiative: audited both tool stacks, mapped field schemas "
                "across the two CRMs, designed a migration sequencing plan that minimized pipeline risk, "
                "and negotiated vendor consolidations. Built org-wide enablement programs for each "
                "tool transition. Managed cross-functional stakeholders across Sales, Marketing, CS, "
                "IT, and Finance — and maintained an internal project tracker that surfaced risks "
                "to leadership in real time."
            ),
            "result": (
                "Successfully merged 15 tools (including 2 CRMs and 2 MAPs) into a single unified "
                "GTM stack. Eliminated redundant spend, improved data quality across the org, and gave "
                "leadership a single source of truth for pipeline and revenue reporting — which became "
                "a key input for PE reporting cadences."
            ),
        },
        "metrics": ["15 tools → 1 unified stack", "2 CRMs merged", "2 MAPs consolidated", "150-person org enabled"],
    },
    {
        "id": "ai",
        "name": "AI Micro-App Suite",
        "context": "LumApps · Deputy VP RevOps · 2026",
        "tags": ["AI Deployment", "Claude", "Gemini", "GTM Engineering"],
        "star": {
            "situation": (
                "LumApps' 150-person GTM org was spending significant time on manual research, "
                "repetitive data tasks, and unscalable sales prep — with no AI tooling in place. "
                "Leadership wanted to move fast on AI but lacked a concrete roadmap connecting "
                "intent to execution."
            ),
            "task": (
                "Develop and deploy a suite of production-ready AI tools that could meaningfully "
                "accelerate GTM execution — within a 6-week window, using existing infrastructure "
                "and without disrupting live sales motion."
            ),
            "action": (
                "Built 5 production AI micro-apps using Claude and Gemini APIs: an intent enrichment "
                "tool, a custom data enrichment pipeline, an AI one-pager generator for reps, an "
                "inbound SDR qualifier, and a competitor detection system. Designed the full AI "
                "roadmap connecting the agent layer, CRM data layer, and API mesh across the 11-tool "
                "GTM stack. Managed deployment, user onboarding, and feedback loops across the org."
            ),
            "result": (
                "All 5 apps shipped to the full GTM org in 6 weeks. The AI roadmap identified $200k "
                "in tool spend optimization opportunities. Reps gained structured intel on accounts "
                "in minutes instead of hours — directly improving outbound quality and inbound "
                "response speed."
            ),
        },
        "metrics": ["5 apps in 6 weeks", "$200k tool spend identified", "150-person org", "Claude + Gemini APIs"],
    },
    {
        "id": "acquisition",
        "name": "Beekeeper Acquisition Integration",
        "context": "LumApps · GTM Sales Strategy Director · 2023–2024",
        "tags": ["M&A Integration", "CRM Migration", "Data Reconciliation", "Stakeholder Management"],
        "star": {
            "situation": (
                "LumApps acquired Beekeeper — a 400-person, $40M ARR company — bringing with it "
                "separate ERP, CRM, and MAP platforms across multiple geographies and distinct "
                "sales motions (field enterprise vs. PLG). Post-close, both orgs were operating "
                "independently with no unified view of combined pipeline or revenue."
            ),
            "task": (
                "Own the RevOps integration track of the acquisition: ensure data continuity across "
                "systems, drive CRM and MAP consolidation, and give leadership a reliable view of "
                "the combined business throughout the integration process."
            ),
            "action": (
                "Led cross-org data reconciliation across CRM and ERP systems, designed unified "
                "field schemas that preserved both orgs' historical data, and built internal tooling "
                "to track integration progress and surface risks to the executive team. Coordinated "
                "with Finance, Legal, Sales, and IT across both companies. Managed communication "
                "to a combined sales org navigating significant organizational change."
            ),
            "result": (
                "Successfully integrated revenue operations systems across the combined organization. "
                "Pipeline data integrity was preserved throughout, enabling a clean unified view of "
                "the business for PE reporting. Integration was delivered without material disruption "
                "to the live sales cycle."
            ),
        },
        "metrics": ["400-person acquisition", "$40M ARR integrated", "Multiple ERP/CRM/MAP platforms", "Zero pipeline disruption"],
    },
    {
        "id": "meddpic",
        "name": "MEDDPIC Rollout & Forecast Transformation",
        "context": "LumApps · GTM Sales Strategy Director · 2022–2023",
        "tags": ["Sales Methodology", "Forecasting", "Salesforce", "Change Management"],
        "star": {
            "situation": (
                "LumApps' 80-person international sales org was running inconsistent qualification "
                "processes across regions and segments. Deal slippage was high, forecast accuracy "
                "was unreliable, and leadership lacked the pipeline visibility needed to make "
                "confident resource and capacity decisions."
            ),
            "task": (
                "Standardize the sales methodology and rebuild the forecasting infrastructure to "
                "give leadership reliable, rep-level pipeline visibility — across an international "
                "org with entrenched habits and multiple sales leaders."
            ),
            "action": (
                "Implemented MEDDPIC across the full sales org — including rep training, manager "
                "coaching, and CRM enforcement via custom Salesforce fields and validation rules. "
                "Redesigned the forecast cadence: built exec-ready pipeline dashboards, introduced "
                "weekly forecast calls with structured inspection criteria, and tied compensation "
                "hygiene to CRM data quality. Ran change management across NORAM, EMEA, and APAC."
            ),
            "result": (
                "Forecast accuracy improved by over 60%. Leadership gained reliable, consistent "
                "pipeline visibility that became a key input for the PE exit process. The org "
                "adopted MEDDPIC as its standard language for deal qualification — and it remained "
                "in place through the acquisition."
            ),
        },
        "metrics": [">60% forecast accuracy improvement", "80-person international org", "NORAM + EMEA + APAC", "Survived M&A intact"],
    },
    {
        "id": "noram",
        "name": "NORAM Team Build & PE Exit",
        "context": "LumApps · GTM Sales Strategy Director · 2022–2024",
        "tags": ["GTM Strategy", "Hiring", "Revenue Growth", "PE Exit"],
        "star": {
            "situation": (
                "LumApps needed a credible, scaling NORAM revenue motion to support its growth "
                "narrative heading into a PE fundraise. NORAM was underleveraged relative to the "
                "company's EU footprint, with limited headcount, no dedicated CS structure, and "
                "inconsistent pipeline coverage."
            ),
            "task": (
                "Design and build out the NORAM GTM team from the ground up — including org design, "
                "hiring, process infrastructure, and pipeline strategy — while maintaining the "
                "broader RevOps function across the global org."
            ),
            "action": (
                "Designed the NORAM GTM structure in collaboration with the CRO and VP Sales. Led "
                "hiring across AE, SDR, and CS functions. Built the supporting RevOps infrastructure "
                "(territories, quotas, compensation plans, CRM setup) and aligned the NORAM pipeline "
                "motion with the global revenue strategy. Established Account Management as a "
                "distinct function, with dedicated headcount and a structured expansion playbook."
            ),
            "result": (
                "NORAM team drove the largest quarters in company history. The Account Management "
                "function generated $2M+ in additional bookings in its first full fiscal year. "
                "The combined revenue performance was a direct contributor to a successful exit to PE."
            ),
        },
        "metrics": ["Largest quarters in company history", "$2M+ from new AM function", "Full GTM team hired", "PE exit achieved"],
    },
    {
        "id": "brightmd",
        "name": "Bright.md — GTM Build from Zero",
        "context": "Bright.md · Manager, Sales Ops & Enablement · 2018–2020",
        "tags": ["Startup GTM", "CRM Implementation", "SDR", "Revenue Growth"],
        "star": {
            "situation": (
                "Bright.md was a pre-revenue telehealth startup selling to enterprise healthcare "
                "systems, with a 4-person sales team and no formal GTM infrastructure. As the "
                "second GTM hire, there was no CRM, no MAP, no sales process, and no enablement "
                "function — only a product and a list of target accounts."
            ),
            "task": (
                "Build all GTM infrastructure from scratch — CRM, MAP, sales process, SDR program, "
                "and enablement — while also personally carrying pipeline responsibility as the "
                "company's first SDR hire."
            ),
            "action": (
                "Implemented the CRM and MAP from the ground up, built all RevOps processes and "
                "playbooks, designed the sales methodology, and created the enablement program for "
                "incoming reps. Simultaneously ran the SDR function personally in the early days — "
                "prospecting, sequencing, and qualifying enterprise healthcare accounts. Scaled the "
                "team from 4 to 15 as the infrastructure matured."
            ),
            "result": (
                "Grew company revenue from $0 to $10M, representing a 3x during my tenure. "
                "Generated $7.86M in personal pipeline at 131% of quota as the first SDR. "
                "Built the operational foundation that enabled the company to scale and attract "
                "follow-on investment."
            ),
        },
        "metrics": ["$0 → $10M revenue", "3x growth", "$7.86M personal pipeline", "131% of quota", "Team: 4 → 15"],
    },
]

# ── Page header ───────────────────────────────────────────────────────────────
st.markdown("# Strategic Projects")
st.markdown("**Key initiatives from my career — structured via STAR methodology.**")
st.divider()

# ── Tabs ──────────────────────────────────────────────────────────────────────
tab_labels = [p["name"] for p in projects]
tabs = st.tabs(tab_labels)

for tab, project in zip(tabs, projects):
    with tab:
        # Header row
        col_info, col_metrics = st.columns([3, 2])

        with col_info:
            st.markdown(f"### {project['name']}")
            st.caption(project["context"])
            tag_html = "".join(
                f'<span style="display:inline-block;background:#eff6ff;color:#1d4ed8;'
                f'font-size:0.72rem;padding:0.2rem 0.65rem;border-radius:3px;'
                f'margin:0.2rem 0.2rem 0.2rem 0;font-weight:500">{t}</span>'
                for t in project["tags"]
            )
            st.markdown(tag_html, unsafe_allow_html=True)

        with col_metrics:
            st.markdown("**Impact at a glance**")
            for m in project["metrics"]:
                st.markdown(f"✦ {m}")

        st.divider()

        # STAR breakdown
        s_col, t_col = st.columns(2)
        a_col, r_col = st.columns(2)

        with s_col:
            st.markdown("#### 🔍 Situation")
            st.markdown(project["star"]["situation"])

        with t_col:
            st.markdown("#### 🎯 Task")
            st.markdown(project["star"]["task"])

        with a_col:
            st.markdown("#### ⚙️ Action")
            st.markdown(project["star"]["action"])

        with r_col:
            st.markdown("#### 📈 Result")
            st.info(project["star"]["result"])
