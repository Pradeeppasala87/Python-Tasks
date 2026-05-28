# To run this code you need to install the following dependencies:
# pip install google-genai python-dotenv

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

def generate():
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-3.1-flash-lite"
    
    user_prompt = "What is FastAPI?"
    print(f"Asking AI: {user_prompt}\n")

    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=user_prompt), 
            ],
        ),
    ]
    
    generate_content_config = types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(
            thinking_level="MINIMAL",
        )
    )

    print("AI Response:")
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        if text := chunk.text:
            print(text, end="")
            
    print("\n")

if __name__ == "__main__":
    generate()