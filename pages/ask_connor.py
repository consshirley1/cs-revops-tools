"""Ask Connor — AI chatbot powered by Claude, grounded in portfolio context."""

import streamlit as st
from anthropic import Anthropic
from portfolio_context import PORTFOLIO_CONTEXT
from shared import COMMON_CSS, DARK, TEAL_DARK, TEAL_MID, TEAL_LIGHT
from sidebar import render_sidebar

st.set_page_config(page_title="Ask Connor — AI Chat", page_icon=None, layout="wide")
render_sidebar()
st.markdown(COMMON_CSS, unsafe_allow_html=True)

# ── Page-specific CSS ────────────────────────────────────────────────────────
st.markdown(f"""
<style>
    .chat-user {{
        background: {DARK}; color: #ffffff; border-radius: 8px;
        padding: 0.85rem 1.1rem; margin-bottom: 0.6rem; font-size: 0.9rem;
        line-height: 1.6; max-width: 85%;
        margin-left: auto;
    }}
    .chat-assistant {{
        background: #ffffff; color: {DARK}; border-radius: 8px;
        border-left: 4px solid {TEAL_DARK}; padding: 0.85rem 1.1rem;
        margin-bottom: 0.6rem; font-size: 0.9rem; line-height: 1.6;
        max-width: 85%;
    }}
    .chip {{
        display: inline-block; background: {TEAL_LIGHT}; color: {TEAL_DARK};
        font-size: 0.78rem; padding: 0.3rem 0.75rem; border-radius: 99px;
        margin: 0.2rem 0.3rem 0.2rem 0; cursor: pointer; font-weight: 500;
        border: 1px solid {TEAL_MID}44;
    }}
</style>
""", unsafe_allow_html=True)

# ── System prompt ────────────────────────────────────────────────────────────
SYSTEM_PROMPT = f"""You are Connor Shirley's portfolio assistant. You answer questions about
Connor's background, experience, skills, projects, and the tools in this portfolio app.

You are friendly, concise, and professional. You speak in the third person about Connor
unless the question is clearly directed at "you" in the context of the portfolio.

RULES:
- Only answer questions grounded in the portfolio context below.
- If a question is outside the scope of Connor's background or this portfolio, say so politely
  and redirect to relevant topics.
- Never fabricate information not present in the context.
- Keep answers concise — 2-4 sentences for simple questions, up to a short paragraph for
  complex ones.
- If asked about contacting Connor, share his LinkedIn and email from the context.

PORTFOLIO CONTEXT:
{PORTFOLIO_CONTEXT}
"""

# ── Injection detection ──────────────────────────────────────────────────────
INJECTION_PATTERNS = [
    "ignore previous", "ignore above", "disregard", "forget your instructions",
    "new instructions", "you are now", "act as", "pretend you are",
    "system prompt", "reveal your prompt", "show me your instructions",
    "override", "jailbreak",
]


def is_injection(text: str) -> bool:
    lower = text.lower()
    return any(p in lower for p in INJECTION_PATTERNS)


# ── Session state ────────────────────────────────────────────────────────────
if "ask_messages" not in st.session_state:
    st.session_state.ask_messages = []

if "ask_input" not in st.session_state:
    st.session_state.ask_input = ""

# ── Header ───────────────────────────────────────────────────────────────────
st.markdown('<div class="page-title">Ask <span>Connor</span></div>', unsafe_allow_html=True)
st.markdown(
    f"<p style='color:{TEAL_MID};font-size:0.9rem;'>AI-powered Q&A grounded in Connor's resume, projects, and portfolio tools.</p>",
    unsafe_allow_html=True,
)
st.markdown("<hr>", unsafe_allow_html=True)

# ── Suggestion chips ─────────────────────────────────────────────────────────
SUGGESTIONS = [
    "What tools has Connor built?",
    "Tell me about his AI micro-apps",
    "What's his experience with Salesforce?",
    "How did he handle the acquisition integration?",
    "What is MEDDPIC?",
    "What role is Connor looking for?",
]

chip_cols = st.columns(len(SUGGESTIONS))
for i, suggestion in enumerate(SUGGESTIONS):
    with chip_cols[i]:
        if st.button(suggestion, key=f"chip_{i}", use_container_width=True):
            st.session_state.ask_input = suggestion
            st.rerun()

st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

# ── Chat history display ─────────────────────────────────────────────────────
for msg in st.session_state.ask_messages:
    if msg["role"] == "user":
        st.markdown(f'<div class="chat-user">{msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-assistant">{msg["content"]}</div>', unsafe_allow_html=True)

# ── Input row ────────────────────────────────────────────────────────────────
col_input, col_send, col_clear = st.columns([6, 1, 1])

with col_input:
    user_input = st.text_input(
        "Ask a question about Connor's background, projects, or tools",
        value=st.session_state.ask_input,
        key="ask_text_input",
        label_visibility="collapsed",
        placeholder="Ask about Connor's experience, projects, or tools…",
    )

with col_send:
    send = st.button("Send", type="primary", use_container_width=True)

with col_clear:
    if st.button("Clear", use_container_width=True):
        st.session_state.ask_messages = []
        st.session_state.ask_input = ""
        st.rerun()

# ── Send logic ───────────────────────────────────────────────────────────────
if send and user_input:
    st.session_state.ask_input = ""

    if is_injection(user_input):
        st.session_state.ask_messages.append({"role": "user", "content": user_input})
        st.session_state.ask_messages.append({
            "role": "assistant",
            "content": "I'm here to answer questions about Connor's background and portfolio. I can't help with that request, but feel free to ask about his experience, projects, or tools!",
        })
        st.rerun()

    st.session_state.ask_messages.append({"role": "user", "content": user_input})

    # Build API messages from history
    api_messages = [
        {"role": m["role"], "content": m["content"]}
        for m in st.session_state.ask_messages
    ]

    with st.spinner("Thinking…"):
        try:
            client = Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=512,
                system=SYSTEM_PROMPT,
                messages=api_messages,
            )
            reply = response.content[0].text
        except Exception as e:
            reply = f"Sorry, something went wrong: {e}"

    st.session_state.ask_messages.append({"role": "assistant", "content": reply})
    st.rerun()

elif send and not user_input:
    st.warning("Please type a question first.")

# ── Footer ───────────────────────────────────────────────────────────────────
st.markdown("<hr>", unsafe_allow_html=True)
st.caption("Powered by Anthropic Claude. Answers are grounded in Connor's portfolio content and may not cover topics outside that scope.")
