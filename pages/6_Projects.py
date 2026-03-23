import streamlit as st
from shared import COMMON_CSS, DARK, TEAL_DARK, TEAL_MID, TEAL_LIGHT, PROJECTS
from sidebar import render_sidebar

st.set_page_config(page_title="Projects — Connor Shirley", page_icon=None, layout="wide")
render_sidebar()
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

st.markdown('<div class="page-title">Strategic <span>Projects</span></div>', unsafe_allow_html=True)
st.markdown(
    f"<p style='color:{DARK};font-size:0.9rem;'>Key initiatives structured via STAR methodology — Situation, Task, Action, Result.</p>",
    unsafe_allow_html=True,
)
st.markdown("<hr>", unsafe_allow_html=True)

# ── Tabs — one per project ────────────────────────────────────────────────────
tab_labels = [p["name"] for p in PROJECTS]
tabs = st.tabs(tab_labels)

for tab, project in zip(tabs, PROJECTS):
    with tab:
        st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

        # Project header
        col_info, col_metrics = st.columns([3, 2])
        with col_info:
            st.markdown(f"<h2 style='color:{DARK};font-weight:400;margin-bottom:0.1rem;'>{project['name']}</h2>", unsafe_allow_html=True)
            st.caption(project["context"])
            tag_html = "".join(f'<span class="tag-chip">{t}</span>' for t in project["tags"])
            st.markdown(tag_html, unsafe_allow_html=True)

        with col_metrics:
            st.markdown("<div class='section-label'>Impact at a Glance</div>", unsafe_allow_html=True)
            metrics_html = "".join(f'<span class="metric-pill">{m}</span>' for m in project["metrics"])
            st.markdown(metrics_html, unsafe_allow_html=True)

        st.markdown("<hr>", unsafe_allow_html=True)

        # STAR breakdown
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
