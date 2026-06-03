import os

def read_sample_prompt():
    """Reads and displays the sample prompt from the text file."""
    prompt_file = "sample_prompt.txt"
    
    if os.path.exists(prompt_file):
        with open(prompt_file, 'r', encoding='utf-8') as file:
            prompt = file.read()
            print("--- Loaded Sample Prompt ---")
            print(prompt)
            print("----------------------------")
            return prompt
    else:
        print("Error: sample_prompt.txt not found!")
        return None

if __name__ == "__main__":
    read_sample_prompt()
