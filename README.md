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

### 🧠 Intelligent Command Analysis
The assistant features an **Intelligent Command Analyzer** that makes interaction more natural:
- **Intent Recognition:** Understands synonyms (e.g., you can type `create` or `новий` instead of `add`).
- **Fuzzy Matching:** If you make a typo (e.g., `ad-contct`), the bot will suggest the closest correct command.
- **Multilingual Support:** Supports commands and synonyms in both **English** and **Ukrainian**.

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

```
assignment1/
│
├── main.py
├── parser.py
├── models.py
├── handlers.py
├── storage.py
│
├── notes.py
├── notes_handlers.py
├── notes_storage.py
│
└── tests
```

### Modules description

| Module              | Responsibility                             |
| ------------------- | ------------------------------------------ |
| `main.py`           | application entry point and command loop   |
| `parser.py`         | parses user input into command + arguments |
| `models.py`         | core contact data models                   |
| `handlers.py`       | CLI commands for contacts                  |
| `storage.py`        | persistence layer for contacts             |
| `notes.py`          | notes data model                           |
| `notes_handlers.py` | CLI commands for notes                     |
| `notes_storage.py`  | persistence layer for notes                |

---

## Installation

Clone the repository:

```bash
git clone https://github.com/Darik576/Team-13.git
cd Team-13
```

Run the assistant:

```bash
python -m assignment1.main
```

or use RunBot.bat to start the program.

## Usage

After installation, you can start the assistant using one of these methods:
1. **Console Command:** Simply type `assistant-bot` in your terminal.
2. **Python Module:** Run `python -m assignment1.main`.
3. **Desktop Shortcut:** Use the provided `RunBot.bat` file for a quick start on Windows.

Example commands:

### Contacts

```bash
add John 0951234567
add-email John john@mail.com
add-address John Kyiv Khreshchatyk 10
add-birthday John 15.03.1990
search John
all
```

### Notes

```bash
add-note Buy milk
add-tag 1 shopping
add-note Finish Python project
find-note Python
find-tag shopping
sort-notes
show-notes
```

###System Commands

```bash
help
hello
exit
```

---

# Error Handling

The project uses a decorator (input_error) that converts Python exceptions into user-friendly CLI messages.
This improves user experience and prevents program crashes caused by incorrect input.

---

# Team Development Experience

During the development of this project the team practiced:

- collaborative Git workflow
- feature branches
- pull requests
- resolving merge conflicts
- repository cleanup (.gitignore)
- modular architecture design

---

## 📝 Documentation & Standards
- **Code Documentation:** All core functions include **Docstrings** and comments explaining the logic.
- **Packaging:** The project is structured as a Python package with `setup.py` and entry points.
- **PEP8:** The code follows Python styling guidelines for better readability.