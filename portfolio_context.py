"""Compiled portfolio context for the Ask Connor chatbot.

This module combines resume content with extracted page content from every
page in the Streamlit portfolio app.  It is auto-generated — edits here
will be overwritten on the next crawl.
"""

PORTFOLIO_CONTEXT = """
===============================================================================
RESUME — BASE LAYER
===============================================================================

Connor Shirley — RevOps Leader | Tech Stack Architecture and GTM Engineering

SUMMARY
Connor builds the systems that make revenue teams more efficient and profitable — from CRM
architecture and tool stack design to AI agents and custom micro-apps. Seven years scaling B2B
SaaS GTM from seed to PE exit, with hands-on ownership of forecasting, acquisition integrations,
and live AI deployment.

EXPERIENCE

LumApps (B2B SaaS — Digital Workplace / Intranet)
Deputy VP RevOps, Head of Strategy and Analytics | January 2026 – Present
- Developed company AI roadmap connecting agent layer, CRM data layer, and API mesh across
  11-tool GTM stack, identifying $200k in tool spend savings.
- Built 5 production AI micro-apps (intent enrichment, custom data enrichment, one-pager
  generation, inbound SDR, competitor detection) using Claude and Gemini APIs, deployed to
  a 150-person GTM org in 6 weeks. Increased outbound conversion rate by 15%.

GTM Sales Strategy Director | December 2021 – December 2025
- Led RevOps through $60M to $140M ARR company growth across the full revenue lifecycle.
- Implemented MEDDPIC methodology, rolled out 20+ GTM tools over 4 years.
- Designed and hired NORAM GTM teams that drove the largest quarters in company history,
  culminating in a PE exit.
- Established Account Management function that generated $2M+ in additional bookings.
- Led 400-person, $40M acquisition integration with multi-platform ERP/CRM/MAP consolidation
  — handled in-house, saving $250k+ in consulting fees, delivered on time.

Acquire.io | Sales Operations Manager | May–Dec 2021
- Built SDR outbound training that improved Stage 1 opportunity creation by 120% in two quarters.

Chili Piper | Sales Strategy and Enablement Manager | Nov 2020–May 2021
- TAM/ICP analysis unlocked ~$250k in incremental pipeline in two quarters.
- Rebuilt SDR curriculum, cutting new hire TTV by 4 days, increasing promoted SDR win rate 15%+.

Bright.md | Manager, Sales Operations and Enablement; SDR | Aug 2018–Nov 2020
- Second GTM hire. Scaled sales team from 4 to 15, helped 3x revenue from $0 to $10M ARR.
- Built all RevOps and Enablement functions from scratch.
- As first SDR hire, generated $7.86M in pipeline (131% of quota).

TECHNICAL SKILLS
CRM: Salesforce (Apex, LWC, SOQL, Flow), HubSpot
Sales Engagement: Outreach | MAP: HubSpot, Pardot/MCAE
Data: BigQuery, Python, SQL
AI/APIs: Anthropic Claude API, Google Gemini API, Google Agentspace
GTM Tools: ZoomInfo, Spiff, Showpad, Chili Piper, 15+ others
Dev: JavaScript, Google Apps Script, Python, Streamlit
Methodology: MEDDPIC, GTM stack architecture, acquisition integration,
revenue forecasting, AI agent deployment, SDR/AE enablement

EDUCATION
B.A., MENAS & Criminal Justice — University of Arizona, Tucson
MEDDPICC Academy for Managers
IBM — RAG & Agentic AI

CONTACT
Phone: (509) 496-7013
Email: consshirley@gmail.com
LinkedIn: https://www.linkedin.com/in/connor-shirley-93986954/
GitHub: https://github.com/consshirley1

===============================================================================
PORTFOLIO PAGE CONTENT — EXTRACTED FROM STREAMLIT APP
===============================================================================

--- HOME PAGE (app.py) ---
Title: Connor Shirley — RevOps Portfolio
Tagline: RevOps Leader · GTM Engineer · AI Deployment · CRM Architecture
Summary: I build the systems that make revenue teams more efficient and profitable — from CRM
architecture and tool stack design to AI agents and custom micro-apps. Seven years scaling
B2B SaaS from seed to PE exit. Browse the tools below or learn more about my background.
Key Stats: 7 Years in B2B SaaS GTM | 20+ GTM Tools Implemented | 5 Production Apps Shipped | $140M ARR RevOps Ownership
Featured Projects: GTM Stack Unification, AI Micro-App Suite, MEDDPIC & Forecast Rebuild
Tools & Demos: MX Lookup, Company Summarizer, INSEE Gap Detector, Lead Researcher,
White Space Mapper, Permission Auditor, SOQL Translator

--- ABOUT PAGE (1_About.py) ---
Title: About — Connor Shirley
Subtitle: RevOps Leader turned GTM Engineer · AI Deployment · CRM Architecture · $140M Scale
Bio: I build the systems that make revenue teams faster — from CRM architecture and tool stack
design to AI agents and custom micro-apps. Seven years scaling B2B SaaS GTM from seed to PE
exit, with hands-on ownership of forecasting, acquisition integrations, and live AI deployment.
I sit at the intersection of GTM and engineering, which means I can design it, build it, and
get buy-in on it.

What I Do:
- GTM Stack Architecture: Led simultaneous multi-tool rollouts across Sales, Marketing, and CS,
  including 20+ tool deployments over four years spanning Outreach, ZoomInfo, Spiff, Showpad,
  Nooks, LinkedIn Sales Navigator, and more. Full lifecycle: vendor selection, implementation,
  enablement, and governance.
- AI-Powered RevOps Tooling: Designs and ships internal AI tools that actually get used. Recent
  work includes 5 production AI micro-apps (intent enrichment, custom data enrichment, one-pager
  generation, inbound SDR, competitor detection) using Claude and Gemini, deployed to 150-person
  GTM org in 6 weeks.
- CRM Strategy & Migration: Owned complex Salesforce migrations through post-merger integrations,
  including cross-org data reconciliation, field schema design, and executive stakeholder
  communication.
- Data & Reporting Infrastructure: From BigQuery pipelines to executive dashboards, builds
  operational infrastructure that gives leadership real-time pulse on pipeline health and
  GTM execution.

Core Skills:
Tech & Tools: Salesforce, BigQuery, Google Apps Script, Python, Outreach, ZoomInfo, Spiff,
Showpad, Nooks, Syncari, Salesforce CPQ, Planhat, 6sense, Google Agentspace, Gemini API,
Claude / Anthropic
RevOps & Strategy: CRM Administration, GTM Architecture, CRM Migration, ICP/TAM Analysis,
AI Deployment, Project Management, Executive Reporting, Data Governance, Corporate Strategy
Methodologies: MEDDPIC, Challenger, JOLT, Command of the Message
Domain Expertise: Intranet / Digital Workplace SaaS, B2B Mid-Market & Enterprise (F500),
Post-merger GTM integration, French market (INSEE / SIREN), Seed to PE Exit journeys

What I'm Looking For: A senior RevOps or GTM Engineering role at a Series A–C SaaS company
where I can own the full GTM systems stack, build AI-powered tooling, work cross-functionally
with Sales, Marketing, and Finance leadership, and have meaningful influence on how the company
scales its go-to-market motion. Remote-first or hybrid.

--- RESUME PAGE (2_Resume.py) ---
Title: Resume — Connor Shirley
Purpose: Displays Connor's resume as an inline PDF viewer with download button.

--- MX LOOKUP TOOL (3_MX_Lookup.py) ---
Title: MX Lookup — Email Provider Identifier
Purpose: Enter any domain to identify its email provider via live DNS/MX record lookup.
How it works: Queries MX and TXT DNS records, matches against known provider patterns
(Google Workspace, Microsoft 365, Mimecast, Proofpoint, Barracuda, Mailgun, SendGrid,
Amazon SES, Zoho Mail, Proton Mail), displays provider card with CRM context, typical
segment, confidence scoring, email security checks (SPF, DMARC, redundant MX).
Technologies: Python, dnspython, Streamlit, live DNS resolution
Status: Live tool — no API key needed, no data stored or logged.

--- COMPANY SUMMARIZER (4_Company_Summarizer.py) ---
Title: Company Summarizer
Purpose: Enter a company name or domain and get an AI-generated RevOps-focused one-pager.
Output sections: Company Overview, Industry & Category, Company Size & Stage, Key Products /
Value Prop, Typical Buyer & ICP, GTM & Sales Notes, Tech Stack Signals, RevOps Relevance.
Focus modes: GTM & Sales Intel, General Overview, Competitive Landscape.
Technologies: Google Gemini 2.5 Flash API, Streamlit
Built for sales reps who need fast, structured intel.

--- INSEE GAP DETECTOR (5_INSEE_Gap_Detector.py) ---
Title: INSEE Gap Detector
Purpose: Salesforce account coverage analysis for the French market — identifying whitespace
by SIREN number. Cross-references the INSEE établissement registry with Salesforce account
records to find companies missing from CRM.
How it works (production): Pulls full INSEE registry from BigQuery, cross-references against
Salesforce account SIREN fields, applies fuzzy name matching with two-pass cleaning for
French public-sector entity names, surfaces net-new account import requests vs. SIREN
enrichment requests as separate export flows.
Technologies: BigQuery, Salesforce API, Python, Pandas, Streamlit
Status: Demo mode with mock data (30 French companies).
Metrics shown: Total companies, In Salesforce count, Missing (gaps), Coverage percentage.

--- PROJECTS PAGE (6_Projects.py) ---
Title: Strategic Projects
Purpose: Key initiatives structured via STAR methodology — Situation, Task, Action, Result.

Project 1: GTM Stack Unification (LumApps · 2024–2025)
Tags: CRM Migration, Tool Consolidation, Post-Merger Integration
Metrics: 15 tools → 1 unified stack, 2 CRMs merged, 2 MAPs consolidated, 150-person org enabled
Situation: Following LumApps' acquisition of Beekeeper, the combined organization was running
two parallel GTM stacks — 2 CRMs, 2 MAPs, and 15 overlapping tools across Sales, Marketing,
and CS.
Task: Architect and execute a full GTM stack unification within the fiscal year without
disrupting live pipeline.
Action: Led the end-to-end LA3.0 initiative: audited both tool stacks, mapped field schemas
across two CRMs, designed migration sequencing plan, negotiated vendor consolidations, built
org-wide enablement programs, managed cross-functional stakeholders.
Result: Successfully merged 15 tools into a single unified GTM stack. Eliminated redundant
spend, improved data quality, gave leadership a single source of truth for pipeline and
revenue reporting — key input for PE reporting cadences.

Project 2: AI Micro-App Suite (LumApps · 2026)
Tags: AI Deployment, Claude, Gemini, GTM Engineering
Metrics: 5 apps in 6 weeks, $200k tool spend identified, 150-person org, Claude + Gemini APIs
Situation: LumApps' 150-person GTM org had no AI tooling in place.
Task: Develop and deploy production-ready AI tools within a 6-week window.
Action: Built 5 production AI micro-apps using Claude and Gemini APIs: intent enrichment,
custom data enrichment, AI one-pager generator, inbound SDR qualifier, competitor detection.
Designed AI roadmap connecting agent layer, CRM data layer, and API mesh across 11-tool
GTM stack.
Result: All 5 apps shipped to full GTM org in 6 weeks. AI roadmap identified $200k in tool
spend optimization. Reps gained structured intel in minutes instead of hours.

Project 3: Beekeeper Acquisition Integration (LumApps · 2023–2024)
Tags: M&A Integration, CRM Migration, Data Reconciliation, Stakeholder Management
Metrics: 400-person acquisition, $40M ARR integrated, Multiple ERP/CRM/MAP platforms,
Zero pipeline disruption
Situation: LumApps acquired Beekeeper — a 400-person, $40M ARR company — with separate ERP,
CRM, and MAP platforms.
Task: Own the RevOps integration track: data continuity, CRM/MAP consolidation, reliable
combined business view.
Action: Led cross-org data reconciliation, designed unified field schemas, built internal
tooling to track integration progress, coordinated with Finance, Legal, Sales, and IT.
Result: Successfully integrated revenue operations systems. Pipeline data integrity preserved
throughout. Integration delivered without material disruption to live sales cycle.

Project 4: MEDDPIC Rollout & Forecast Transformation (LumApps · 2022–2023)
Tags: Sales Methodology, Forecasting, Salesforce, Change Management
Metrics: >60% forecast accuracy improvement, 80-person international org, NORAM + EMEA + APAC,
Survived M&A intact
Situation: 80-person international sales org running inconsistent qualification processes.
Task: Standardize sales methodology and rebuild forecasting infrastructure.
Action: Implemented MEDDPIC across full sales org, redesigned forecast cadence, built exec-ready
dashboards, introduced weekly forecast calls, tied compensation hygiene to CRM data quality.
Result: Forecast accuracy improved by over 60%. Org adopted MEDDPIC as standard language.
Remained in place through the acquisition.

Project 5: NORAM Team Build & PE Exit (LumApps · 2022–2024)
Tags: GTM Strategy, Hiring, Revenue Growth, PE Exit
Metrics: Largest quarters in company history, $2M+ from new AM function, Full GTM team hired,
PE exit achieved
Situation: NORAM underleveraged relative to EU footprint with limited headcount.
Task: Design and build out NORAM GTM team from the ground up.
Action: Designed NORAM GTM structure, led hiring across AE, SDR, and CS functions, built
RevOps infrastructure, established Account Management as distinct function.
Result: NORAM team drove largest quarters in company history. AM function generated $2M+
in additional bookings. Direct contributor to successful PE exit.

Project 6: Bright.md — GTM Build from Zero (2018–2020)
Tags: Startup GTM, CRM Implementation, SDR, Revenue Growth
Metrics: $0 → $10M revenue, 3x growth, $7.86M personal pipeline, 131% of quota, Team: 4 → 15
Situation: Pre-revenue telehealth startup with 4-person sales team, no formal GTM infrastructure.
Task: Build all GTM infrastructure from scratch while carrying pipeline responsibility as
first SDR.
Action: Implemented CRM and MAP from ground up, built all RevOps processes and playbooks,
ran SDR function personally, scaled team from 4 to 15.
Result: Grew company revenue from $0 to $10M (3x). Generated $7.86M in personal pipeline
at 131% of quota.

--- LEAD RESEARCHER (7_Lead_Researcher.py) ---
Title: Lead Researcher — AI Brief Generator
Purpose: Paste a LinkedIn bio or company About Us text to get a RevOps-ready executive brief.
Output: 3-Sentence Summary, Potential Pain Points (3-5 specific revenue team pain points),
Suggested Outreach Hook (personalized non-generic opener).
Context types: Individual (LinkedIn bio), Company (About Us), Mixed.
Technologies: Google Gemini 2.5 Flash API, Streamlit

--- WHITE SPACE MAPPER (8_SFDC_Account_Mapper.py) ---
Title: White Space Mapper
Purpose: Simulates a Salesforce white space analysis — identifying cross-sell gaps in account
base by product penetration and industry.
How it works: Rule-based recommendation engine that suggests next best action based on
product penetration (CRM → Analytics → AI Suite). Filters by industry and recommended play.
Outputs coverage metrics, color-coded penetration grid, and strategic insights.
RevOps Tip: In Salesforce, automate using Summary Formula on custom report or Flow that
updates a Next Best Action field on Account object. Combine with territory rules.
Technologies: Pandas, Streamlit
Status: Demo mode with mock Salesforce data.

--- PERMISSION AUDITOR (9_SFDC_Perm.py) ---
Title: Permission Set Auditor
Purpose: RevOps governance tool that identifies permission creep by auditing Salesforce user
rights against a defined security baseline.
How it works: Compares user permissions against a baseline policy. Flags violations where
permissions are assigned but not in baseline as "High Risk". Recommends Least Privilege
Model using Permission Set Groups and Muting Permission Sets.
Technologies: Pandas, Streamlit
Status: Demo mode with mock permission data. Production connects via Salesforce Metadata API
or Tooling API.

--- SOQL TRANSLATOR (10_SOQL_to_Human.py) ---
Title: SOQL Translator
Purpose: Converts plain English to Salesforce SOQL and helps non-technical stakeholders
understand the queries running their business.
Tab 1 — AI: Natural language to SOQL using Gemini. Includes example queries.
Tab 2 — Manual Query Builder: Visual SOQL builder supporting Account, Contact, Opportunity,
Lead, Task, Event objects with field selection, WHERE filters, ORDER BY, and LIMIT.
Technologies: Google Gemini 2.5 Flash API, Streamlit
Insight: Technical debt often grows because stakeholders don't understand the queries
running their business. This tool bridges that gap.

===============================================================================
PORTFOLIO APP TECHNOLOGIES & ARCHITECTURE
===============================================================================
Framework: Streamlit (Python)
AI Models: Anthropic Claude API, Google Gemini 2.5 Flash API
Data: BigQuery, Pandas, Salesforce (SOQL, Metadata API, Tooling API)
DNS: dnspython for live MX/TXT resolution
Deployment: Streamlit Community Cloud with GitHub Actions keep-alive
Design: Inter font family, teal color palette, card-based UI, Mermaid diagrams
Architecture: Multi-page app with shared CSS/config module, session state management
"""
