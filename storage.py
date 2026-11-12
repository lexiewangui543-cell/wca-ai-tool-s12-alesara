import uuid
from datetime import datetime
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
