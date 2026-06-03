# To run this code you need to install the following dependencies:
# pip install google-genai

import os
import time
import random
from google import genai
from google.genai import types
from google.genai import errors as genai_errors
from dotenv import load_dotenv

load_dotenv()


def generate(question):
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    env_model = os.environ.get("GEMINI_MODEL", "gemini-3-flash-preview")
    models = [env_model, "gemini-1.0", "gemini-1.5"]
    max_retries = 6

    for model in models:
        print(f"Trying model: {model}")
        backoff = 1
        for attempt in range(1, max_retries + 1):
            try:
                for chunk in client.models.generate_content_stream(model=model, contents=question):
                    if text := chunk.text:
                        print(text, end="")
                return
            except genai_errors.ServerError as e:
                jitter = random.uniform(0, 1)
                wait = backoff + jitter
                print(f"\nServerError for {model} (attempt {attempt}/{max_retries}): {e}")
                if attempt < max_retries:
                    print(f"Waiting {wait:.1f}s before retry...")
                    time.sleep(wait)
                    backoff *= 2
                    continue
                else:
                    print(f"Model {model} exhausted, trying next model...")
                    break
            except Exception as e:
                error_msg = str(e)
                if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
                    print(f"\nAPI Rate Limit / Quota Exhausted for {model}.")
                    print("Please wait for your quota to reset or use a new API key.")
                    break
                print(f"Unexpected error with model {model}: {e}")
                break

if __name__ == "__main__":
    question = input("Enter your question: ")
    generate(question)

