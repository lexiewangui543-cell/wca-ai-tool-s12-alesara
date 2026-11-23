from storage import (
    create_session,
    save_session,
    load_session,
    list_sessions,
    delete_session
)

session = create_session("Mathematics - Algebra")

saved_file = save_session(session)
print("Saved file:", saved_file)

loaded_session = load_session(session["session_id"])
print("Loaded session:", loaded_session)

all_sessions = list_sessions()
print("All saved sessions:", all_sessions)

deleted = delete_session(session["session_id"])
print("Session deleted:", deleted)