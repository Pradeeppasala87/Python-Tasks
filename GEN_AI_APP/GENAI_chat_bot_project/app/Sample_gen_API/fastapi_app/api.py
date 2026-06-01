from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
# It's safe to initialize the client here if key is present, otherwise handle gracefully below
client = genai.Client(api_key=GEMINI_API_KEY) if GEMINI_API_KEY else None

class PromptRequest(BaseModel):
    prompt: str
    model: Optional[str] = "gemini-2.5-flash"

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "GenAI FastAPI running"}

@app.post("/generate")
async def generate(prompt_request: PromptRequest):
    if not client:
        raise HTTPException(status_code=500, detail="Gemini API key not configured. Set GEMINI_API_KEY in .env.")

    try:
        response = client.models.generate_content(
            model=prompt_request.model,
            contents=prompt_request.prompt,
        )
        answer = response.text
    except Exception as exc:
        error_msg = str(exc)
        if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
            raise HTTPException(status_code=429, detail="API Rate Limit / Quota Exhausted. Please wait.")
        raise HTTPException(status_code=500, detail=error_msg)

    return {
        "prompt": prompt_request.prompt,
        "model": prompt_request.model,
        "response": answer,
    }
