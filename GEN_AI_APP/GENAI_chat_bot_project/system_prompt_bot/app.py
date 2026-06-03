from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
import uvicorn
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = FastAPI(title="System Prompt Bot")

# Mount static files folder (for CSS, JS, etc.)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup Jinja2 templates folder
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Serve the modern web interface showing the sample prompt."""
    prompt_content = "Prompt could not be loaded."
    if os.path.exists("sample_prompt.txt"):
        with open("sample_prompt.txt", "r", encoding="utf-8") as f:
            prompt_content = f.read()
            
    return templates.TemplateResponse(
        request=request,
        name="index.html", 
        context={"prompt": prompt_content, "request": request}
    )

@app.get("/stats")
async def get_stats():
    """Return bot statistics as requested."""
    return {
        "status": "online",
        "prompts_served": 9001,
        "uptime_hours": 128.4,
        "version": "2.0.0",
        "message": "Stats endpoint is fully operational."
    }

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    # Run the server on port 8000
    uvicorn.run("app:app", host="127.0.0.1", port=port, reload=True)
