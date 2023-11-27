import streamlit as st
from components import chat, sidebar
from config import page_config


def main():
    page_config()  # Contains webiste info displays in the browser tab
    resume = sidebar()  # Sidebar of our app (resume is uploaded in the sidebar)

    if not resume:
        st.warning(body="Resume not detected", icon="⚠️")
    else:
        st.success(body="Resume is uploaded", icon="🎉")

        chat()  # Chatbot ui


if __name__ == "__main__":
    main()
