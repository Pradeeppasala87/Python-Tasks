from flask import Flask, render_template

flask_app = Flask(__name__)
flask_app.config.from_object('configuration.Config')

@flask_app.route('/')
def home():
    """Render the simple HTML template."""
    return render_template('index.html', title="Flask Bot Home")

@flask_app.route('/flask-api')
def flask_api():
    """A simple API endpoint in Flask."""
    return {"message": "Hello from Flask Bot!"}
