import streamlit as st
import pandas as pd
from shared import COMMON_CSS, DARK, TEAL_DARK, TEAL_MID, TEAL_LIGHT, mermaid_chart

st.set_page_config(page_title="SFDC White Space Mapper", page_icon="📈", layout="wide")
st.markdown(COMMON_CSS, unsafe_allow_html=True)

st.markdown(f"""
<style>
    .demo-banner {{
        background: {TEAL_LIGHT}; border: 1px solid {TEAL_MID}55;
        border-radius: 6px; padding: 0.75rem 1rem;
        font-size: 0.85rem; color: {DARK}; margin-bottom: 1.5rem;
    }}
    .insight-card {{
        border: 1px solid {TEAL_LIGHT}; border-radius: 8px;
        padding: 1rem 1.25rem; background: #ffffff;
    }}
    .metric-num {{ font-size: 1.75rem; font-weight: 300; color: {TEAL_DARK}; }}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="page-title">📈 White Space <span>Mapper</span></div>', unsafe_allow_html=True)
st.markdown(f"<p style='color:{DARK};'>Simulates a Salesforce white space analysis — identifying cross-sell gaps in your account base by product penetration and industry.</p>", unsafe_allow_html=True)

st.markdown(f"""
<div class="demo-banner">
    ℹ️ <strong>Demo Mode</strong> — Uses mock Salesforce account data to illustrate the concept.
    In production, this pulls live from a Salesforce report export or SOQL query.
</div>
""", unsafe_allow_html=True)

# ── Mock data ──────────────────────────────────────────────────────────────────
data = {
    "Account Name": ["Acme Corp", "Globex", "Soylent Corp", "Initech", "Umbrella Co", "Hooli", "Wonka Industries", "Dunder Mifflin"],
    "Industry":     ["Manufacturing", "Tech", "Manufacturing", "Tech", "Healthcare", "Tech", "Manufacturing", "Retail"],
    "Product A — CRM":       [True, True, True, False, True, True, True, False],
    "Product B — Analytics": [False, True, False, False, True, True, False, False],
    "Product C — AI Suite":  [False, False, False, False, False, True, False, False],
}
df = pd.DataFrame(data)


def suggest_next_step(row):
    if not row["Product A — CRM"]:
        return "🎯 Target for Core CRM"
    if row["Product A — CRM"] and not row["Product B — Analytics"]:
        return "📊 Suggest Analytics (CRM user)"
    if row["Product B — Analytics"] and not row["Product C — AI Suite"]:
        return "🤖 Suggest AI Suite (High maturity)"
    return "✅ Fully Penetrated"


df["Recommended Play"] = df.apply(suggest_next_step, axis=1)

# ── Filters ───────────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Filters</div>', unsafe_allow_html=True)
f1, f2 = st.columns(2)
with f1:
    industries = ["All"] + sorted(df["Industry"].unique().tolist())
    industry_filter = st.selectbox("Industry", industries)
with f2:
    play_filter = st.selectbox(
        "Filter by Play",
        ["All"] + df["Recommended Play"].unique().tolist(),
    )

filtered = df.copy()
if industry_filter != "All":
    filtered = filtered[filtered["Industry"] == industry_filter]
if play_filter != "All":
    filtered = filtered[filtered["Recommended Play"] == play_filter]

# ── Coverage summary ──────────────────────────────────────────────────────────
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<div class="section-label">Coverage Summary</div>', unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)
with m1:
    n = len(filtered)
    st.metric("Accounts in View", n)
with m2:
    crm_pct = round(filtered["Product A — CRM"].sum() / n * 100) if n else 0
    st.metric("CRM Penetration", f"{crm_pct}%")
with m3:
    analytics_pct = round(filtered["Product B — Analytics"].sum() / n * 100) if n else 0
    st.metric("Analytics Penetration", f"{analytics_pct}%")
with m4:
    ai_pct = round(filtered["Product C — AI Suite"].sum() / n * 100) if n else 0
    st.metric("AI Suite Penetration", f"{ai_pct}%")

# ── Account grid ──────────────────────────────────────────────────────────────
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<div class="section-label">Account Penetration Grid</div>', unsafe_allow_html=True)


def highlight_bool(val):
    if val is True:
        return f"background-color: {TEAL_LIGHT}; color: {TEAL_DARK}; font-weight: 600;"
    if val is False:
        return "background-color: #fee2e2; color: #b91c1c;"
    return ""


styled_df = filtered.style.applymap(
    highlight_bool,
    subset=["Product A — CRM", "Product B — Analytics", "Product C — AI Suite"],
)
st.dataframe(styled_df, use_container_width=True, hide_index=True)

# ── Strategic insights ────────────────────────────────────────────────────────
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<div class="section-label">Strategic Insights — Top Cross-Sell Opportunities</div>', unsafe_allow_html=True)

plays = {
    "📊 Suggest Analytics (CRM user)": "Ready for Analytics upsell (have CRM, missing Analytics)",
    "🤖 Suggest AI Suite (High maturity)": "High-maturity accounts ready for AI expansion",
    "🎯 Target for Core CRM": "Unactivated accounts — start with CRM",
}

cols = st.columns(len(plays))
for col, (play, description) in zip(cols, plays.items()):
    targets = filtered[filtered["Recommended Play"] == play]
    with col:
        st.markdown(f"""
        <div class="insight-card">
            <div class="section-label">{play}</div>
            <div class="metric-num">{len(targets)}</div>
            <div style="font-size:0.78rem;color:{DARK};margin-top:0.3rem;">{description}</div>
        </div>
        """, unsafe_allow_html=True)
        if len(targets) > 0:
            st.dataframe(targets[["Account Name", "Industry"]], hide_index=True, use_container_width=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.info(f"💡 **RevOps Tip:** In Salesforce, automate this using a Summary Formula on a custom report or a Flow that updates a 'Next Best Action' field on the Account object. Combine with territory rules for automatic rep assignment.")

# ── How it works ─────────────────────────────────────────────────────────────
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<div class="section-label">How It Works</div>', unsafe_allow_html=True)

mermaid_chart("""
flowchart LR
    A[(Salesforce\\nAccount Export\\nor SOQL Report)] --> B[Pandas DataFrame\\nProduct Penetration Grid]
    B --> C{Rule Engine\\nPriority-ordered}
    C -->|Has CRM, no Analytics| D[📊 Suggest Analytics]
    C -->|Has Analytics, no AI| E[🤖 Suggest AI Suite]
    C -->|No CRM| F[🎯 Target for CRM]
    C -->|All products| G[✅ Fully Penetrated]
    D & E & F & G --> H([Color-coded Grid\\n+ Strategic Insights])
""", height=260)

st.markdown("<hr>", unsafe_allow_html=True)
st.caption("Demo data is illustrative. In production, connect directly to a Salesforce report via the REST API or a scheduled SOQL export.")
