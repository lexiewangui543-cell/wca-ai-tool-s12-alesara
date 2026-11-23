import os
from dotenv import load_dotenv
from openai import OpenAI
# Load environment variables from .env
load_dotenv()

def create_client():
    """
    Create a connection to the OpenAI API.
    """
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError("OpenAI API key not found. Check your .env file.")

    client = OpenAI(api_key=api_key)
    return client


def get_ai_response(prompt, instructions=None):
    """
    Send a prompt to OpenAI and return its response.
    """

    client = create_client()

    response = client.responses.create(
        model=os.getenv("OPENAI_MODEL", "gpt-5.5"),
        instructions=instructions,
        input=prompt
    )

    return response.output_text