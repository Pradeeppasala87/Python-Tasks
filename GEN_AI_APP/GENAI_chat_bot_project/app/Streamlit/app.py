import streamlit as st
import requests

st.set_page_config(page_title="Gemini ChatBot", page_icon="🤖", layout="wide")
st.title("🤖 Gemini ChatBot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

def get_response(question: str) -> str:
    try:
        res = requests.post("http://127.0.0.1:8000/ask", json={"question": question})
        return res.json().get("response", "Error in response")
    except Exception as e:
        return f"Error: {str(e)}"

def test_app():
    resp = get_response("Hello")
    assert isinstance(resp, str)
    print("Streamlit app tests passed!")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test_app()
    else:
        question = st.chat_input("Ask me anything...")
        if question:
            st.session_state.messages.append({"role": "user", "content": question})
            with st.chat_message("user"):
                st.markdown(question)
            
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    answer = get_response(question)
                    st.markdown(answer)
            
            st.session_state.messages.append({"role": "assistant", "content": answer})