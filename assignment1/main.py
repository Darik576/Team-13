from models import AddressBook
from parser import parse_input
from handlers import (
    add_contact, change_contact, search_contact, show_phone, show_all,
    add_birthday, show_birthday, birthdays, 
    delete_contact, edit_contact_name, show_birthday_after
)
from storage import save_data, load_data
from notes_storage import load_notes, save_notes
from notes_handlers import (
    add_note,
    show_notes,
    find_note,
    edit_note,
    delete_note,
    add_tag,
    remove_tag,
    find_tag,
    sort_notes,
)

def show_help() -> str:
    return (
        "Available commands:\n"
        "--- General ---\n"
        "hello           - show greeting\n"
        "help            - show this list of commands\n"
        "exit / close    - save data and exit\n"
        "--- Contacts ---\n"
        "add name phone             - add new contact or add phone to existing\n"
        "change name old_phone new_phone - change existing phone number\n"
        "edit-contact old_name new_name - rename a contact\n"
        "delete-contact name        - remove a contact from the book\n"
        "phone name                 - show all phone numbers for contact\n"
        "all                        - show all contacts with all details\n"
        "search query               - search by name, phone, email, address, or birthday\n"
        "--- Details ---\n"
        "add-birthday name DD.MM.YYYY - set or change birthday\n"
        "show-birthday name           - show contact's birthday\n"
        "birthdays                    - show birthdays in the next 7 days\n"
        "add-email name email         - add email to contact\n"
        "change-email name email      - update contact's email\n"
        "add-address name address     - add address (can include spaces)\n"
        "change-address name address  - update contact's address\n"
        "--- Notes ---\n"
        "add-note text                - add a new note\n"
        "show-notes                   - show all notes\n"
        "find-note query              - search notes by text\n"
        "edit-note id new_text        - edit note text\n"
        "delete-note id               - delete note\n"
        "add-tag id tag               - add tag to note\n"
        "remove-tag id tag            - remove tag from note\n"
        "sort-notes                   - sort notes by tags\n"
        "find-tag tag                 - search notes by tag"
    )


def main() -> None:
    book = load_data()
    notes_book = load_notes()
    print("Welcome to the assistant bot!")
    print("Type 'help' to see available commands.")

    try:
        while True:
            user_input = input("Enter a command: ")
            command, args = parse_input(user_input)

            if command in ["close", "exit"]:
                save_data(book)
                save_notes(notes_book)
                print("Good bye!")
                break

            elif command == "hello":
                print("How can I help you?")

            elif command == "add":
                print(add_contact(args, book))

            elif command == "change":
                print(change_contact(args, book))

            elif command == "phone":
                print(show_phone(args, book))

            elif command == "all":
                print(show_all(book))

            elif command == "help":
                print(show_help())

            elif command == "add-birthday":
                print(add_birthday(args, book))

            elif command == "show-birthday":
                print(show_birthday(args, book))

            elif command == "birthdays":
                print(birthdays(args, book))

            elif command == "search":
                print(search_contact(args, book))

            elif command == "add-note":
                print(add_note(args, notes_book))

            elif command == "show-notes":
                print(show_notes(notes_book))

            elif command == "find-note":
                print(find_note(args, notes_book))

            elif command == "edit-note":
                print(edit_note(args, notes_book))

            elif command == "delete-note":
                print(delete_note(args, notes_book))

            elif command == "add-tag":
                print(add_tag(args, notes_book))

            elif command == "remove-tag":
                print(remove_tag(args, notes_book))

            elif command == "find-tag":
                print(find_tag(args, notes_book))

            elif command == "sort-notes":
                print(sort_notes(notes_book))

            elif command == "delete-contact":
                if not args:
                    print("Error: Enter contact name.")
                    continue
                
                name = args[0]
                confirm = input(f"Are you sure you want to delete contact '{name}'? (y/n): ").lower()
                
                if confirm in ["y", "yes"]:
                    print(delete_contact(args, book))
                else:
                    print("Deletion cancelled.")

            elif command == "edit-contact":
                print(edit_contact_name(args, book))

            elif command == "show-birthday-after":
                print(show_birthday_after(args, book))

            else:
                print("Invalid command.")            
    finally:
        save_data(book)
        save_notes(notes_book)
        print("Address book and notes are saved.")


if __name__ == "__main__":
    main()