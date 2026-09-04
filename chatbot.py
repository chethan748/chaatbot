import streamlit as st

a = st.chat_input("Hey, I am Chethan Made AI :: ")

if a:
    st.chat_message("user").write(a)

    if a.lower() == "hii":
        st.chat_message("ai").write("Hello! 👋")

    elif a.lower() == "byee":
        st.chat_message("ai").write("Goodbye! 👋")

    elif a.lower() == "i":
        st.chat_message("ai").write(
            "Hello! My name is Chethan Made AI. 🤖 "
            "I am a simple chatbot created using Python and Streamlit. "
            "I can chat with you and answer basic questions!"
        )
