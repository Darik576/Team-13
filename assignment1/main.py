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
)

def show_help() -> str:
    return (
        "\n✨ " + "━" * 18 + " SMART ASSISTANT HELP " + "━" * 18 + " ✨\n"
        
        "\n👤 CONTACTS MANAGEMENT\n"
        "  ➕ add [name] [phone]                      • Додати новий контакт або телефон до існуючого\n"
        "  ✏️  change [name] [old_phone] [new_phone]   • Замінити старий номер телефону на новий\n"
        "  📛 edit-contact [old_name] [new_name]      • Змінити ім'я існуючого контакту\n"
        "  🗑️  delete-contact [name]                  • Повністю видалити контакт з книги\n"
        "  🔍 search [query_text]                     • Пошук за ім'ям, номером, поштою або адресою\n"
        "  📱 all                                     • Показати всі контакти з усіма деталями\n"
        
        "\n🎂 BIRTHDAYS & INFO\n"
        "  📅 add-birthday [name] [DD.MM.YYYY]        • Встановити або змінити дату народження\n"
        "  🎈 birthdays                               • Показати іменинників на найближчі 7 днів\n"
        "  🎯 birthday-after [number_of_days]         • Знайти тих, у кого день народження рівно через X днів\n"
        "  📧 add-email [name] [example@mail.com]     • Додати або оновити електронну пошту\n"
        "  🏠 add-address [name] [full_address]       • Додати поштову адресу (можна з пробілами)\n"
        
        "\n📝 NOTES & TAGS\n"
        "  📓 add-note [note_text]                    • Створити нову нотатку з текстом\n"
        "  📋 show-notes                              • Вивести список усіх збережених нотаток\n"
        "  🔎 find-note [search_text]                 • Знайти нотатки, що містять вказаний текст\n"
        "  🏷️  add-tag [note_id] [tag_name]            • Додати ключове слово (тег) до нотатки за її ID\n"
        "  ❌ delete-note [note_id]                   • Видалити нотатку за її унікальним номером\n"
        
        "\n⚙️  SYSTEM\n"
        "  👋 hello                                   • Отримати привітання від бота\n"
        "  ❓ help                                    • Викликати це меню допомоги\n"
        "  🚪 exit / close                            • Зберегти всі зміни у файл та вийти\n"
        
        "\n" + "━" * 60 + "\n"
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