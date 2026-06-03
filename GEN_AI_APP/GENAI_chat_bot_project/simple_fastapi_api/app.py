from fastapi import FastAPI
import os
from dotenv import load_dotenv
from typing import Optional

# Load environment variables from the .env file
load_dotenv()

# Get the app name from environment variables or use a default
app_name = os.getenv("APP_NAME", "My FastAPI App")

# Initialize the FastAPI app
app = FastAPI(title=app_name, description="A simple FastAPI application")

@app.get("/")
def read_root():
    """Root endpoint to check if the API is running."""
    return {"message": f"Welcome to {app_name}!", "status": "ok"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    """Retrieve an item by its ID with an optional query parameter."""
    return {"item_id": item_id, "query_param": q}

@app.post("/items/")
def create_item(name: str, price: float):
    """Create a new item."""
    return {"name": name, "price": price, "message": "Item created successfully"}
