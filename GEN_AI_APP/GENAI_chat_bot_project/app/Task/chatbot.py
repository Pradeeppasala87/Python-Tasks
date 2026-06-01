import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

with open("project_knowledge.txt", "r", encoding="utf-8") as f:
    PROJECT_DATA = f.read()

def get_response(question):

    prompt = f"""
    You are an AI assistant for a Movie Ticket Booking Project.

    Project Information:
    {PROJECT_DATA}

    Answer only using the project information above.

    User Question:
    {question}
    """

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
            return "API Rate Limit / Quota Exhausted. Please wait."
        return f"Error: {error_msg}"