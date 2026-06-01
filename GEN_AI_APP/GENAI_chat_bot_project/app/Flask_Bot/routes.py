from flask import Blueprint, render_template, request, jsonify
from chatbot import get_response

main = Blueprint("main", __name__)

# Home Page
@main.route("/")
def home():
    return render_template("index.html")

# Chat API
@main.route("/chat", methods=["POST"])
def chat():

    try:
        user_message = request.json["message"]

        print("User:", user_message)

        answer = get_response(user_message)

        print("Bot:", answer)

        return jsonify({
            "response": answer
        })

    except Exception as e:
        error_msg = str(e)
        print("ERROR:", error_msg)
        
        # Check if it's a rate limit error
        if "429" in error_msg or "RESOURCE_EXHAUSTED" in error_msg:
            friendly_response = "You are sending messages too quickly! (API Rate Limit). Please wait about 30 seconds and try again."
        else:
            friendly_response = f"Error: {error_msg}"

        return jsonify({
            "response": friendly_response
        })