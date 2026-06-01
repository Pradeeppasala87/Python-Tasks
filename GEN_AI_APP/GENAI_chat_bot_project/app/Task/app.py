import streamlit as st
from chatbot import get_response

st.set_page_config(
    page_title="Movie Project AI",
    page_icon="🎬",
    layout="wide"
)

if "messages" not in st.session_state:
    st.session_state.messages = []

st.markdown(
    """
    <h1 style='text-align:center'>
    🎬 Movie Ticket Booking Project Assistant
    </h1>
    """,
    unsafe_allow_html=True
)

for msg in st.session_state.messages:

    with st.chat_message(msg["role"]):
        st.write(msg["content"])

question = st.chat_input(
    "Ask about the project..."
)

if question:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":question
        }
    )

    with st.chat_message("user"):
        st.write(question)

    with st.chat_message("assistant"):

        with st.spinner("Analyzing project..."):

            answer = get_response(question)

            st.write(answer)

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )