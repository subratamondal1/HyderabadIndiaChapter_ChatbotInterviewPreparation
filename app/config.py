import streamlit as __st


def page_config():
    # Set the page config
    __st.set_page_config(
        page_title="Omdena Chatbot",  # The title of the web page
        page_icon="💬",  # The icon of the web page, can be an emoji or a file path
        initial_sidebar_state="expanded",  # Expanded sidebar
    )


def page_session():
    # Initialize chat history
    if "messages" not in __st.session_state:
        __st.session_state.messages = []

    # Initialize user data
    if "user_data" not in __st.session_state:
        __st.session_state.user_data = None

    # Initialize greeting
    if "greeted" not in __st.session_state:
        __st.session_state.greeted = False
