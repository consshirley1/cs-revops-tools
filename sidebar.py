"""Shared sidebar component with compact Ask Connor chat and Book a Call embed."""

import streamlit as st
import streamlit.components.v1 as components
from anthropic import Anthropic
from portfolio_context import PORTFOLIO_CONTEXT

# ── System prompt (mirrors ask_connor.py) ────────────────────────────────────
# NOTE: Duplicated here to avoid circular imports. Keep in sync with
# pages/ask_connor.py SYSTEM_PROMPT.
_SIDEBAR_SYSTEM_PROMPT = f"""You are Connor Shirley's portfolio assistant. You answer questions about
Connor's background, experience, skills, projects, and the tools in this portfolio app.

You are friendly, concise, and professional. You speak in the third person about Connor
unless the question is clearly directed at "you" in the context of the portfolio.

RULES:
- Only answer questions grounded in the portfolio context below.
- If a question is outside the scope of Connor's background or this portfolio, say so politely
  and redirect to relevant topics.
- Never fabricate information not present in the context.
- Keep answers very short — 1-2 sentences max. Be punchy and direct.
- If asked about contacting Connor, share his LinkedIn and email from the context.

PORTFOLIO CONTEXT:
{PORTFOLIO_CONTEXT}
"""

# ── Injection detection ──────────────────────────────────────────────────────
_INJECTION_PATTERNS = [
    "ignore previous", "ignore above", "disregard", "forget your instructions",
    "new instructions", "you are now", "act as", "pretend you are",
    "system prompt", "reveal your prompt", "show me your instructions",
    "override", "jailbreak",
]


def _is_injection(text: str) -> bool:
    lower = text.lower()
    return any(p in lower for p in _INJECTION_PATTERNS)


def render_sidebar():
    """Render the shared sidebar with Ask Connor chat widget and Book a Call embed."""

    with st.sidebar:
        # ── Sidebar CSS ──────────────────────────────────────────────────────
        st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=DM+Mono:wght@400;500&display=swap');

            .sb-header {
                font-family: 'DM Mono', monospace;
                font-size: 0.7rem;
                font-weight: 500;
                letter-spacing: 0.18em;
                text-transform: uppercase;
                color: #c84b2f;
                margin-bottom: 0.5rem;
                margin-top: 0.75rem;
            }
            .sb-chat-user {
                background: #0f0f0f;
                color: #f7f4ef;
                border-radius: 6px;
                padding: 0.5rem 0.7rem;
                margin-bottom: 0.4rem;
                font-size: 0.8rem;
                font-family: 'DM Sans', sans-serif;
                line-height: 1.5;
            }
            .sb-chat-assistant {
                background: #ffffff;
                color: #0f0f0f;
                border-radius: 6px;
                border-left: 3px solid #c84b2f;
                padding: 0.5rem 0.7rem;
                margin-bottom: 0.4rem;
                font-size: 0.8rem;
                font-family: 'DM Sans', sans-serif;
                line-height: 1.5;
            }
            .sb-link {
                font-family: 'DM Sans', sans-serif;
                font-size: 0.75rem;
                color: #c84b2f;
                text-decoration: none;
                opacity: 0.8;
            }
            .sb-subtitle {
                font-family: 'DM Sans', sans-serif;
                font-size: 0.78rem;
                color: #555;
                margin-bottom: 0.5rem;
            }
        </style>
        """, unsafe_allow_html=True)

        # ── Section A: Ask Connor Chat Widget ────────────────────────────────
        st.markdown('<div class="sb-header">ASK CONNOR</div>', unsafe_allow_html=True)

        # Initialize sidebar session state
        if "sidebar_messages" not in st.session_state:
            st.session_state.sidebar_messages = []

        # Display last 6 messages only (keep full history for API context)
        display_messages = st.session_state.sidebar_messages[-6:]
        for msg in display_messages:
            if msg["role"] == "user":
                st.markdown(
                    f'<div class="sb-chat-user">{msg["content"]}</div>',
                    unsafe_allow_html=True,
                )
            else:
                st.markdown(
                    f'<div class="sb-chat-assistant">{msg["content"]}</div>',
                    unsafe_allow_html=True,
                )

        # Input row
        col_in, col_btn = st.columns([4, 1])
        with col_in:
            sidebar_input = st.text_input(
                "Ask Connor",
                key="sidebar_chat_input",
                label_visibility="collapsed",
                placeholder="Ask something…",
            )
        with col_btn:
            sidebar_send = st.button("→", key="sidebar_send", use_container_width=True)

        # Send logic
        if sidebar_send and sidebar_input:
            if _is_injection(sidebar_input):
                st.session_state.sidebar_messages.append(
                    {"role": "user", "content": sidebar_input}
                )
                st.session_state.sidebar_messages.append({
                    "role": "assistant",
                    "content": "I can only answer questions about Connor's background and portfolio.",
                })
                st.rerun()

            st.session_state.sidebar_messages.append(
                {"role": "user", "content": sidebar_input}
            )

            api_messages = [
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.sidebar_messages
            ]

            try:
                client = Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])
                response = client.messages.create(
                    model="claude-sonnet-4-20250514",
                    max_tokens=120,
                    system=_SIDEBAR_SYSTEM_PROMPT,
                    messages=api_messages,
                )
                reply = response.content[0].text
            except Exception as e:
                reply = f"Error: {e}"

            st.session_state.sidebar_messages.append(
                {"role": "assistant", "content": reply}
            )
            st.rerun()

        # Full conversation link
        st.markdown(
            '<div style="margin-top:0.3rem;"><span class="sb-link" style="cursor:pointer;">→ Full conversation</span></div>',
            unsafe_allow_html=True,
        )
        if st.button("Open full chat", key="sidebar_full_chat", type="secondary", use_container_width=True):
            st.switch_page("pages/ask_connor.py")

        st.markdown("<hr style='margin:1rem 0;'>", unsafe_allow_html=True)

        # ── Section B: Book a Call ───────────────────────────────────────────
        st.markdown('<div class="sb-header">BOOK A CALL</div>', unsafe_allow_html=True)
        st.markdown('<div class="sb-subtitle">30 min · Google Meet</div>', unsafe_allow_html=True)

        components.html(
            """
            <div style="border-radius:4px; overflow:hidden;">
                <iframe
                    src="https://cal.com/connor-shirley-akvszl/30-min-intro-call"
                    width="100%"
                    height="600"
                    frameborder="0"
                ></iframe>
            </div>
            """,
            height=620,
        )
