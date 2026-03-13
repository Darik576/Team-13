# Smart Assistant CLI Bot

A **command-line personal assistant** built with Python that helps manage **contacts and notes** in one place.

The assistant allows users to store contacts with phone numbers, email, addresses, and birthdays, as well as create and manage notes with tags for easier organization and searching.

All data is stored locally and automatically restored when the program is restarted.

---

## Project Features

### Contact Management

The assistant supports full contact management functionality.

Users can:

- add new contacts
- add multiple phone numbers
- edit contact information
- delete contacts
- add and update email
- add and update address
- add birthdays
- view upcoming birthdays
- search contacts by:
  - name
  - phone
  - birthday
  - email
  - address

---

### Notes Management

The assistant includes a notes system with tagging support.

Users can:

- create notes
- edit notes
- delete notes
- add tags to notes
- remove tags
- search notes by text
- search notes by tag
- sort notes by tags

---

## Data Persistence

All user data is saved locally using **pickle serialization**.

Two storage files are used:

- `addressbook.pkl` — contacts
- `notes.pkl` — notes

When the application starts, previously saved data is automatically loaded.

---

## Technologies Used

The project demonstrates several core Python concepts:

- Python 3
- Object-Oriented Programming (OOP)
- CLI (Command Line Interface)
- Modular architecture
- Error handling with decorators
- Data persistence with `pickle`
- Git collaborative workflow

---

## Project Architecture

The project follows a modular structure separating responsibilities between different components.
