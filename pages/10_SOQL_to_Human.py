import streamlit as st
import google.generativeai as genai
from shared import COMMON_CSS, DARK, TEAL_DARK, TEAL_MID, TEAL_LIGHT, mermaid_chart

st.set_page_config(page_title="SOQL Translator", page_icon="🔍", layout="wide")
st.markdown(COMMON_CSS, unsafe_allow_html=True)

st.markdown(f"""
<style>
    .key-help {{
        background: {TEAL_LIGHT}; border: 1px solid {TEAL_MID}55; border-radius: 6px;
        padding: 0.85rem 1rem; font-size: 0.82rem; color: {DARK}; margin-top: 0.5rem;
    }}
    .key-help a {{ color: {TEAL_DARK}; text-decoration: none; }}
    .logic-map {{
        background: {TEAL_LIGHT}; border-radius: 8px; padding: 1rem 1.25rem;
        font-size: 0.85rem; color: {DARK}; line-height: 1.65;
    }}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="page-title">SOQL <span>Translator</span></div>', unsafe_allow_html=True)
st.markdown(f"<p style='color:{DARK};'>Converts plain English to Salesforce SOQL — and helps non-technical stakeholders understand the queries running their business.</p>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# ── API Key ───────────────────────────────────────────────────────────────────
GEMINI_MODEL = "gemini-1.5-flash"

if "gemini_api_key" not in st.session_state:
    st.session_state.gemini_api_key = None

api_key = None
try:
    api_key = st.secrets["GEMINI_API_KEY"]
except Exception:
    pass

if not api_key:
    api_key = st.session_state.gemini_api_key

if not api_key:
    st.markdown('<div class="section-label">API Key Required (for AI Tab)</div>', unsafe_allow_html=True)
    key_input = st.text_input("Google Gemini API Key", type="password", placeholder="AIza...")
    st.markdown(f"""
    <div class="key-help">
        Free key at <a href="https://aistudio.google.com/app/apikey" target="_blank">aistudio.google.com</a>.
        The Manual Builder tab works without a key.
    </div>
    """, unsafe_allow_html=True)
    if key_input:
        st.session_state.gemini_api_key = key_input
        api_key = key_input
        st.rerun()
else:
    col_key, col_clear = st.columns([6, 1])
    with col_key:
        st.success(f"✅ API key loaded · Model: `{GEMINI_MODEL}`")
    with col_clear:
        if st.button("Clear key", use_container_width=True):
            st.session_state.gemini_api_key = None
            st.rerun()

st.markdown("<hr>", unsafe_allow_html=True)

# ── Tabs ──────────────────────────────────────────────────────────────────────
tab1, tab2 = st.tabs(["AI — Natural Language to SOQL", "Manual Query Builder"])

with tab1:
    st.markdown(f"<h4 style='color:{DARK};font-weight:500;'>Describe what data you need in plain English</h4>", unsafe_allow_html=True)

    examples = [
        "Show me all Closed Won opportunities over $50k from last year",
        "Get all contacts at accounts in the Technology industry",
        "Find open opportunities with no activity in the last 30 days",
        "List all leads created this quarter that haven't been converted",
    ]

    ex_col = st.selectbox("Example queries", [""] + examples, label_visibility="collapsed")
    default_val = ex_col if ex_col else ""

    user_input = st.text_input(
        "Your query in plain English",
        value=default_val,
        placeholder="e.g. Show me all Closed Won opportunities over $50k from last year",
    )

    if st.button("Generate SOQL →", type="primary", disabled=not api_key):
        if user_input:
            with st.spinner("Writing query…"):
                try:
                    genai.configure(api_key=api_key)
                    model = genai.GenerativeModel(GEMINI_MODEL)
                    prompt = f"""Convert the following natural language request into a valid Salesforce SOQL query.
Only return the SOQL query string itself — no explanation, no markdown fencing.
Always include a LIMIT clause (use 200 unless the user specifies otherwise).
Request: {user_input}"""
                    response = model.generate_content(prompt)
                    query = response.text.strip().strip("```sql").strip("```").strip()

                    st.markdown("<hr>", unsafe_allow_html=True)
                    st.markdown(f"<div class='section-label'>Generated SOQL</div>", unsafe_allow_html=True)
                    st.code(query, language="sql")
                    st.info("**RevOps Tip:** Always include a `LIMIT` clause in high-volume environments to prevent governor limit issues. Use `OFFSET` for pagination.")

                except Exception as e:
                    err = str(e)
                    if "API_KEY_INVALID" in err or "API key not valid" in err:
                        st.error("❌ Invalid API key.")
                        st.session_state.gemini_api_key = None
                    else:
                        st.error(f"Something went wrong: {err}")
        else:
            st.warning("Please enter a query description.")

with tab2:
    st.markdown(f"<h4 style='color:{DARK};font-weight:500;'>Build a SOQL query visually</h4>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    SF_OBJECTS = {
        "Account":     ["Id", "Name", "Industry", "BillingState", "AnnualRevenue", "NumberOfEmployees", "OwnerId", "CreatedDate"],
        "Contact":     ["Id", "FirstName", "LastName", "Email", "Phone", "AccountId", "Title", "LeadSource"],
        "Opportunity": ["Id", "Name", "StageName", "Amount", "CloseDate", "AccountId", "OwnerId", "Probability"],
        "Lead":        ["Id", "FirstName", "LastName", "Email", "Company", "Status", "LeadSource", "IsConverted"],
        "Task":        ["Id", "Subject", "Status", "Priority", "WhoId", "WhatId", "ActivityDate", "OwnerId"],
        "Event":       ["Id", "Subject", "StartDateTime", "EndDateTime", "WhoId", "WhatId", "OwnerId"],
    }

    with col1:
        obj = st.selectbox("Salesforce Object", list(SF_OBJECTS.keys()))
        fields = st.multiselect(
            "SELECT Fields",
            SF_OBJECTS[obj],
            default=SF_OBJECTS[obj][:3],
        )
        limit = st.number_input("LIMIT", min_value=1, max_value=50000, value=200, step=50)

    with col2:
        add_where = st.checkbox("Add WHERE filter", value=True)
        if add_where:
            condition_field = st.selectbox("Filter by field", SF_OBJECTS[obj])
            operator = st.selectbox("Operator", ["=", "!=", ">", "<", ">=", "<=", "LIKE", "IN", "NOT IN"])
            value = st.text_input("Value", placeholder="e.g. Closed Won")
        add_order = st.checkbox("Add ORDER BY", value=False)
        if add_order:
            order_field = st.selectbox("Order by", SF_OBJECTS[obj])
            order_dir = st.radio("Direction", ["ASC", "DESC"], horizontal=True)

    if fields:
        field_str = ", ".join(fields)
        query_parts = [f"SELECT {field_str}", f"FROM {obj}"]

        if add_where and value:
            formatted_val = f"'{value}'" if operator not in ("IN", "NOT IN") else f"({value})"
            query_parts.append(f"WHERE {condition_field} {operator} {formatted_val}")

        if add_order:
            query_parts.append(f"ORDER BY {order_field} {order_dir}")

        query_parts.append(f"LIMIT {limit}")
        query_str = "\n".join(query_parts)

        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown('<div class="section-label">Generated Query</div>', unsafe_allow_html=True)
        st.code(query_str, language="sql")

        # Logic map
        where_str = f"{condition_field} {operator} {value}" if add_where and value else "no filter"
        order_str = f"ordered by {order_field} {order_dir}" if add_order else "no ordering"
        st.markdown(f"""
        <div class="logic-map">
            <strong>Query Logic:</strong> Fetch <strong>{', '.join(fields)}</strong> from
            <strong>{obj}</strong> where <strong>{where_str}</strong>, {order_str},
            returning up to <strong>{limit}</strong> records.
        </div>
        """, unsafe_allow_html=True)
    else:
        st.info("Select at least one field to generate a query.")

# ── How it works ─────────────────────────────────────────────────────────────
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown('<div class="section-label">How It Works</div>', unsafe_allow_html=True)

mermaid_chart("""
flowchart TB
    A([Plain English Request]) --> B[Gemini 1.5 Flash]
    B --> C([AI-Generated SOQL])
    D([Object + Fields + Conditions]) --> E[Visual Query Builder]
    E --> F([Generated SOQL + Logic Map])
""", height=220)

st.markdown("<hr>", unsafe_allow_html=True)
st.caption("Technical debt often grows because stakeholders don't understand the queries running their business. This tool bridges that gap.")
