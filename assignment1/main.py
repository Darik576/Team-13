"""
Entry point for the Smart Assistant CLI application.

Initializes data storage and runs the main command loop.
Handles routing of user commands to appropriate handlers.
"""

import difflib
from .models import AddressBook
from .parser import parse_input
from .handlers import (
    add_contact, change_contact, search_contact, show_phone, show_all,
    add_birthday, show_birthday, birthdays, 
    delete_contact, edit_contact_name, show_birthday_after, add_email,
    change_email, add_address, change_address
)
from .storage import save_data, load_data
from .notes_storage import load_notes, save_notes
from .notes_handlers import (
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

INTENTS = {
    "hello": ["hello", "hi", "привіт", "вітаю"],
    "help": ["help", "допомога", "команди", "що ти вмієш"],
    "add": ["add", "new", "create", "додати", "новий", "записати"],
    "change": ["change", "edit", "update", "змінити", "редагувати", "оновити"],
    "phone": ["phone", "number", "номер", "телефон"],
    "all": ["all", "show-all", "всі", "список", "показати-все", "покажи"],
    "search": ["search", "find", "пошук", "знайти"],
    "add-birthday": ["add-birthday", "set-birthday", "додати-день-народження"],
    "birthdays": ["birthdays", "upcoming", "іменинники", "список-днів-народження"],
    "add-note": ["add-note", "new-note", "нотатка", "записка"],
    "exit": ["exit", "close", "quit", "вихід", "бувай", "стоп", "пака"],
    "edit-contact": ["edit-contact", "rename", "перейменувати"],
    "delete-contact": ["delete-contact", "remove-contact", "видалити-контакт"],
    "add-email": ["add-email", "set-email", "пошта", "мейл"],
    "change-email": ["change-email", "edit-email", "оновити-пошту"], 
    "add-address": ["add-address", "set-address", "адреса"],
    "change-address": ["change-address", "edit-address", "оновити-адресу"], 
    "show-birthday-after": ["show-birthday-after", "birthday-after", "через", "днів"],
    "show-notes": ["show-notes", "нотатки", "всі-нотатки"], 
    "find-note": ["find-note", "search-note", "знайти-нотатку"], 
    "edit-note": ["edit-note", "change-note", "редагувати-нотатку"], 
    "delete-note": ["delete-note", "remove-note", "видалити-нотатку"], 
    "add-tag": ["add-tag", "tag", "тег", "додати-тег"], 
    "remove-tag": ["remove-tag", "delete-tag", "видалити-тег"], 
    "find-tag": ["find-tag", "search-tag", "знайти-тег"], 
    "sort-notes": ["sort-notes", "sort", "сортувати", "сортування"], 
}

def show_help() -> str:
    return (
        "\n✨━━━━━━━━━━━━━━━━ SMART ASSISTANT HELP ━━━━━━━━━━━━━━━━✨\n"

        "\n👤 CONTACTS MANAGEMENT\n"
        "  ➕ add [name] [phone]\n"
        "     Додати новий контакт або телефон до існуючого\n"
        "  ✏️ change [name] [old_phone] [new_phone]\n"
        "     Замінити старий номер телефону на новий\n"
        "  📛 edit-contact [old_name] [new_name]\n"
        "     Змінити ім'я існуючого контакту\n"
        "  🗑️ delete-contact [name]\n"
        "     Повністю видалити контакт з книги\n"
        "  🔍 search [query_text]\n"
        "     Пошук за ім'ям, номером, поштою або адресою\n"
        "  📱 all\n"
        "     Показати всі контакти з усіма деталями\n"

        "\n🎂 BIRTHDAYS & INFO\n"
        "  🎂 add-birthday [name] [DD.MM.YYYY]\n"
        "     Встановити або змінити дату народження\n"
        "  🎉 birthdays\n"
        "     Показати іменинників на найближчі 7 днів\n"
        "  🎯 show-birthday-after [number_of_days]\n"
        "     Знайти тих, у кого день народження в наступні X днів\n"
        "  📧 add-email [name] [email]\n"
        "     Додати або змінити email контакту\n"
        "  🏠 add-address [name] [address]\n"
        "     Додати або змінити адресу контакту\n"

        "\n📝 NOTES & TAGS\n"
        "  📓 add-note [text]\n"
        "     Створити нову нотатку\n"
        "  📋 show-notes\n"
        "     Показати всі нотатки\n"
        "  🔎 find-note [text]\n"
        "     Знайти нотатки за текстом\n"
        "  ✏️ edit-note [id] [new_text]\n"
        "     Редагувати текст нотатки\n"
        "  🏷️ add-tag [note_id] [tag]\n"
        "     Додати тег до нотатки\n"
        "  🧹 remove-tag [note_id] [tag]\n"
        "     Видалити тег з нотатки\n"
        "  🔍 find-tag [tag]\n"
        "     Знайти нотатки за тегом\n"
        "  🔃 sort-notes\n"
        "     Відсортувати нотатки за тегами\n"
        "  ❌ delete-note [note_id]\n"
        "     Видалити нотатку\n"

        "\n⚙️ SYSTEM\n"
        "  👋 hello\n"
        "     Привітання від бота\n"
        "  ❓ help\n"
        "     Показати список команд\n"
        "  🚪 exit / close\n"
        "     Зберегти дані та вийти\n"

        "\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
    )


def get_command_from_intent(user_word: str) -> str:
    """Перетворює слово користувача на офіційну команду на основі синонімів."""
    user_word = user_word.lower().strip()
    
    # 1. Перевірка на прямий збіг зі словником синонімів
    for official_command, synonyms in INTENTS.items():
        if user_word in synonyms:
            return official_command
            
    # 2. Якщо прямого збігу немає, використовуємо нечіткий пошук (Fuzzy Matching)
    # Збираємо всі можливі слова (ключі + синоніми) в один список
    flattened_synonyms = [syn for syns in INTENTS.values() for syn in syns]
    matches = difflib.get_close_matches(user_word, flattened_synonyms, n=1, cutoff=0.6)
    
    if matches:
        # Шукаємо, якій офіційній команді належить знайдений синонім
        for official_command, synonyms in INTENTS.items():
            if matches[0] in synonyms:
                return official_command
                
    return user_word # Повертаємо як є, якщо нічого не знайдено


def main() -> None:
    """
    Main entry point for the assistant bot.
    Initializes data, runs the command loop, and provides 
    fuzzy string matching for intelligent command analysis.
    """
    book = load_data()
    notes_book = load_notes()
    print("Welcome to the assistant bot!")
    print("Type 'help' to see available commands.")

    try:
        while True:
            user_input = input("Enter a command: ")
            raw_command, args = parse_input(user_input) # Зберігаємо оригінальне слово

            if not raw_command:
                continue
            
            # Викликаємо інтелектуальний аналізатор
            command = get_command_from_intent(raw_command)

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

            elif command == "add-email":
                print(add_email(args, book))

            elif command == "change-email":
                print(change_email(args, book))

            elif command == "add-address":
                print(add_address(args, book))

            elif command == "change-address":
                print(change_address(args, book))

            else:
                # Якщо команда не потрапила в жоден elif
                print(f"I'm sorry, I don't recognize '{raw_command}'.")
                print("Type 'help' to see what I can do.")

    finally:
        save_data(book)
        save_notes(notes_book)
        print("Address book and notes are saved.")


if __name__ == "__main__":
    main()