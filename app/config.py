import streamlit as st


def page_config():
    # Set the page config
    st.set_page_config(
        page_title="Omdena Chatbot",  # The title of the web page
        page_icon="💬",  # The icon of the web page, can be an emoji or a file path
        initial_sidebar_state="expanded",  # Expanded sidebar
    )
