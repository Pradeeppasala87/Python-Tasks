from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
import os
from dotenv import load_dotenv
from fastapi.testclient import TestClient
from system_prompt import SYSTEM_PROMPT

load_dotenv()
app = FastAPI()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

class ChatRequest(BaseModel):
    question: str

@app.post("/ask")
def ask(request: ChatRequest):
    prompt = f"{SYSTEM_PROMPT}\n\nUser Question:\n{request.question}"
    try:
        response = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
        return {"response": response.text}
    except Exception as e:
        return {"response": f"Error: {str(e)}"}

client_test = TestClient(app)
def test_server():
    res = client_test.post("/ask", json={"question": "What is Python?"})
    assert res.status_code == 200
    assert "response" in res.json()
    print("Sys_prompt_Bot server tests passed!")

if __name__ == "__main__":
    test_server()