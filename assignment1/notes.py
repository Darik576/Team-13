from collections import UserDict


class Note:
    def __init__(self, note_id: int, text: str, tags=None):
        self.id = note_id
        self.text = text
        self.tags = tags if tags else []

    def edit_text(self, new_text: str):
        self.text = new_text

    def add_tag(self, tag: str):
        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag: str):
        if tag in self.tags:
            self.tags.remove(tag)

    def matches_text(self, query: str) -> bool:
        return query.lower() in self.text.lower()

    def matches_tag(self, tag: str) -> bool:
        return tag.lower() in [t.lower() for t in self.tags]

    def __str__(self):
        tags_str = f" | Tags: {', '.join(self.tags)}" if self.tags else ""
        return f"{self.id}: {self.text}{tags_str}"


class NotesBook(UserDict):
    def __init__(self):
        super().__init__()
        self.next_id = 1

    def add_note(self, text: str, tags=None):
        note = Note(self.next_id, text, tags)
        self.data[self.next_id] = note
        self.next_id += 1
        return note

    def find_by_id(self, note_id: int):
        return self.data.get(note_id)

    def delete_note(self, note_id: int):
        if note_id in self.data:
            del self.data[note_id]
            return True
        return False

    def edit_note(self, note_id: int, new_text: str):
        note = self.find_by_id(note_id)
        if note:
            note.edit_text(new_text)
            return True
        return False

    def add_tag(self, note_id: int, tag: str):
        note = self.find_by_id(note_id)
        if note:
            note.add_tag(tag)
            return True
        return False

    def remove_tag(self, note_id: int, tag: str):
        note = self.find_by_id(note_id)
        if note:
            note.remove_tag(tag)
            return True
        return False

    def find_by_text(self, query: str):
        return [note for note in self.data.values() if note.matches_text(query)]

    def find_by_tag(self, tag: str):
        return [note for note in self.data.values() if note.matches_tag(tag)]

    def sort_by_tags(self):
        return sorted(
            self.data.values(),
            key=lambda note: ",".join(sorted(note.tags)) if note.tags else ""
        )

    def show_all(self):
        return list(self.data.values())