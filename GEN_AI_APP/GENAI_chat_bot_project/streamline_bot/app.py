from fastapi import FastAPI

# Initialize the streamline FastAPI application
app = FastAPI(title="Streamline Bot API")

@app.get("/")
def read_root():
    """A clean, streamlined home endpoint."""
    return {"message": "Streamline Bot is up and running!", "status": "success"}

@app.get("/bot/info")
def bot_info():
    """Endpoint providing bot metadata."""
    return {"bot_name": "StreamlineBot", "version": "1.0", "description": "A lightweight bot API"}
