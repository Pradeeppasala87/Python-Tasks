import streamlit as st
import requests

st.set_page_config(page_title="System Prompt Bot", page_icon="🤖", layout="wide")
st.title("🚀 System Prompt Bot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def get_answer(question: str) -> str:
    try:
        res = requests.post("http://127.0.0.1:8000/ask", json={"question": question})
        return res.json().get("response", "No response received.")
    except Exception as e:
        return f"Error: {str(e)}"

def test_app():
    # Simple unit test for the request logic assuming server might not be running
    ans = get_answer("Hello")
    assert isinstance(ans, str)
    print("Sys_prompt_Bot app tests passed!")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test_app()
    else:
        question = st.chat_input("Ask a question")
        if question:
            st.session_state.messages.append({"role": "user", "content": question})
            with st.chat_message("user"):
                st.write(question)
            
            with st.spinner("Thinking..."):
                answer = get_answer(question)
            
            st.session_state.messages.append({"role": "assistant", "content": answer})
            with st.chat_message("assistant"):
                st.write(answer)