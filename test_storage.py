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
print("\n--- TEST 1: Loading a missing session ---")

missing_session = load_session("this-session-does-not-exist")

print("Result:", missing_session)
print("\n--- TEST 2: Deleting a missing session ---")

deleted = delete_session("this-session-does-not-exist")

print("Deletion result:", deleted)
print("\n--- TEST 3: Saving invalid session data ---")

invalid_session = {}

result = save_session(invalid_session)

print("Saving result:", result)
print("\n--- TEST 4: Loading a corrupted JSON file ---")

from pathlib import Path

test_folder = Path("sessions")
test_folder.mkdir(exist_ok=True)

corrupted_file = test_folder / "corrupted_test_session.json"

# Deliberately write invalid JSON
corrupted_file.write_text(
    "{ this is not valid JSON }",
    encoding="utf-8"
)

result = load_session("corrupted_test_session")

print("Loading result:", result)

# Remove the temporary test file
corrupted_file.unlink()