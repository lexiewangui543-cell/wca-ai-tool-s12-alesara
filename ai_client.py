

# STUDY BUDDY - AI STUDY ASSISTANT
# Member 2: AI Integration and JSON Validation
# File: ai_client.py

import os
import json

from dotenv import load_dotenv
from openai import OpenAI

from prompts import SYSTEM_PROMPT, SUMMARY_PROMPT


# STEP 1: Load environment variables

load_dotenv(override=True)

MODEL_NAME = os.getenv("OPENAI_MODEL", "gpt-4o-mini")


# STEP 2: Connect to OpenAI


def get_openai_client():

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        raise ValueError(
            "OpenAI API key is missing. "
            "Check your .env file."
        )

    return OpenAI(api_key=api_key)


# STEP 3: Validate study responses

def validate_study_response(data):

    if not isinstance(data, dict):
        raise ValueError("Response must be a JSON object.")

    response_type = data.get("type")

    if response_type == "question":

        required_fields = [
            "subject",
            "topic",
            "question",
            "expected_answer",
            "next_action"
        ]

        for field in required_fields:
            if not isinstance(data.get(field), str) or not data[field].strip():
                raise ValueError(f"Missing or empty field: {field}")

    elif response_type == "evaluation":

        required_fields = [
            "learner_answer",
            "feedback",
            "explanation",
            "next_action"
        ]

        for field in required_fields:
            if not isinstance(data.get(field), str) or not data[field].strip():
                raise ValueError(f"Missing or empty field: {field}")

        if not isinstance(data.get("is_correct"), bool):
            raise ValueError("is_correct must be true or false.")

        if not isinstance(data.get("score"), (int, float)):
            raise ValueError("score must be a number.")

        if not isinstance(data.get("max_score"), (int, float)):
            raise ValueError("max_score must be a number.")

        if data["score"] < 0 or data["score"] > data["max_score"]:
            raise ValueError("Invalid score.")

    else:
        raise ValueError("Unknown response type.")

    return True


# STEP 4: Validate summary responses

def validate_summary(data):

    if not isinstance(data, dict):
        raise ValueError("Summary must be a JSON object.")

    required_fields = [
        "type",
        "subject",
        "topic",
        "total_questions",
        "correct_answers",
        "score_percentage",
        "strengths",
        "topics_to_revise",
        "incorrect_questions",
        "recommendations",
        "overall_feedback"
    ]

    for field in required_fields:

        if field not in data:
            raise ValueError(f"Missing summary field: {field}")

    if data["type"] != "summary":
        raise ValueError("Invalid summary type.")

    for field in ["subject", "topic", "overall_feedback"]:

        if not isinstance(data[field], str) or not data[field].strip():
            raise ValueError(f"Empty summary field: {field}")

    for field in [
        "strengths",
        "topics_to_revise",
        "incorrect_questions",
        "recommendations"
    ]:

        if not isinstance(data[field], list):
            raise ValueError(f"{field} must be a list.")

        if not data[field] or not all(
            isinstance(item, str) and item.strip()
            for item in data[field]
        ):
            raise ValueError(f"{field} cannot be empty.")

    if not isinstance(data["total_questions"], int):
        raise ValueError("total_questions must be an integer.")

    if not isinstance(data["correct_answers"], int):
        raise ValueError("correct_answers must be an integer.")

    if not isinstance(data["score_percentage"], (int, float)):
        raise ValueError("score_percentage must be a number.")

    if not 0 <= data["correct_answers"] <= data["total_questions"]:
        raise ValueError("Invalid question totals.")

    if not 0 <= data["score_percentage"] <= 100:
        raise ValueError("Invalid score percentage.")

    return True


# STEP 5: Send request and retry invalid JSON



def request_json(instructions, conversation_history, validator):

    client = get_openai_client()

    for attempt in range(2):

        try:

            # Add an instruction requiring JSON output
            api_input = conversation_history + [
                {
                    "role": "user",
                    "content": (
                        "IMPORTANT: Return your complete response "
                        "as valid JSON only. Follow the required "
                        "JSON structure and include all required fields."
                    )
                }
            ]

            # Send the request to OpenAI
            response = client.responses.create(
                model=MODEL_NAME,
                instructions=instructions,
                input=api_input,
                text={
                    "format": {
                        "type": "json_object"
                    }
                },
                max_output_tokens=1200
            )

            # Extract AI response
            response_text = response.output_text

            # Convert JSON text into Python dictionary
            data = json.loads(response_text)

            # Validate the response
            validator(data)

            return data

        except (json.JSONDecodeError, ValueError) as error:

            if attempt == 0:

                print("Invalid AI response. Retrying once...")

                conversation_history = conversation_history + [
                    {
                        "role": "user",
                        "content": (
                            "Your previous response was invalid: "
                            + str(error)
                            + ". Return corrected valid JSON."
                        )
                    }
                ]

            else:

                raise ValueError(
                    "The AI returned an invalid response twice."
                ) from error

    raise ValueError("Unable to obtain a valid AI response.")

# --------------------------------------------
# STEP 6: Generate study questions and feedback
# --------------------------------------------

def get_study_buddy_response(conversation_history):

    return request_json(
        SYSTEM_PROMPT,
        conversation_history,
        validate_study_response
    )


# STEP 7: Generate the final study summary

def generate_session_summary(conversation_history):

    return request_json(
        SUMMARY_PROMPT,
        conversation_history,
        validate_summary
    )
