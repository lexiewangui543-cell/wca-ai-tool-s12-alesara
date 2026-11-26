
from ai_client import get_study_buddy_response

# Start a new conversation
conversation_history = [
    {
        "role": "user",
        "content": (
            "My name is Samuel. "
            "I want to study Mathematics, "
            "specifically Algebra. "
            "Please start my study session "
            "by asking one question."
        )
    }
]

# Send the request to the AI
try:

    result = get_study_buddy_response(conversation_history)

    print("\nAI RESPONSE")
    print("-" * 40)

    print(result)

except Exception as error:

    print("\nAI INTEGRATION FAILED")
    print(error)