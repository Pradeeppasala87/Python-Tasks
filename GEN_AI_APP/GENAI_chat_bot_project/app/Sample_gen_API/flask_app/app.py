from flask import Flask, render_template, request
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

app = Flask(__name__)
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
client = genai.Client(api_key=GEMINI_API_KEY) if GEMINI_API_KEY else None

def generate_gemini_response(prompt: str) -> str:
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        return response.text
    except Exception as exc:
        error_msg = str(exc)
        if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
            return "API Rate Limit / Quota Exhausted. Please wait."
        return f"Error generating response: {error_msg}"


@app.route("/", methods=["GET", "POST"])
def index():
    prompt = ""
    ai_response = ""

    if request.method == "POST":
        prompt = request.form.get("prompt", "").strip()
        if prompt:
            if not client:
                ai_response = "Gemini API key not configured. Set GEMINI_API_KEY in .env."
            else:
                ai_response = generate_gemini_response(prompt)

    return render_template("index.html", prompt=prompt, response=ai_response)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
