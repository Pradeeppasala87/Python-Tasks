from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
import os
from dotenv import load_dotenv
from fastapi.testclient import TestClient

load_dotenv()
app = FastAPI()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class ChatRequest(BaseModel):
    question: str

@app.post("/ask")
def ask(request: ChatRequest):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=request.question
        )
        return {"response": response.text}
    except Exception as e:
        return {"response": f"Error: {str(e)}"}

client_test = TestClient(app)
def test_server():
    res = client_test.post("/ask", json={"question": "Say hello!"})
    assert res.status_code == 200
    assert "response" in res.json()
    print("Streamlit server tests passed!")

if __name__ == "__main__":
    test_server()