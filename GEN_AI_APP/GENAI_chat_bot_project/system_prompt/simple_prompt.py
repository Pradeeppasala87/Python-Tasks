import os
from dotenv import load_dotenv

def display_system_config():
    """Loads environment variables and displays the system prompt configuration."""
    
    # Load variables from the .env file
    load_dotenv()
    
    api_key = os.getenv("API_KEY")
    system_prompt = os.getenv("DEFAULT_SYSTEM_PROMPT", "Default prompt: You are a helpful assistant.")
    
    print("====================================")
    print("  System Prompt Configuration Test  ")
    print("====================================")
    
    if not api_key:
        print("[-] Warning: No API_KEY found in environment variables.")
    else:
        print("[+] API_KEY successfully loaded.")
        
    print(f"[+] System Prompt: {system_prompt}")
    print("====================================")

if __name__ == "__main__":
    print("Running system prompt application...\n")
    display_system_config()
    print("\nApplication ran successfully!")
