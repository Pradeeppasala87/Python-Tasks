import os
from google import genai

def is_python_related(question: str) -> bool:
    """Classifies if a question is related to Python or Programming."""
    client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))
    prompt = f"Return YES if the question is about Python, AI, or programming, else NO.\nQuestion: {question}"
    try:
        response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
        return "YES" in response.text.upper()
    except Exception:
        return False

def test_classifier():
    """Test the classifier functionality."""
    from dotenv import load_dotenv
    load_dotenv()
    assert is_python_related("What is a python dictionary?") == True
    assert is_python_related("How to bake a cake?") == False
    print("System_Prompt classifier tests passed!")

if __name__ == "__main__":
    test_classifier()