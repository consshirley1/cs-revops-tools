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
@import url('https://fonts.googleapis.com/css2?family=Material+Symbols+Rounded:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200&display=swap');

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
    display: flex; flex-direction: column; height: 100%;
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

/* ── Material icon fix ── */
span[data-testid="stIconMaterial"] {{
    font-family: 'Material Symbols Rounded' !important;
    font-variation-settings: 'FILL' 0, 'wght' 400, 'GRAD' 0, 'opsz' 24;
    font-size: 1.2rem; line-height: 1;
}}

/* ── Streamlit overrides ── */
.stTextInput > label, .stSelectbox > label, .stTextArea > label,
.stMultiselect > label {{ color: {DARK} !important; font-weight: 500; }}
.stAlert {{ border-radius: 6px; }}
</style>
"""


PROJECTS = [
    {
        "id": "la3",
        "name": "GTM Stack Unification",
        "context": "LumApps · Head of RevOps · 2024–2025",
        "tags": ["CRM Migration", "Tool Consolidation", "Post-Merger Integration"],
        "badge": "LumApps · 2024–2025",
        "badge_class": "badge-live",
        "desc": "Merged 15 tools into a single unified stack post-acquisition, including 2 CRMs and 2 MAPs — across a 150-person GTM org.",
        "metrics": ["15 tools → 1 unified stack", "2 CRMs merged", "2 MAPs consolidated", "150-person org enabled"],
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
    },
    {
        "id": "ai",
        "name": "AI Micro-App Suite",
        "context": "LumApps · Deputy VP RevOps · 2026",
        "tags": ["AI Deployment", "Claude", "Gemini", "GTM Engineering"],
        "badge": "AI-Powered · Claude + Gemini",
        "badge_class": "badge-ai",
        "desc": "5 production AI apps shipped in 6 weeks: intent enrichment, data enrichment, one-pager generation, inbound SDR, and competitor detection.",
        "metrics": ["5 apps in 6 weeks", "$200k tool spend identified", "150-person org", "Claude + Gemini APIs"],
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
    },
    {
        "id": "acquisition",
        "name": "Beekeeper Acquisition Integration",
        "context": "LumApps · GTM Sales Strategy Director · 2023–2024",
        "tags": ["M&A Integration", "CRM Migration", "Data Reconciliation", "Stakeholder Management"],
        "badge": "LumApps · 2023–2024",
        "badge_class": "badge-live",
        "desc": "Owned the RevOps integration track of a $40M ARR acquisition — data reconciliation, CRM consolidation, and unified pipeline reporting.",
        "metrics": ["400-person acquisition", "$40M ARR integrated", "Multiple ERP/CRM/MAP platforms", "Zero pipeline disruption"],
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
    },
    {
        "id": "meddpic",
        "name": "MEDDPIC Rollout & Forecast Transformation",
        "context": "LumApps · GTM Sales Strategy Director · 2022–2023",
        "tags": ["Sales Methodology", "Forecasting", "Salesforce", "Change Management"],
        "badge": "LumApps · 2022–2023",
        "badge_class": "badge-live",
        "desc": "Standardized MEDDPIC across an 80-person international org and rebuilt forecast infrastructure — improving accuracy by 60%+.",
        "metrics": [">60% forecast accuracy improvement", "80-person international org", "NORAM + EMEA + APAC", "Survived M&A intact"],
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
    },
    {
        "id": "noram",
        "name": "NORAM Team Build & PE Exit",
        "context": "LumApps · GTM Sales Strategy Director · 2022–2024",
        "tags": ["GTM Strategy", "Hiring", "Revenue Growth", "PE Exit"],
        "badge": "LumApps · 2022–2024",
        "badge_class": "badge-live",
        "desc": "Designed and built NORAM GTM from scratch — org structure, hiring, territories, quotas — contributing to the largest quarters in company history and a PE exit.",
        "metrics": ["Largest quarters in company history", "$2M+ from new AM function", "Full GTM team hired", "PE exit achieved"],
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
    },
    {
        "id": "brightmd",
        "name": "Bright.md — GTM Build from Zero",
        "context": "Bright.md · Manager, Sales Ops & Enablement · 2018–2020",
        "tags": ["Startup GTM", "CRM Implementation", "SDR", "Revenue Growth"],
        "badge": "Bright.md · 2018–2020",
        "badge_class": "badge-live",
        "desc": "Second GTM hire at a pre-revenue telehealth startup — built the entire RevOps stack from scratch and grew revenue from $0 to $10M.",
        "metrics": ["$0 → $10M revenue", "3x growth", "$7.86M personal pipeline", "131% of quota", "Team: 4 → 15"],
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
    },
]


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
