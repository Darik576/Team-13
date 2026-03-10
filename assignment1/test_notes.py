from notes import NotesBook

notes = NotesBook()

# add notes
n1 = notes.add_note("Buy milk")
n2 = notes.add_note("Finish Python project", ["study"])

print("All notes:")
for note in notes.show_all():
    print(note)

print("\nSearch 'milk':")
for note in notes.find_by_text("milk"):
    print(note)

print("\nEdit note 1:")
notes.edit_note(1, "Buy milk and bread")
print(notes.find_by_id(1))

print("\nAdd tag:")
notes.add_tag(1, "shopping")
print(notes.find_by_id(1))

print("\nFind by tag 'study':")
for note in notes.find_by_tag("study"):
    print(note)

print("\nDelete note 1:")
notes.delete_note(1)

print("\nRemaining notes:")
for note in notes.show_all():
    print(note)