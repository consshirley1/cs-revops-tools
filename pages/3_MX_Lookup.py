import streamlit as st
import dns.resolver
import re

st.set_page_config(page_title="MX Lookup — Email Provider Identifier", page_icon="📡", layout="wide")

st.markdown("""
<style>
    .page-title { font-size: 2rem; font-weight: 300; margin-bottom: 0.25rem; }
    .page-title span { color: #1d4ed8; }
    .provider-box {
        border: 1px solid #e5e7eb; border-radius: 6px;
        padding: 1.25rem 1.5rem; margin-bottom: 1rem;
    }
    .provider-name { font-size: 1.25rem; font-weight: 500; }
    .provider-type { font-size: 0.85rem; color: #6b7280; margin-top: 0.1rem; }
    .flag-present { color: #10b981; font-weight: 500; }
    .flag-absent  { color: #9ca3af; }
    hr { border: none; border-top: 1px solid #e5e7eb; margin: 1.5rem 0; }
    .section-label {
        font-size: 0.65rem; font-weight: 500; letter-spacing: 0.15em;
        text-transform: uppercase; color: #9ca3af; margin-bottom: 0.5rem;
    }
    .tag-blue { background:#eff6ff; color:#1d4ed8; font-size:0.72rem; padding:0.2rem 0.6rem; border-radius:3px; }
    .tag-gray { background:#f3f4f6; color:#6b7280; font-size:0.72rem; padding:0.2rem 0.6rem; border-radius:3px; }
    .tag-green { background:#ecfdf5; color:#10b981; font-size:0.72rem; padding:0.2rem 0.6rem; border-radius:3px; }
    .tag-yellow { background:#fffbeb; color:#f59e0b; font-size:0.72rem; padding:0.2rem 0.6rem; border-radius:3px; }
</style>
""", unsafe_allow_html=True)

# --- Provider definitions ---
PROVIDERS = [
    {
        "match": lambda hosts: any(re.search(r"google|gmail|googlemail", h, re.I) for h in hosts),
        "name": "Google Workspace",
        "type": "Cloud Email · Google",
        "icon": "📧",
        "crm": "Common with Salesforce, HubSpot",
        "segment": "SMB → Enterprise",
        "confidence": "High",
    },
    {
        "match": lambda hosts: any(re.search(r"outlook|hotmail|microsoft|office365|protection\.outlook", h, re.I) for h in hosts),
        "name": "Microsoft 365",
        "type": "Cloud Email · Microsoft",
        "icon": "📨",
        "crm": "Common with Dynamics, Salesforce",
        "segment": "Mid-Market → Enterprise",
        "confidence": "High",
    },
    {
        "match": lambda hosts: any(re.search(r"mimecast", h, re.I) for h in hosts),
        "name": "Mimecast",
        "type": "Email Security Gateway",
        "icon": "🛡️",
        "crm": "Gateway — underlying provider varies",
        "segment": "Enterprise",
        "confidence": "Medium",
    },
    {
        "match": lambda hosts: any(re.search(r"proofpoint", h, re.I) for h in hosts),
        "name": "Proofpoint",
        "type": "Email Security Gateway",
        "icon": "🔒",
        "crm": "Gateway — underlying provider varies",
        "segment": "Enterprise",
        "confidence": "Medium",
    },
    {
        "match": lambda hosts: any(re.search(r"barracuda", h, re.I) for h in hosts),
        "name": "Barracuda",
        "type": "Email Security Gateway",
        "icon": "🔐",
        "crm": "Gateway — underlying provider varies",
        "segment": "SMB → Mid-Market",
        "confidence": "Medium",
    },
    {
        "match": lambda hosts: any(re.search(r"mailgun", h, re.I) for h in hosts),
        "name": "Mailgun",
        "type": "Transactional Email",
        "icon": "⚡",
        "crm": "Developer / transactional use",
        "segment": "Startup → Tech",
        "confidence": "High",
    },
    {
        "match": lambda hosts: any(re.search(r"sendgrid", h, re.I) for h in hosts),
        "name": "SendGrid / Twilio",
        "type": "Transactional Email",
        "icon": "📤",
        "crm": "Developer / transactional use",
        "segment": "Startup → Mid-Market",
        "confidence": "High",
    },
    {
        "match": lambda hosts: any(re.search(r"amazonses|amazon", h, re.I) for h in hosts),
        "name": "Amazon SES",
        "type": "Cloud Email · AWS",
        "icon": "☁️",
        "crm": "Developer / transactional use",
        "segment": "Startup → Enterprise",
        "confidence": "High",
    },
    {
        "match": lambda hosts: any(re.search(r"zoho", h, re.I) for h in hosts),
        "name": "Zoho Mail",
        "type": "Cloud Email · Zoho",
        "icon": "📬",
        "crm": "Often paired with Zoho CRM",
        "segment": "SMB",
        "confidence": "High",
    },
    {
        "match": lambda hosts: any(re.search(r"protonmail|proton\.me", h, re.I) for h in hosts),
        "name": "Proton Mail",
        "type": "Encrypted Email · Proton",
        "icon": "🔏",
        "crm": "Privacy-first, rare in enterprise",
        "segment": "SMB → Privacy-focused",
        "confidence": "High",
    },
]


def clean_domain(raw: str) -> str:
    raw = raw.strip().lower()
    raw = re.sub(r"^https?://", "", raw)
    raw = re.sub(r"^www\.", "", raw)
    return raw.split("/")[0]


def lookup_mx(domain: str):
    resolver = dns.resolver.Resolver()
    resolver.timeout = 5
    resolver.lifetime = 5
    try:
        answers = resolver.resolve(domain, "MX")
        records = sorted(
            [{"priority": r.preference, "host": str(r.exchange).rstrip(".")} for r in answers],
            key=lambda x: x["priority"],
        )
        return records, None
    except dns.resolver.NXDOMAIN:
        return [], "Domain does not exist."
    except dns.resolver.NoAnswer:
        return [], "No MX records found for this domain."
    except dns.resolver.Timeout:
        return [], "DNS query timed out. Try again."
    except Exception as e:
        return [], str(e)


def lookup_txt(domain: str):
    resolver = dns.resolver.Resolver()
    resolver.timeout = 5
    resolver.lifetime = 5
    try:
        answers = resolver.resolve(domain, "TXT")
        return [r.to_text().strip('"') for r in answers]
    except Exception:
        return []


def identify_provider(mx_records):
    hosts = [r["host"] for r in mx_records]
    for p in PROVIDERS:
        if p["match"](hosts):
            return p
    return {
        "name": "Unknown / Custom",
        "type": "Self-hosted or custom MTA",
        "icon": "❓",
        "crm": "Requires manual investigation",
        "segment": "Unknown",
        "confidence": "Low",
    }


# --- UI ---
st.markdown('<div class="page-title">📡 MX Lookup — <span>Email Provider Identifier</span></div>', unsafe_allow_html=True)
st.markdown("Enter any domain to identify its email provider via live DNS/MX record lookup.")
st.markdown("<hr>", unsafe_allow_html=True)

col_input, col_examples = st.columns([3, 2])

with col_input:
    domain_input = st.text_input(
        "Domain",
        placeholder="company.com",
        label_visibility="collapsed",
    )

with col_examples:
    st.markdown("<div style='margin-top: 0.4rem; font-size: 0.8rem; color: #9ca3af;'>Try: </div>", unsafe_allow_html=True)
    ex_cols = st.columns(5)
    examples = ["google.com", "microsoft.com", "salesforce.com", "stripe.com", "hubspot.com"]
    for i, ex in enumerate(examples):
        with ex_cols[i]:
            if st.button(ex, key=f"ex_{ex}", use_container_width=True):
                domain_input = ex

run = st.button("Run Lookup →", type="primary", use_container_width=False)

if run and domain_input:
    domain = clean_domain(domain_input)

    with st.spinner(f"Querying MX records for {domain}…"):
        mx_records, error = lookup_mx(domain)
        txt_records = lookup_txt(domain)
        dmarc_records = lookup_txt(f"_dmarc.{domain}")

    if error:
        st.error(f"⚠️ {error}")
    elif not mx_records:
        st.warning("No MX records returned. This domain may not have email configured.")
    else:
        provider = identify_provider(mx_records)

        conf_tag = {
            "High":   '<span class="tag-green">High Confidence</span>',
            "Medium": '<span class="tag-yellow">Medium Confidence</span>',
            "Low":    '<span class="tag-gray">Low Confidence</span>',
        }.get(provider["confidence"], "")

        st.success(f"Resolved **{len(mx_records)} MX record{'s' if len(mx_records) > 1 else ''}** for `{domain}`")

        # Provider card
        st.markdown(f"""
        <div class="provider-box">
            <div style="display:flex; justify-content:space-between; align-items:flex-start;">
                <div>
                    <div class="provider-name">{provider['icon']} {provider['name']}</div>
                    <div class="provider-type">{provider['type']}</div>
                </div>
                <div>{conf_tag}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown('<div class="section-label">MX Records</div>', unsafe_allow_html=True)
            st.metric("Records Found", len(mx_records))
        with col2:
            st.markdown('<div class="section-label">CRM Context</div>', unsafe_allow_html=True)
            st.markdown(f"<div style='font-size:0.85rem; color:#374151;'>{provider['crm']}</div>", unsafe_allow_html=True)
        with col3:
            st.markdown('<div class="section-label">Typical Segment</div>', unsafe_allow_html=True)
            st.markdown(f"<div style='font-size:0.85rem; color:#374151;'>{provider['segment']}</div>", unsafe_allow_html=True)

        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown('<div class="section-label">MX Records</div>', unsafe_allow_html=True)
        import pandas as pd
        df = pd.DataFrame(mx_records)
        df.columns = ["Priority", "Mail Exchange Host"]
        st.dataframe(df, use_container_width=True, hide_index=True)

        # Security flags
        st.markdown("<hr>", unsafe_allow_html=True)
        st.markdown('<div class="section-label">Email Security</div>', unsafe_allow_html=True)

        spf = any("v=spf1" in r for r in txt_records)
        dmarc = any("v=DMARC1" in r for r in dmarc_records)
        redundant = len(mx_records) > 1

        flag_col1, flag_col2, flag_col3 = st.columns(3)
        with flag_col1:
            if spf:
                st.success("✅ SPF Configured")
            else:
                st.warning("⚠️ SPF Not Found")
        with flag_col2:
            if dmarc:
                st.success("✅ DMARC Configured")
            else:
                st.warning("⚠️ DMARC Not Found")
        with flag_col3:
            if redundant:
                st.success(f"✅ Redundant MX ({len(mx_records)} records)")
            else:
                st.info("ℹ️ Single MX record")

elif run and not domain_input:
    st.warning("Please enter a domain first.")

st.markdown("<hr>", unsafe_allow_html=True)
st.caption("Uses live DNS resolution via dnspython. No data is stored or logged.")
