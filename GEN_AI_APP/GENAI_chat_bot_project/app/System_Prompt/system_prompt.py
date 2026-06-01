SYSTEM_PROMPT = """You are an AI learning assistant.
Respond only to Python, FastAPI, Flask, APIs, AI/ML, and Software Development questions.
Reject unrelated questions politely."""

def test_system_prompt():
    """Test that the system prompt contains expected keywords."""
    assert "Python" in SYSTEM_PROMPT
    assert "FastAPI" in SYSTEM_PROMPT
    print("System_Prompt system_prompt tests passed!")

if __name__ == "__main__":
    test_system_prompt()