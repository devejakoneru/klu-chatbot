import streamlit as st
from chatbot_control.controller import handle_user_query
import os
import time
import base64

def speak(text):
    safe_text = text.replace('"', "'").replace("\n", " ")
    st.markdown(f"""
        <script>
        var msg = new SpeechSynthesisUtterance("{safe_text}");
        msg.rate = 1;
        msg.pitch = 1;
        msg.volume = 1;
        window.speechSynthesis.speak(msg);
        </script>
    """, unsafe_allow_html=True)


def start_ui():
    st.set_page_config(page_title="KLU Smart Assistant", layout="centered")

    st.markdown("""
    <style>

    .stApp {
        background: linear-gradient(145deg, #0f172a, #1e293b);
        color: white;
    }

    @keyframes float {
      0% { transform: translateY(0px); }
      50% { transform: translateY(-20px); }
      100% { transform: translateY(0px); }
    }

    .floating {
      position: fixed;
      width: 250px;
      height: 250px;
      background: rgba(59,130,246,0.08);
      border-radius: 50%;
      filter: blur(90px);
      animation: float 6s ease-in-out infinite;
      z-index: -1;
    }

    .f1 { top: 10%; left: 5%; }
    .f2 { top: 60%; right: 10%; animation-delay: 2s; }
    .f3 { bottom: 10%; left: 40%; animation-delay: 4s; }

    .chat-user {
        background: linear-gradient(145deg, #1e40af, #2563eb);
        padding: 12px 18px;
        border-radius: 20px;
        margin-bottom: 8px;
    }

    .chat-bot {
        background: rgba(255,255,255,0.08);
        padding: 12px 18px;
        border-radius: 20px;
        margin-bottom: 12px;
        border: 1px solid rgba(255,255,255,0.1);
    }

    .stButton>button {
        background: linear-gradient(145deg, #3b82f6, #2563eb);
        color: white;
        border-radius: 12px;
        border: none;
    }

    .pulse {
        height: 10px;
        width: 10px;
        background: #22c55e;
        border-radius: 50%;
        display: inline-block;
        animation: pulse-animation 2s infinite;
    }

    @keyframes pulse-animation {
        0% { box-shadow: 0 0 0 0 rgba(34,197,94,0.7); }
        70% { box-shadow: 0 0 0 10px rgba(34,197,94,0); }
        100% { box-shadow: 0 0 0 0 rgba(34,197,94,0); }
    }

    .bot-corner {
        position: fixed;
        bottom: 25px;
        right: 25px;
        width: 90px;
        z-index: 999;
        animation: floatBot 3s ease-in-out infinite;
        cursor: pointer;
    }

    @keyframes floatBot {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-12px); }
        100% { transform: translateY(0px); }
    }

    .bot-corner:hover {
        transform: scale(1.1);
    }

    </style>

    <div class="floating f1"></div>
    <div class="floating f2"></div>
    <div class="floating f3"></div>
    """, unsafe_allow_html=True)

    if os.path.exists("assets/chatbot_avatar.png"):
        with open("assets/chatbot_avatar.png", "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode()

        st.markdown(f"""
            <img src="data:image/png;base64,{encoded}" class="bot-corner">
        """, unsafe_allow_html=True)

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
        st.caption("Powered by Python & Streamlit")

    col1, col2 = st.columns([1, 5])

    with col1:
        if os.path.exists("assets/klu_logo.jpg"):
            st.image("assets/klu_logo.jpg", width=70)

    with col2:
        st.markdown("## KLU Smart Assistant <span class='pulse'></span>", unsafe_allow_html=True)
        st.markdown("How may I help you today?")

    st.divider()

    if "chat" not in st.session_state:
        st.session_state.chat = []

    for sender, msg_type, content in st.session_state.chat:
        if sender == "user":
            st.markdown(f"<div class='chat-user'><b>You:</b> {content}</div>", unsafe_allow_html=True)
        else:
            if msg_type == "text":
                st.markdown(f"<div class='chat-bot'><b>KLU AI:</b> {content}</div>", unsafe_allow_html=True)
            elif msg_type == "image":
                if os.path.exists(content):
                    st.image(content, width="stretch")

    with st.form("chat_form", clear_on_submit=True):
        user_input = st.text_input("Ask something:")
        send = st.form_submit_button("Send")

    if send and user_input.strip():

        st.session_state.chat.append(("user", "text", user_input))

        with st.spinner("🤖 Processing..."):
            msg_type, reply = handle_user_query(user_input)

        if msg_type == "text":
            placeholder = st.empty()
            typed = ""

            for char in reply:
                typed += char
                placeholder.markdown(
                    f"<div class='chat-bot'><b>KLU AI:</b> {typed}</div>",
                    unsafe_allow_html=True
                )
                time.sleep(0.01)

            st.session_state.chat.append(("bot", "text", reply))
            speak(reply)

        elif msg_type == "image":
            st.session_state.chat.append(("bot", "image", reply))

        st.rerun()