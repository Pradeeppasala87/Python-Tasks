from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
from database import init_db

app = FastAPI(title="Employee Management System API")

# Determine paths dynamically so server/app.py can find client/ folders
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CLIENT_DIR = os.path.join(BASE_DIR, "client")
STATIC_DIR = os.path.join(CLIENT_DIR, "static")
TEMPLATES_DIR = os.path.join(CLIENT_DIR, "templates")

# Initialize Jinja2 Templates
templates = Jinja2Templates(directory=TEMPLATES_DIR)

# Initialize database on startup
@app.on_event("startup")
def startup_event():
    init_db()

# Mount static files
if os.path.exists(STATIC_DIR):
    app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Serve the frontend web UI."""
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/health")
def health_check():
    """A simple health check endpoint for the system."""
    return {"status": "Database and Server are running perfectly!"}
