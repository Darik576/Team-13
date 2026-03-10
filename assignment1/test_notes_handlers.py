from notes import NotesBook
from notes_handlers import (
    add_note,
    show_notes,
    find_note,
    edit_note,
    delete_note,
    add_tag,
    remove_tag,
    find_tag,
)

notes_book = NotesBook()

print(add_note(["Buy", "milk"], notes_book))
print(add_note(["Finish", "project"], notes_book))
print(show_notes(notes_book))

print(find_note(["milk"], notes_book))
print(edit_note(["1", "Buy", "milk", "and", "bread"], notes_book))
print(add_tag(["1", "shopping"], notes_book))
print(find_tag(["shopping"], notes_book))
print(delete_note(["2"], notes_book))
print(show_notes(notes_book))