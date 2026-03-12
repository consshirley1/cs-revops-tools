import streamlit as st
from shared import COMMON_CSS, DARK, TEAL_DARK, TEAL_MID, TEAL_LIGHT, PROJECTS

st.set_page_config(page_title="Project Detail — Connor Shirley", page_icon=None, layout="wide")
st.markdown(COMMON_CSS, unsafe_allow_html=True)

st.markdown(f"""
<style>
    .star-box {{
        border: 1px solid {TEAL_LIGHT}; border-radius: 8px;
        padding: 1.1rem 1.25rem; background: #ffffff; height: 100%;
    }}
    .star-label {{
        font-size: 0.65rem; font-weight: 600; letter-spacing: 0.15em;
        text-transform: uppercase; color: {TEAL_MID}; margin-bottom: 0.4rem;
    }}
    .metric-pill {{
        display: inline-block;
        background: {TEAL_LIGHT}; color: {TEAL_DARK}; border-radius: 4px;
        font-size: 0.78rem; font-weight: 500; padding: 0.25rem 0.65rem;
        margin: 0.2rem 0.25rem 0.2rem 0;
    }}
    .result-box {{
        background: {TEAL_LIGHT}; border-left: 4px solid {TEAL_DARK};
        border-radius: 0 8px 8px 0; padding: 1.1rem 1.25rem;
    }}
</style>
""", unsafe_allow_html=True)

# ── Guard: redirect to index if no project selected ──────────────────────────
project_id = st.session_state.get("selected_project_id")
if not project_id:
    st.switch_page("pages/6_Projects.py")
    st.stop()

project = next((p for p in PROJECTS if p["id"] == project_id), None)
if not project:
    st.switch_page("pages/6_Projects.py")
    st.stop()

# ── Back button ──────────────────────────────────────────────────────────────
if st.button("Back to Projects", type="secondary"):
    st.session_state.pop("selected_project_id", None)
    st.switch_page("pages/6_Projects.py")

st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
st.markdown('<div class="page-title">Strategic <span>Projects</span></div>', unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# ── Project header ────────────────────────────────────────────────────────────
col_info, col_metrics = st.columns([3, 2])

with col_info:
    st.markdown(f"<h2 style='color:{DARK};font-weight:400;margin-bottom:0.1rem;'>{project['name']}</h2>", unsafe_allow_html=True)
    st.caption(project["context"])
    tag_html = "".join(f'<span class="tag-chip">{t}</span>' for t in project["tags"])
    st.markdown(tag_html, unsafe_allow_html=True)

with col_metrics:
    st.markdown(f"<div class='section-label'>Impact at a Glance</div>", unsafe_allow_html=True)
    metrics_html = "".join(f'<span class="metric-pill">{m}</span>' for m in project["metrics"])
    st.markdown(metrics_html, unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# ── STAR breakdown ────────────────────────────────────────────────────────────
s_col, t_col = st.columns(2)
a_col, r_col = st.columns(2)

with s_col:
    st.markdown(f"""
    <div class="star-box">
        <div class="star-label">Situation</div>
        <p style="font-size:0.88rem;color:{DARK};line-height:1.65;margin:0;">{project["star"]["situation"]}</p>
    </div>
    """, unsafe_allow_html=True)

with t_col:
    st.markdown(f"""
    <div class="star-box">
        <div class="star-label">Task</div>
        <p style="font-size:0.88rem;color:{DARK};line-height:1.65;margin:0;">{project["star"]["task"]}</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("<div style='height:0.75rem'></div>", unsafe_allow_html=True)

with a_col:
    st.markdown(f"""
    <div class="star-box">
        <div class="star-label">Action</div>
        <p style="font-size:0.88rem;color:{DARK};line-height:1.65;margin:0;">{project["star"]["action"]}</p>
    </div>
    """, unsafe_allow_html=True)

with r_col:
    st.markdown(f"""
    <div class="result-box">
        <div class="star-label" style="color:{TEAL_DARK};">Result</div>
        <p style="font-size:0.88rem;color:{DARK};line-height:1.65;margin:0;">{project["star"]["result"]}</p>
    </div>
    """, unsafe_allow_html=True)
