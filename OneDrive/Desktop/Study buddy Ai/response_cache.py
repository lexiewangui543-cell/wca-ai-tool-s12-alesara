
import json
from pathlib import Path


# Location of the cache file
CACHE_FILE = Path(__file__).parent / "cache.json"


def normalize_question(question):
    """
    Standardizes a question so that small differences
    in capitalization and spacing do not create duplicate entries.
    """
    return " ".join(question.lower().split())


def load_cache():
    """
    Loads previously cached responses.
    Returns an empty dictionary if the cache does not exist
    or contains invalid JSON.
    """
    if not CACHE_FILE.exists():
        return {}

    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as file:
            cache_data = json.load(file)

        if isinstance(cache_data, dict):
            return cache_data

        return {}

    except (json.JSONDecodeError, OSError):
        return {}


def get_cached_answer(question):
    """
    Checks whether an answer to the question is already cached.
    Returns the cached answer if found, otherwise returns None.
    """
    cache = load_cache()
    question_key = normalize_question(question)

    cached_response = cache.get(question_key)

    if isinstance(cached_response, dict):
        return cached_response.get("answer")

    return None


def save_cached_answer(question, answer):
    """
    Saves a question and its AI-generated answer
    to the cache file.
    """
    cache = load_cache()
    question_key = normalize_question(question)

    cache[question_key] = {
        "question": question.strip(),
        "answer": answer
    }

    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(CACHE_FILE, "w", encoding="utf-8") as file:
        json.dump(cache, file, indent=4, ensure_ascii=False)


def clear_cache():
    """
    Removes all cached responses.
    """
    if CACHE_FILE.exists():
        CACHE_FILE.unlink()
