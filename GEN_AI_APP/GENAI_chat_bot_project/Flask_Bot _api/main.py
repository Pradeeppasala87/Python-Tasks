from fastapi import FastAPI
from fastapi.middleware.wsgi import WSGIMiddleware
from root import flask_app
import uvicorn

# Initialize the FastAPI application
app = FastAPI(
    title="Bot API",
    description="A joint FastAPI and Flask application",
    version="1.0.0"
)

# Add FastAPI routes
@app.get("/fastapi-route")
def read_fastapi_route():
    return {"message": "Hello from FastAPI!", "status": "active"}

@app.get("/ping")
def ping():
    return {"ping": "pong"}

# Mount the Flask application within FastAPI
# This allows Flask to handle routes not explicitly defined by FastAPI
app.mount("/", WSGIMiddleware(flask_app))

if __name__ == "__main__":
    # Run the ASGI app using uvicorn
    # Make sure you have 'uvicorn' installed: pip install uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
