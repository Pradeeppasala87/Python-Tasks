import os
from google import genai
from dotenv import load_dotenv
from classifier import is_python_related
from system_prompt import SYSTEM_PROMPT

load_dotenv()

def generate(question: str) -> str:
    """Generates a response for a user question."""
    if not is_python_related(question):
        return "I'm currently designed to provide responses only for python platform-related learning queries."
    
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    full_prompt = f"{SYSTEM_PROMPT}\n\nUser Question:\n{question}"
    try:
        response = client.models.generate_content(model="gemini-2.5-flash", contents=full_prompt)
        return response.text
    except Exception as e:
        return f"Error: {e}"

def test_app():
    """Test the application response generation."""
    print("Running tests...")
    # Test unrelated question
    unrelated_res = generate("What is the capital of France?")
    assert "provide responses only" in unrelated_res
    print("System_Prompt app tests passed!")

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test_app()
    else:
        q = input("Enter your question: ")
        print(generate(q))