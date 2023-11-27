import streamlit as st


def sidebar():
    # Omdena Logo
    with st.sidebar:
        st.image(image="images/omdena.png")
        st.markdown(
            body=(
                "<center>Welcome to Omdena interview preparation <strong>chatbot</strong>. "
                "Wish you all the luck 🤞🏼</center>"
            ),
            unsafe_allow_html=True,
        )

        st.divider()

        # Resume uploader label
        st.markdown(body="<center>Upload your Resume 📄</center>", unsafe_allow_html=True)

        # Resume uploader
        resume = st.file_uploader(label="upload file", type=["pdf", "docx"], label_visibility="hidden")

        st.divider()

        # Footer - Copyright info
        st.markdown(body="`© 2023 by Omdena. All rights reserved.`", unsafe_allow_html=True)

    return resume


def chat():
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages from history on app rerun
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # React to user input
    if prompt := st.chat_input("Start typing ..."):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = f"HR: {prompt}"
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response)
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})
