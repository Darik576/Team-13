import pickle
from pathlib import Path
from .notes import NotesBook

BASE_DIR = Path(__file__).resolve().parent
NOTES_FILE = BASE_DIR / "notes.pkl"


def save_notes(notes_book):
    with open(NOTES_FILE, "wb") as file:
        pickle.dump(notes_book, file)


def load_notes():
    if not NOTES_FILE.exists():
        return NotesBook()

    try:
        with open(NOTES_FILE, "rb") as file:
            notes_book = pickle.load(file)

            if notes_book.data:
                notes_book.next_id = max(notes_book.data.keys()) + 1
            else:
                notes_book.next_id = 1

            return notes_book
    except (FileNotFoundError, EOFError, pickle.UnpicklingError):
        return NotesBook()