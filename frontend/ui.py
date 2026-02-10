import streamlit as st
from chatbot_control.controller import handle_user_query


def start_ui():
    st.set_page_config(page_title="KLU Chatbot", layout="centered")

    # HEADER
    col1, col2 = st.columns([1, 5])
    with col1:
        st.image("assets/klu_logo.jpg", width=70)
    with col2:
        st.markdown("## Welcome to **KLU Chatbot**")
        st.markdown("How may I help you today?")

    st.divider()

    # SESSION STATE
    if "chat" not in st.session_state:
        st.session_state.chat = []

    # DISPLAY CHAT
    for sender, msg_type, content in st.session_state.chat:
        if sender == "user":
            st.markdown(f"**You:** {content}")
        else:
            if msg_type == "text":
                st.markdown(f"**KLU Bot:** {content}")
            else:
                st.image(content, use_container_width=True)

    # INPUT AREA (NO manual clearing)
    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_input("Ask your question:")
        send = st.form_submit_button("Send")

    # QUICK BUTTONS
    c1, c2, c3, c4 = st.columns(4)
    if c1.button("Rules"):
        user_input, send = "college rules", True
    if c2.button("Fees"):
        user_input, send = "fee structure", True
    if c3.button("Library"):
        user_input, send = "library books", True
    if c4.button("Campus Map"):
        user_input, send = "campus map", True

    # PROCESS INPUT
    if send and user_input.strip():
        st.session_state.chat.append(("user", "text", user_input))

        msg_type, response = handle_user_query(user_input)
        if msg_type == "text":
            response = enhance_response(response)

        st.session_state.chat.append(("bot", msg_type, response))

        st.rerun()
