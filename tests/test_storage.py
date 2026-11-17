import unittest
import tempfile
from pathlib import Path
import storage

from storage import (
    SESSIONS_FOLDER,
    generate_session_id,
    create_session,
    save_session,
    load_session,
    list_sessions,
    delete_session
)
class TestStorage(unittest.TestCase):
    def setUp(self):
        self.test_directory = tempfile.TemporaryDirectory()
        self.original_folder = SESSIONS_FOLDER
        storage.SESSIONS_FOLDER = Path(self.test_directory.name)

    def tearDown(self):
        storage.SESSIONS_FOLDER = self.original_folder
        self.test_directory.cleanup()

    def test_generate_session_id(self):
        session_id = generate_session_id()

        self.assertIsInstance(session_id, str)
        self.assertEqual(len(session_id), 36)
    
    def test_create_session(self):
        session = create_session("Biology Revision")

        self.assertEqual(session["session_name"], "Biology Revision")
        self.assertEqual(session["project"], "WCA AI Study Buddy")
        self.assertIsInstance(session["session_id"], str)
        self.assertEqual(session["messages"], [])
        self.assertEqual(session["summary"], "")
    
    def test_save_and_load_session(self):
        session = create_session("Testing Session")

        save_session(session)

        loaded_session = load_session(session["session_id"])

        self.assertEqual(
            loaded_session["session_name"],
            "Testing Session"
        )

        self.assertEqual(
            loaded_session["session_id"],
            session["session_id"]
        )
    
    def test_list_sessions(self):
        session = create_session("Listing Test")
        save_session(session)

        sessions = list_sessions()

        self.assertIsInstance(sessions, list)
        self.assertTrue(
            any(item["session_id"] == session["session_id"] for item in sessions)
        )
    def test_delete_session(self):
        session = create_session("Deletion Test")
        save_session(session)

        result = delete_session(session["session_id"])

        self.assertTrue(result)
        self.assertIsNone(load_session(session["session_id"]))

    def test_load_missing_session(self):
        result = load_session("nonexistent-session")

        self.assertIsNone(result)

    def test_load_corrupted_session(self):
        file_path = storage.SESSIONS_FOLDER / "broken.json"
        file_path.write_text("{invalid json}", encoding="utf-8")

        result = load_session("broken")

        self.assertIsNone(result)