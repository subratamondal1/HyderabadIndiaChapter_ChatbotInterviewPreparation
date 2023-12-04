import streamlit as st
from components import chat, sidebar
from config import page_config, page_session

# from lib.agents import


def main():
    # Page session
    page_session()

    # Page config
    page_config()

    # Sidebar
    sidebar()

    # Chat UI
    chat()


if __name__ == "__main__":
    main()
