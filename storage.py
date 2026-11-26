
import json
from pathlib import Path
import uuid
from datetime import datetime


# Folder where study sessions will be stored
SESSIONS_FOLDER = Path("sessions")


def generate_session_id():
    """Generate a unique ID for every study session."""
    return str(uuid.uuid4())


def create_session(session_name, messages=None, summary=""):
    """Create a new study session."""

    session_data = {
        "session_id": generate_session_id(),
        "session_name": session_name,
        "date": datetime.now().isoformat(),
        "project": "WCA AI Study Buddy",
        "messages": messages if messages is not None else [],
        "summary": summary
    }

    return session_data


def save_session(session_data):
    """Save a study session as a JSON file."""

    try:
        SESSIONS_FOLDER.mkdir(parents=True, exist_ok=True)

        file_path = SESSIONS_FOLDER / f"{session_data['session_id']}.json"

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(session_data, file, indent=4)

        return file_path

    except (OSError, KeyError, TypeError) as error:
        print(f"Error saving session: {error}")
        return None


def load_session(session_id):
    """Load a previously saved study session."""

    file_path = SESSIONS_FOLDER / f"{session_id}.json"

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print("Session not found.")
        return None

    except json.JSONDecodeError:
        print("Error: The session file contains invalid JSON.")
        return None

    except OSError as error:
        print(f"Error loading session: {error}")
        return None


def list_sessions():
    """Return all saved study sessions."""

    sessions = []

    if not SESSIONS_FOLDER.exists():
        return sessions

    for file_path in SESSIONS_FOLDER.glob("*.json"):

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                session_data = json.load(file)

            sessions.append(session_data)

        except json.JSONDecodeError:
            print(f"Invalid session file: {file_path}")

        except OSError as error:
            print(f"Could not read {file_path}: {error}")

    return sessions


def delete_session(session_id):
    """Delete a saved study session."""

    file_path = SESSIONS_FOLDER / f"{session_id}.json"

    try:
        if file_path.exists():
            file_path.unlink()
            return True

        print("Session not found.")
        return False

    except OSError as error:
        print(f"Error deleting session: {error}")
        return False
