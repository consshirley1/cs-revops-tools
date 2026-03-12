import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="INSEE Gap Detector", page_icon="🇫🇷", layout="wide")

st.markdown("""
<style>
    .page-title { font-size: 2rem; font-weight: 300; margin-bottom: 0.25rem; }
    .page-title span { color: #1d4ed8; }
    hr { border: none; border-top: 1px solid #e5e7eb; margin: 1.5rem 0; }
    .section-label {
        font-size: 0.65rem; font-weight: 500; letter-spacing: 0.15em;
        text-transform: uppercase; color: #9ca3af; margin-bottom: 0.5rem;
    }
    .demo-banner {
        background: #fffbeb; border: 1px solid #fcd34d;
        border-radius: 6px; padding: 0.75rem 1rem;
        font-size: 0.85rem; color: #92400e; margin-bottom: 1.5rem;
    }
    .metric-card {
        border: 1px solid #e5e7eb; border-radius: 6px;
        padding: 1rem 1.25rem; text-align: center;
    }
    .metric-num { font-size: 1.75rem; font-weight: 300; color: #111827; }
    .metric-label { font-size: 0.75rem; color: #9ca3af; margin-top: 0.1rem; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="page-title">🇫🇷 INSEE <span>Gap Detector</span></div>', unsafe_allow_html=True)
st.markdown("Salesforce account coverage analysis for the French market — identifying whitespace by SIREN number.")

st.markdown("""
<div class="demo-banner">
    ⚠️ <strong>Demo Mode</strong> — This tool uses mock data to illustrate the concept.
    The production version queries a BigQuery dataset backed by the full INSEE établissement registry
    and cross-references live Salesforce account records.
</div>
""", unsafe_allow_html=True)

# --- Mock data ---
@st.cache_data
def get_mock_data():
    random.seed(42)
    companies = [
        ("Société Générale", "75009", "Paris", "Finance / Banking", 145000),
        ("BNP Paribas", "75009", "Paris", "Finance / Banking", 189000),
        ("Crédit Agricole", "92120", "Montrouge", "Finance / Banking", 138000),
        ("Capgemini France", "75009", "Paris", "IT Services", 55000),
        ("Atos SE", "75008", "Paris", "IT Services", 47000),
        ("Sopra Steria", "75014", "Paris", "IT Services", 21000),
        ("Dassault Systèmes", "78140", "Vélizy-Villacoublay", "Software", 20000),
        ("OVHcloud", "59100", "Roubaix", "Cloud Infrastructure", 2400),
        ("Doctolib", "75010", "Paris", "HealthTech", 2800),
        ("Contentsquare", "75009", "Paris", "Analytics SaaS", 1500),
        ("Mirakl", "75002", "Paris", "E-commerce SaaS", 900),
        ("Payfit", "75009", "Paris", "HR SaaS", 700),
        ("Pennylane", "75009", "Paris", "FinTech SaaS", 450),
        ("Spendesk", "75009", "Paris", "FinTech SaaS", 500),
        ("Qonto", "75009", "Paris", "FinTech SaaS", 1400),
        ("Alan", "75009", "Paris", "InsurTech", 500),
        ("Ledger", "75009", "Paris", "Crypto / Web3", 900),
        ("ManoMano", "75009", "Paris", "E-commerce", 700),
        ("Vestiaire Collective", "75009", "Paris", "E-commerce", 900),
        ("BackMarket", "75011", "Paris", "E-commerce", 650),
        ("Groupe La Poste", "75015", "Paris", "Postal / Logistics", 180000),
        ("SNCF", "93210", "Saint-Denis", "Transport", 150000),
        ("Air France", "95701", "Roissy", "Aviation", 41000),
        ("Michelin", "63040", "Clermont-Ferrand", "Manufacturing", 130000),
        ("L'Oréal", "92117", "Clichy", "Consumer Goods", 87000),
        ("LVMH", "75008", "Paris", "Luxury Goods", 175000),
        ("Carrefour", "91300", "Massy", "Retail", 100000),
        ("Decathlon", "59650", "Villeneuve-d'Ascq", "Retail", 93000),
        ("Renault", "92100", "Boulogne-Billancourt", "Automotive", 111000),
        ("Stellantis France", "75116", "Paris", "Automotive", 28000),
    ]

    rows = []
    for i, (name, postal, city, industry, employees) in enumerate(companies):
        siren = f"{random.randint(100000000, 999999999)}"
        in_sf = random.random() > 0.4
        stage = random.choice(["Prospect", "MQL", "SQL", "Customer", "Churned"]) if in_sf else None
        owner = random.choice(["Marie D.", "Thomas B.", "Sophie L.", "Pierre M.", ""]) if in_sf else None
        rows.append({
            "Company": name,
            "SIREN": siren,
            "Postal Code": postal,
            "City": city,
            "Industry": industry,
            "Employees": employees,
            "In Salesforce": in_sf,
            "SF Stage": stage or "—",
            "SF Owner": owner or "—",
        })
    return pd.DataFrame(rows)

df = get_mock_data()

# --- Filters ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<div class="section-label">Filters</div>', unsafe_allow_html=True)

f1, f2, f3 = st.columns(3)
with f1:
    search = st.text_input("Search company name or SIREN", placeholder="e.g. Capgemini or 123456789")
with f2:
    industries = ["All"] + sorted(df["Industry"].unique().tolist())
    industry_filter = st.selectbox("Industry", industries)
with f3:
    sf_filter = st.selectbox("Salesforce Status", ["All", "In Salesforce ✅", "Missing from Salesforce ⚠️"])

# Apply filters
filtered = df.copy()
if search:
    filtered = filtered[
        filtered["Company"].str.contains(search, case=False) |
        filtered["SIREN"].str.contains(search, case=False)
    ]
if industry_filter != "All":
    filtered = filtered[filtered["Industry"] == industry_filter]
if sf_filter == "In Salesforce ✅":
    filtered = filtered[filtered["In Salesforce"] == True]
elif sf_filter == "Missing from Salesforce ⚠️":
    filtered = filtered[filtered["In Salesforce"] == False]

# --- Metrics ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<div class="section-label">Coverage Summary</div>', unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
total = len(filtered)
in_sf = filtered["In Salesforce"].sum()
missing = total - in_sf
coverage_pct = round((in_sf / total * 100), 1) if total > 0 else 0

with m1:
    st.markdown(f'<div class="metric-card"><div class="metric-num">{total}</div><div class="metric-label">Companies in View</div></div>', unsafe_allow_html=True)
with m2:
    st.markdown(f'<div class="metric-card"><div class="metric-num" style="color:#10b981">{in_sf}</div><div class="metric-label">In Salesforce</div></div>', unsafe_allow_html=True)
with m3:
    st.markdown(f'<div class="metric-card"><div class="metric-num" style="color:#ef4444">{missing}</div><div class="metric-label">Missing from SF</div></div>', unsafe_allow_html=True)
with m4:
    st.markdown(f'<div class="metric-card"><div class="metric-num">{coverage_pct}%</div><div class="metric-label">Coverage Rate</div></div>', unsafe_allow_html=True)

# --- Table ---
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<div class="section-label">Account Records</div>', unsafe_allow_html=True)

display_df = filtered.copy()
display_df["Status"] = display_df["In Salesforce"].apply(lambda x: "✅ In Salesforce" if x else "⚠️ Gap Detected")
display_df = display_df.drop(columns=["In Salesforce"])
cols = ["Status", "Company", "SIREN", "City", "Industry", "Employees", "SF Stage", "SF Owner"]
display_df = display_df[cols]

st.dataframe(
    display_df,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Employees": st.column_config.NumberColumn(format="%d"),
        "Status": st.column_config.TextColumn(width="medium"),
        "Company": st.column_config.TextColumn(width="large"),
    }
)

# --- Export ---
st.markdown("<hr>", unsafe_allow_html=True)
gaps_only = filtered[filtered["In Salesforce"] == False][["Company", "SIREN", "City", "Industry", "Employees"]]

if len(gaps_only) > 0:
    st.download_button(
        f"⬇️ Export {len(gaps_only)} Gap{'s' if len(gaps_only) != 1 else ''} to CSV",
        data=gaps_only.to_csv(index=False),
        file_name="insee_sf_gaps.csv",
        mime="text/csv",
    )
else:
    st.info("No gaps in current filtered view.")

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
**How the production version works:**
1. Pulls the full INSEE établissement registry from BigQuery (`insee-enrichment` project)
2. Cross-references against Salesforce account SIREN fields via a custom cross-org lookup
3. Applies fuzzy name matching with a two-pass cleaning system for French public-sector entity names
4. Surfaces net-new account import requests vs. SIREN enrichment requests as separate export flows
""")
st.caption("Demo data is randomly generated for illustrative purposes. SIREN numbers are synthetic.")
