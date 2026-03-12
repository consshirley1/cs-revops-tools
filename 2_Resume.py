import streamlit as st
import base64
from pathlib import Path

st.set_page_config(page_title="Resume — Connor Shirley", page_icon="📄", layout="wide")

st.markdown("""
<style>
    .stApp { background-color: #ffffff; }
    section[data-testid="stSidebar"] { background-color: #f8fafc; }
    .page-title { font-size: 2rem; font-weight: 300; margin-bottom: 0.25rem; }
    .page-title span { color: #1d4ed8; }
    hr { border: none; border-top: 1px solid #e5e7eb; margin: 1.5rem 0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="page-title">Resume — Connor <span>Shirley</span></div>', unsafe_allow_html=True)
st.markdown("Revenue Operations Leader · GTM Engineer")
st.markdown("<hr>", unsafe_allow_html=True)

RESUME_PATH = Path("assets/resume.pdf")

if RESUME_PATH.exists():
    with open(RESUME_PATH, "rb") as f:
        pdf_bytes = f.read()

    # Download button
    st.download_button(
        label="⬇️ Download Resume (PDF)",
        data=pdf_bytes,
        file_name="Connor_Smith_Resume.pdf",
        mime="application/pdf",
    )

    st.markdown("<div style='height: 1rem'></div>", unsafe_allow_html=True)

    # Inline PDF viewer
    b64 = base64.b64encode(pdf_bytes).decode("utf-8")
    pdf_display = f"""
    <iframe
        src="data:application/pdf;base64,{b64}"
        width="100%"
        height="900px"
        style="border: 1px solid #e5e7eb; border-radius: 4px;"
        type="application/pdf">
        <p>Your browser doesn't support inline PDFs.
        <a href="data:application/pdf;base64,{b64}" download="Connor_Smith_Resume.pdf">Download instead.</a></p>
    </iframe>
    """
    st.markdown(pdf_display, unsafe_allow_html=True)

else:
    st.warning("""
    **Resume PDF not found.**

    To add your resume:
    1. Place your PDF at `assets/resume.pdf` in the repo
    2. Redeploy — it will display inline with a download button automatically

    In the meantime, you can reach me directly to request a copy.
    """)

    st.markdown("💼 **[LinkedIn](https://www.linkedin.com/in/connor-shirley-93986954/)**")
    st.markdown("🐙 **[GitHub](https://github.com/consshirley1)**")