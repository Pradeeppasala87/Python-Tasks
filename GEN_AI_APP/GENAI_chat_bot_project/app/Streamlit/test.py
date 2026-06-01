import os
from dotenv import load_dotenv
from google import genai

def test_gemini_connection():
    load_dotenv()
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
    try:
        response = client.models.generate_content(model="gemini-2.5-flash", contents="Hello")
        assert response.text is not None
        print("Streamlit Gemini connection test passed!")
    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
            print("API Rate Limit Exhausted. Please wait.")
        else:
            raise e

if __name__ == "__main__":
    test_gemini_connection()