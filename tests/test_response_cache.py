import unittest
import tempfile
from pathlib import Path

import response_cache


class TestResponseCache(unittest.TestCase):

    def setUp(self):
        # Create a temporary folder for each test
        self.test_directory = tempfile.TemporaryDirectory()

        # Save the original cache file location
        self.original_cache_file = response_cache.CACHE_FILE

        # Redirect cache operations to the temporary folder
        response_cache.CACHE_FILE = (
            Path(self.test_directory.name) / "cache.json"
        )

    def tearDown(self):
        # Restore the original cache location
        response_cache.CACHE_FILE = self.original_cache_file

        # Remove temporary test files
        self.test_directory.cleanup()

    def test_save_and_get_cached_answer(self):
        question = "What is photosynthesis?"
        answer = "Photosynthesis is the process by which plants make food."

        response_cache.save_cached_answer(question, answer)

        result = response_cache.get_cached_answer(question)

        self.assertEqual(result, answer)

    def test_cache_is_case_insensitive(self):
        response_cache.save_cached_answer(
            "What is photosynthesis?",
            "Plants use light energy to make food."
        )

        result = response_cache.get_cached_answer(
            "what is photosynthesis?"
        )

        self.assertEqual(
            result,
            "Plants use light energy to make food."
        )

    def test_cache_handles_extra_spaces(self):
        response_cache.save_cached_answer(
            "What is photosynthesis?",
            "Plants make food using light energy."
        )

        result = response_cache.get_cached_answer(
            "  What   is photosynthesis?  "
        )

        self.assertEqual(
            result,
            "Plants make food using light energy."
        )

    def test_missing_question_returns_none(self):
        result = response_cache.get_cached_answer(
            "What is the human heart?"
        )

        self.assertIsNone(result)

    def test_cache_file_is_created(self):
        response_cache.save_cached_answer(
            "What is an atom?",
            "An atom is the basic unit of an element."
        )

        self.assertTrue(response_cache.CACHE_FILE.exists())

    def test_clear_cache(self):
        response_cache.save_cached_answer(
            "What is DNA?",
            "DNA carries genetic information."
        )

        response_cache.clear_cache()

        self.assertIsNone(
            response_cache.get_cached_answer("What is DNA?")
        )


if __name__ == "__main__":
    unittest.main()