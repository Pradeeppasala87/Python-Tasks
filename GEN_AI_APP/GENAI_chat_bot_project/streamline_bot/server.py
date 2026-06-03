import uvicorn
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    # Load environment settings
    load_dotenv()
    
    # Get host and port from environment or use sensible defaults
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", 8080))
    
    print(f"Starting Streamline Bot Server on http://{host}:{port}...")
    
    # Start the application. 'app:app' means the app object within app.py
    uvicorn.run("app:app", host=host, port=port, reload=True)
