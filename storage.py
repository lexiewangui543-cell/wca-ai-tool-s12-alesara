import json
from pathlib import Path
import uuid
from datetime import datetime

SESSIONS_FOLDER = Path("sessions")

def generate_session_id():
    return str(uuid.uuid4())
def create_session(session_name, messages=None, summary=""):
    session_id = generate_session_id()
    session_data = {
        "session_id": session_id,
        "session_name": session_name,
        "date": datetime.now().isoformat(),
        "project": "WCA AI Study Buddy",
        "messages": messages if messages is not None else [],
        "summary": summary
    }
    return session_data
def save_session(session_data):
    SESSIONS_FOLDER.mkdir(parents=True, exist_ok=True)

    file_path = SESSIONS_FOLDER / f"{session_data['session_id']}.json"

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(session_data, file, indent=4)

    return file_path

def load_session(session_id):
    file_path = SESSIONS_FOLDER / f"{session_id}.json"

    with open(file_path, "r", encoding="utf-8") as file:
        session_data = json.load(file)


    return session_data
def list_sessions():
    sessions = []

    if not SESSIONS_FOLDER.exists():
        return sessions

    for file_path in SESSIONS_FOLDER.glob("*.json"):
        with open(file_path, "r", encoding="utf-8") as file:
            session_data = json.load(file)

        sessions.append(session_data)

    return sessions