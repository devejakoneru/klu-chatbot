import streamlit as st
from chatbot_control.controller import handle_user_query
import os
import time


def start_ui():
    st.set_page_config(page_title="KLU Smart Assistant", layout="centered")

    # =========================
    # 🎨 DARK AI STYLE
    # =========================
    st.markdown("""
    <style>
    body {
        background-color: #0f172a;
    }

    .stApp {
        background: linear-gradient(145deg, #0f172a, #1e293b);
        color: #ffffff;
    }

    /* Chat bubbles */
    .chat-user {
        background: linear-gradient(145deg, #1e40af, #2563eb);
        padding: 12px 18px;
        border-radius: 20px;
        margin-bottom: 8px;
        color: white;
        box-shadow: 0 0 10px rgba(37, 99, 235, 0.5);
    }

    .chat-bot {
        background: rgba(255, 255, 255, 0.08);
        padding: 12px 18px;
        border-radius: 20px;
        margin-bottom: 12px;
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255,255,255,0.1);
    }

    /* Buttons */
    .stButton>button {
        background: linear-gradient(145deg, #3b82f6, #2563eb);
        color: white;
        border-radius: 12px;
        border: none;
        box-shadow: 0 0 10px rgba(59, 130, 246, 0.5);
    }

    /* Input */
    .stTextInput>div>div>input {
        border-radius: 12px;
        background-color: #1e293b;
        color: white;
    }

    </style>
    """, unsafe_allow_html=True)

    # =========================
    # SIDEBAR
    # =========================
    with st.sidebar:
        st.title("KLU Smart Assistant 🤖")
        st.write("AI-based Academic Help System")
        st.divider()
        st.markdown("""
        🔹 Admissions  
        🔹 Fees & ERP  
        🔹 Exams  
        🔹 Hostel  
        🔹 Library  
        🔹 Leadership  
        """)
        st.divider()
        st.caption("Powered by Python & Streamlit")

    # =========================
    # HEADER
    # =========================
    col1, col2 = st.columns([1, 5])

    with col1:
        if os.path.exists("assets/klu_logo.jpg"):
            st.image("assets/klu_logo.jpg", width=70)

    with col2:
        st.markdown("## Welcome to KLU Smart Assistant 🤖")
        st.markdown("How may I help you today?")

    st.divider()

    # =========================
    # SESSION STATE
    # =========================
    if "chat" not in st.session_state:
        st.session_state.chat = []

    # =========================
    # DISPLAY CHAT
    # =========================
    for sender, msg_type, content in st.session_state.chat:
        if sender == "user":
            st.markdown(f"<div class='chat-user'><b>You:</b> {content}</div>", unsafe_allow_html=True)
        else:
            if msg_type == "text":
                st.markdown(f"<div class='chat-bot'><b>KLU AI:</b> {content}</div>", unsafe_allow_html=True)
            else:
                st.image(content, width="stretch")

    # =========================
    # INPUT
    # =========================
    with st.form("chat_form", clear_on_submit=True):
        user_input = st.text_input("Ask something:")
        send = st.form_submit_button("Send")

    # Quick Buttons
    c1, c2, c3, c4 = st.columns(4)

    if c1.button("📘 Rules"):
        user_input, send = "college rules", True

    if c2.button("💰 Fees"):
        user_input, send = "fee structure", True

    if c3.button("📚 Library"):
        user_input, send = "library", True

    if c4.button("🗺 Campus Map"):
        user_input, send = "campus map", True

    # =========================
    # PROCESS INPUT
    # =========================
    if send and user_input.strip():
        st.session_state.chat.append(("user", "text", user_input))

        with st.spinner("🤖 Processing..."):
            msg_type, reply = handle_user_query(user_input)

        st.session_state.chat.append(("bot", msg_type, reply))
        st.rerun()