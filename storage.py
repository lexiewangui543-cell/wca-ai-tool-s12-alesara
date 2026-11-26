
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

def get_session_file(session_id):
    """Find a session file using its unique session ID."""

    if not SESSIONS_FOLDER.exists():
        return None

    for file_path in SESSIONS_FOLDER.glob("*.json"):
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                session_data = json.load(file)

            if session_data.get("session_id") == session_id:
                return file_path

        except (json.JSONDecodeError, OSError):
            continue

    return None

def save_session(session_data):
    """Save a study session using a date-based filename."""

    try:
        SESSIONS_FOLDER.mkdir(parents=True, exist_ok=True)

        session_date = datetime.fromisoformat(
            session_data["date"]
        ).strftime("%Y-%m-%d")

        file_path = (
            SESSIONS_FOLDER /
            f"{session_date}_{session_data['session_id']}.json"
        )

        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(session_data, file, indent=4)

        return file_path

    except (OSError, KeyError, TypeError, ValueError) as error:
        print(f"Error saving session: {error}")
        return None

def load_session(session_id):
    """Load a previously saved study session."""

    file_path = get_session_file(session_id)

    if file_path is None:
        print("Session not found.")
        return None

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

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
    """Delete a saved study session using its unique ID."""

    file_path = get_session_file(session_id)

    if file_path is None:
        print("Session not found.")
        return False

    try:
        file_path.unlink()
        return True

    except OSError as error:
        print(f"Error deleting session: {error}")
        return False