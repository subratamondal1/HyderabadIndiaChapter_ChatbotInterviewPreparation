import streamlit as __st

from app.types import UserData


def sidebar():
    # Omdena Logo
    with __st.sidebar:
        __st.image(image="images/omdena.png")
        __st.markdown(
            body=(
                "<h2><center>Hyderabad, India</center></h2>"
                "<center><code>Interview Preparation Chatbot</code></center>"
                "<hr>"
            ),
            unsafe_allow_html=True,
        )

        with __st.form(key="user_data_form", clear_on_submit=False):
            # Full name
            fullname = __st.text_input(
                label="Full Name",
                placeholder="First Last",
                help="Enter your full name (First & Last name)",
            )

            # Role
            role = __st.text_input(
                label="Role",
                placeholder="Data Scientist",
                help="Enter your role you are applying for (Data Scientist, Data Analyst, etc.)",
            )

            # Years of experience
            experience = __st.number_input(
                label="Years of Experience",
                min_value=0,
                max_value=20,
                value=0,
                help="Enter your years of experience",
            )

            # About
            about = __st.text_area(
                label="About",
                placeholder="Tell us about yourself",
                help="Tell us about yourself",
                max_chars=400,
            )

            # Resume uploader
            resume = __st.file_uploader(
                label="Upload Resume",
                type=["pdf", "docx"],
                label_visibility="visible",
                help="Upload your resume here",
            )

            # Submit button
            submit = __st.form_submit_button(label="Submit")

            # Validation
            if submit:
                if not fullname:
                    __st.toast("Tell us your full name")
                if not role:
                    __st.toast("Tell us the role you are applying for")
                if not experience:
                    __st.toast("Tell us your years of experience")
                if not about:
                    __st.toast("Tell us about yourself")

                if fullname and role and about:
                    __st.toast("Your data has been submitted successfully")

                    # Save user data
                    __st.session_state.user_data = UserData(
                        fullname=fullname,
                        role=role,
                        experience=experience,
                        about=about,
                        resume=resume,
                    )

        __st.divider()

        # Footer - Copyright info
        __st.markdown(body="`©2023 by Omdena. All rights reserved.`", unsafe_allow_html=True)


def chat() -> None:
    # Check if user data is available in the session state
    user_data = __st.session_state.user_data

    # Display chat messages from history on app rerun
    for message in __st.session_state.messages:
        with __st.chat_message(message["role"]):
            __st.markdown(message["content"])

    # React to user input
    prompt = __st.chat_input("Start typing ...", disabled=not user_data)

    if not user_data:
        # Display welcome message from assistant if user data is None
        welcome_message = "Hi there! Before we start, please fill out the form so I can better assist you. 📝"

        # Add welcome message to chat history only if it's not already present
        if not __st.session_state.messages or __st.session_state.messages[-1]["content"] != welcome_message:
            with __st.chat_message("assistant"):
                __st.markdown(welcome_message)

            __st.session_state.messages.append({"role": "assistant", "content": welcome_message})
    elif user_data and prompt:
        # Display user message in chat message container
        __st.chat_message("user").markdown(prompt)

        # Add user message to chat history
        __st.session_state.messages.append({"role": "user", "content": prompt})

        response = f"HR: {prompt}"
        # Display assistant response in chat message container
        with __st.chat_message("assistant"):
            __st.markdown(response)

        # Add assistant response to chat history
        __st.session_state.messages.append({"role": "assistant", "content": response})

    # Greet the user and start the interview questions after successful form submission
    if user_data and not __st.session_state.greeted:
        # Greet the user with their name and the role they applied for
        greeting_message = (
            f"Hi {user_data['fullname']}! Welcome to the interview for the " f"{user_data['role']} position. 🌟"
        )
        with __st.chat_message("assistant"):
            __st.markdown(greeting_message)

        # Add greeting message to chat history
        __st.session_state.messages.append({"role": "assistant", "content": greeting_message})

        # Start asking interview questions
        interview_start_message = (
            "Let's get started with the interview questions. "
            "I'll ask a series of questions, and you can respond when you're ready. 😊"
        )
        with __st.chat_message("assistant"):
            __st.markdown(interview_start_message)

        # Add interview start message to chat history
        __st.session_state.messages.append({"role": "assistant", "content": interview_start_message})

        # Mark the user as greeted to avoid repeating this section
        __st.session_state.greeted = True
