from notes import NotesBook
from notes_storage import save_notes, load_notes

notes = NotesBook()
notes.add_note("Buy milk")
notes.add_note("Finish Python project", ["study"])

save_notes(notes)

loaded_notes = load_notes()

print("Loaded notes:")
for note in loaded_notes.show_all():
    print(note)

new_note = loaded_notes.add_note("Call dentist")
print("\nAfter adding one more:")
for note in loaded_notes.show_all():
    print(note)