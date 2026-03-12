# CS RevOps Tools

A collection of live RevOps tools and demos built by Connor Shirley.

## Tools

| Tool | Description |
|------|-------------|
| **MX Lookup** | Identify email providers via live DNS/MX record lookup |
| **Company Summarizer** | AI-generated company one-pagers for GTM research |
| **INSEE Gap Detector** | Salesforce account coverage analysis for the French market |

## Stack

- [Streamlit](https://streamlit.io) — UI framework
- [dnspython](https://www.dnspython.org) — live DNS resolution
- [Anthropic Claude](https://anthropic.com) — AI summaries
- [Streamlit Community Cloud](https://streamlit.io/cloud) — deployment

## Running Locally

```bash
pip install -r requirements.txt
streamlit run Home.py
```

## Secrets

For the Company Summarizer, add your Gemini API key to `.streamlit/secrets.toml`:

```toml
GEMINI_API_KEY = "AIza..."
```

On Streamlit Community Cloud, add this via **App Settings → Secrets**.
Get a free key at [aistudio.google.com](https://aistudio.google.com/app/apikey).

## Adding a New Tool

1. Create a new file in `pages/` — e.g. `6_My_New_Tool.py`
2. Streamlit auto-discovers it and adds it to the sidebar
3. Push to GitHub — Streamlit Community Cloud redeploys automatically

## Resume

Drop your resume PDF at `assets/resume.pdf` and it will appear on the Resume page.