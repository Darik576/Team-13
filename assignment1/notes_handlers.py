def input_error(func):
    def inner(args, notes_book):
        try:
            return func(args, notes_book)
        except ValueError:
            return "Give me valid arguments, please."
        except IndexError:
            return "Not enough arguments provided."
        except KeyError:
            return "Note not found."
    return inner

def sort_notes(notes_book):
    notes = notes_book.sort_by_tags()

    if not notes:
        return "No notes found."

    return "\n".join(str(note) for note in notes)

@input_error
def add_note(args, notes_book):
    text = " ".join(args).strip()
    if not text:
        raise ValueError
    note = notes_book.add_note(text)
    return f"Note added: {note}"


def show_notes(notes_book):
    notes = notes_book.show_all()
    if not notes:
        return "No notes found."
    return "\n".join(str(note) for note in notes)


@input_error
def find_note(args, notes_book):
    query = " ".join(args).strip()
    if not query:
        raise ValueError
    found_notes = notes_book.find_by_text(query)
    if not found_notes:
        return "No matching notes found."
    return "\n".join(str(note) for note in found_notes)


@input_error
def edit_note(args, notes_book):
    note_id = int(args[0])
    new_text = " ".join(args[1:]).strip()
    if not new_text:
        raise ValueError

    success = notes_book.edit_note(note_id, new_text)
    if not success:
        raise KeyError

    return "Note updated."


@input_error
def delete_note(args, notes_book):
    note_id = int(args[0])

    success = notes_book.delete_note(note_id)
    if not success:
        raise KeyError

    return "Note deleted."


@input_error
def add_tag(args, notes_book):
    note_id = int(args[0])
    tag = args[1].strip()

    if not tag:
        raise ValueError

    success = notes_book.add_tag(note_id, tag)
    if not success:
        raise KeyError

    return "Tag added."


@input_error
def remove_tag(args, notes_book):
    note_id = int(args[0])
    tag = args[1].strip()

    if not tag:
        raise ValueError

    success = notes_book.remove_tag(note_id, tag)
    if not success:
        raise KeyError

    return "Tag removed."


@input_error
def find_tag(args, notes_book):
    tag = args[0].strip()
    if not tag:
        raise ValueError

    found_notes = notes_book.find_by_tag(tag)
    if not found_notes:
        return "No notes found with this tag."

    return "\n".join(str(note) for note in found_notes)