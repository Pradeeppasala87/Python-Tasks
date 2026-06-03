import uvicorn
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    # Load environment variables
    load_dotenv()
    
    # Fetch port from environment or default to 8000
    port = int(os.getenv("PORT", 8000))
    
    # Run the application
    # We reference "app:app" meaning the app object inside the app.py module
    print(f"Starting server on port {port}...")
    uvicorn.run("app:app", host="127.0.0.1", port=port, reload=True)
