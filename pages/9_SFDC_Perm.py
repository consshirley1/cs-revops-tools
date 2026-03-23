import streamlit as st
import pandas as pd
from shared import COMMON_CSS, DARK, TEAL_DARK, TEAL_MID, TEAL_LIGHT, mermaid_chart
from sidebar import render_sidebar

st.set_page_config(page_title="SFDC Permission Auditor", page_icon="🔐", layout="wide")
render_sidebar()
st.markdown(COMMON_CSS, unsafe_allow_html=True)

st.markdown(f"""
<style>
    .demo-banner {{
        background: {TEAL_LIGHT}; border: 1px solid {TEAL_MID}55;
        border-radius: 6px; padding: 0.75rem 1rem;
        font-size: 0.85rem; color: {DARK}; margin-bottom: 1.5rem;
    }}
    .risk-card {{
        border-radius: 8px; padding: 1rem 1.25rem;
        border-left: 4px solid;
    }}
    .risk-high   {{ border-color: #ef4444; background: #fef2f2; }}
    .risk-ok     {{ border-color: {TEAL_DARK}; background: {TEAL_LIGHT}; }}
    .risk-none   {{ border-color: #d1d5db; background: #f9fafb; }}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="page-title">Permission Set <span>Auditor</span></div>', unsafe_allow_html=True)
st.markdown(f"<p style='color:{DARK};'>RevOps governance tool that identifies permission creep by auditing Salesforce user rights against a defined security baseline.</p>", unsafe_allow_html=True)

st.markdown(f"""
<div class="demo-banner">
    <strong>Demo Mode</strong> — Uses mock permission data. The production version connects to the
    Salesforce Metadata API to pull live ObjectPermissions and SetupEntityAccess records.
</div>
""", unsafe_allow_html=True)

# ── Mock data ──────────────────────────────────────────────────────────────────
baseline_permissions = {
    "Export Reports":    False,
    "Modify All Data":   False,
    "View Setup":        True,
    "Edit Opportunities": True,
    "Delete Accounts":   False,
    "Manage Users":      False,
    "View All Data":     False,
    "Run Reports":       True,
}

# Simulated multi-user data
users = {
    "Alex Sales-Rep": {
        "Export Reports": True, "Modify All Data": False, "View Setup": True,
        "Edit Opportunities": True, "Delete Accounts": True,
        "Manage Users": False, "View All Data": False, "Run Reports": True,
    },
    "Maria Manager": {
        "Export Reports": True, "Modify All Data": False, "View Setup": True,
        "Edit Opportunities": True, "Delete Accounts": False,
        "Manage Users": True, "View All Data": True, "Run Reports": True,
    },
    "Dev Admin": {
        "Export Reports": True, "Modify All Data": True, "View Setup": True,
        "Edit Opportunities": True, "Delete Accounts": True,
        "Manage Users": True, "View All Data": True, "Run Reports": True,
    },
}


def audit_user(permissions: dict) -> pd.DataFrame:
    rows = []
    for perm, assigned in permissions.items():
        baseline_allowed = baseline_permissions.get(perm, False)
        if assigned and not baseline_allowed:
            status = "High Risk (Violation)"
        elif assigned and baseline_allowed:
            status = "Approved"
        elif not assigned:
            status = "Not Assigned"
        else:
            status = "Not Assigned"
        rows.append({"Permission": perm, "Assigned": assigned, "Baseline": baseline_allowed, "Audit Status": status})
    return pd.DataFrame(rows)


def color_status(val):
    if "High Risk" in str(val):
        return "background-color: #fee2e2; color: #b91c1c; font-weight: 600;"
    if "Approved" in str(val):
        return f"background-color: {TEAL_LIGHT}; color: {TEAL_DARK}; font-weight: 600;"
    return "color: #9ca3af;"


# ── User selector ─────────────────────────────────────────────────────────────
st.markdown('<div class="section-label">Select User to Audit</div>', unsafe_allow_html=True)
selected_user = st.selectbox("User", list(users.keys()), label_visibility="collapsed")

audit_df = audit_user(users[selected_user])

# ── Risk summary ──────────────────────────────────────────────────────────────
violations = audit_df[audit_df["Audit Status"].str.contains("High Risk")]
approved = audit_df[audit_df["Audit Status"].str.contains("Approved")]

m1, m2, m3 = st.columns(3)
with m1:
    st.metric("Total Permissions", len(audit_df))
with m2:
    st.metric("✅ Approved", len(approved))
with m3:
    label = "🚨 Violations" if len(violations) > 0 else "Violations"
    st.metric(label, len(violations))

if len(violations) > 0:
    st.error(f"**{len(violations)} security violation{'s' if len(violations) > 1 else ''}** detected for **{selected_user}**. Review the table below.")

# ── Permission table ──────────────────────────────────────────────────────────
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(f'<div class="section-label">Permission Audit — {selected_user}</div>', unsafe_allow_html=True)

display_df = audit_df[["Permission", "Assigned", "Baseline", "Audit Status"]].copy()
styled = display_df.style.applymap(color_status, subset=["Audit Status"])
st.table(styled)

# ── Analysis ──────────────────────────────────────────────────────────────────
if len(violations) > 0:
    st.markdown("<hr>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)

    with col1:
        violation_list = "\n".join(f"- **{row['Permission']}** — Exceeds baseline" for _, row in violations.iterrows())
        st.error(f"### 🚨 Security Risks Detected\n{violation_list}\n\n**Risk:** Potential data exfiltration or unauthorized modification.\n**Action:** Move to a scoped Permission Set Group.")

    with col2:
        st.markdown(f"""
        <div style="background:{TEAL_LIGHT}; border:1px solid {TEAL_MID}55; border-radius:8px; padding:1rem 1.25rem;">
            <div style="font-size:0.62rem;font-weight:600;letter-spacing:0.15em;text-transform:uppercase;color:{TEAL_MID};margin-bottom:0.5rem;">Least Privilege Model</div>
            <p style="font-size:0.85rem;color:{DARK};line-height:1.6;">
            Design permissions using <strong>Permission Set Groups</strong> and <strong>Muting Permission Sets</strong>
            to ensure users only have access required for their specific job function.
            Use <strong>Named Credential + Connected App</strong> scoping for integration users.
            </p>
        </div>
        """, unsafe_allow_html=True)
else:
    st.success(f"No violations detected for **{selected_user}**. All permissions are within the defined baseline.")

# ── How it works ─────────────────────────────────────────────────────────────
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<div class="section-label">How It Works</div>', unsafe_allow_html=True)

mermaid_chart("""
flowchart LR
    A[(Salesforce\\nMetadata API\\nPermission Sets)] --> B[Audit Engine\\nBaseline Comparison]
    C[(Security Baseline\\nIT / Security Policy)] --> B
    B --> D{Violation Check}
    D -->|Assigned AND not in baseline| E[High Risk Flag]
    D -->|Assigned AND in baseline| F[Approved]
    D -->|Not Assigned| G[Not Assigned]
    E & F & G --> H[Permission Table\\nRAG Status]
    H --> I([Remediation\\nLeast Privilege Model])
""", height=260)

st.markdown("<hr>", unsafe_allow_html=True)
st.caption("Built to simulate Salesforce ObjectPermissions and SetupEntityAccess metadata checks. Production connects via Metadata API or Tooling API.")
