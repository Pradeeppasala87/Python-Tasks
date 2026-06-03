import os
from flask import Flask, jsonify
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    """Root endpoint for the Flask Bot API."""
    return jsonify({
        "message": "Welcome to the Sample Flask Bot API",
        "status": "success",
        "code": 200
    })

@app.route('/api/bot/info', methods=['GET'])
def bot_info():
    """An endpoint providing bot metadata."""
    return jsonify({
        "name": "SampleFlaskBot",
        "version": "1.0.0",
        "description": "A clean, streamlined Flask API setup."
    })

@app.route('/api/ping', methods=['GET'])
def ping():
    """A simple ping-pong endpoint to test connectivity."""
    return jsonify({"ping": "pong"})

if __name__ == '__main__':
    port = int(os.getenv("PORT", 5000))
    debug_mode = os.getenv("FLASK_DEBUG", "1") == "1"
    app.run(host='127.0.0.1', port=port, debug=debug_mode)
