import streamlit as st
import base64
from pathlib import Path
from shared import COMMON_CSS, DARK, TEAL_DARK, TEAL_MID, TEAL_LIGHT
from sidebar import render_sidebar

st.set_page_config(page_title="Resume — Connor Shirley", page_icon=None, layout="wide")
render_sidebar()
st.markdown(COMMON_CSS, unsafe_allow_html=True)

st.markdown('<div class="page-title">Resume — Connor <span>Shirley</span></div>', unsafe_allow_html=True)
st.markdown(f"<p style='color:{TEAL_MID};font-size:0.95rem;'>RevOps Leader turned GTM Engineer &nbsp;·&nbsp; AI Deployment &nbsp;·&nbsp; CRM Architecture</p>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

RESUME_PATH = Path("assets/resume.pdf")

if RESUME_PATH.exists():
    with open(RESUME_PATH, "rb") as f:
        pdf_bytes = f.read()

    st.download_button(
        label="Download Resume (PDF)",
        data=pdf_bytes,
        file_name="Connor_Shirley_Resume.pdf",
        mime="application/pdf",
    )

    st.markdown("<div style='height: 1rem'></div>", unsafe_allow_html=True)

    b64 = base64.b64encode(pdf_bytes).decode("utf-8")
    pdf_display = f"""
    <iframe
        src="data:application/pdf;base64,{b64}"
        width="100%"
        height="900px"
        style="border: 1px solid {TEAL_LIGHT}; border-radius: 4px;"
        type="application/pdf">
        <p>Your browser doesn't support inline PDFs.
        <a href="data:application/pdf;base64,{b64}" download="Connor_Shirley_Resume.pdf">Download instead.</a></p>
    </iframe>
    """
    st.markdown(pdf_display, unsafe_allow_html=True)

else:
    st.markdown(f"""
    <div style='background:{TEAL_LIGHT};border-radius:8px;padding:1.1rem 1.25rem;margin-bottom:1rem;font-size:0.9rem;color:{DARK};line-height:1.7;'>
    <strong>Resume PDF not found.</strong><br><br>
    To add your resume, place your PDF at <code>assets/resume.pdf</code> in the repo and redeploy — it will display inline with a download button automatically.<br><br>
    In the meantime, you can reach me directly to request a copy.
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"<p><a href='https://www.linkedin.com/in/connor-shirley-93986954/' style='color:{TEAL_DARK};font-weight:500;'>LinkedIn</a> &nbsp;&nbsp; <a href='https://github.com/consshirley1' style='color:{TEAL_DARK};font-weight:500;'>GitHub</a></p>", unsafe_allow_html=True)
