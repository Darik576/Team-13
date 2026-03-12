from models import Record, AddressBook
from typing import List, Optional


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return str(e)
        except IndexError:
            return "Enter the argument for the command."
        except KeyError:
            return "Contact not found."
        except Exception as e:
            return f"Unexpected error: {e}"

    return inner


@input_error
def add_contact(args: List[str], book: AddressBook) -> str:
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."

    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."

    record.add_phone(phone)
    return message


@input_error
def change_contact(args: List[str], book: AddressBook) -> str:
    name, old_phone, new_phone = args
    record = book.find(name)
    if record is None:
        raise KeyError
    record.edit_phone(old_phone, new_phone)
    return "Contact updated."


@input_error
def show_phone(args: List[str], book: AddressBook) -> str:
    name = args[0]
    record = book.find(name)
    if record is None:
        raise KeyError
    return "; ".join(p.value for p in record.phones)


@input_error
def show_all(book: AddressBook) -> str:
    if not book.data:
        return "No contacts saved."
    return "\n".join(str(record) for record in book.data.values())


@input_error
def add_birthday(args: List[str], book: AddressBook) -> str:
    name, birthday = args
    record = book.find(name)
    if record is None:
        raise KeyError

    # Перевіряємо, чи це нове додавання чи оновлення
    message = "Birthday updated." if record.birthday else "Birthday added."

    record.add_birthday(birthday)
    return message


@input_error
def show_birthday(args: List[str], book: AddressBook) -> str:
    name = args[0]
    record = book.find(name)
    if record is None:
        raise KeyError
    if record.birthday is None:
        return "Birthday not set."
    return record.birthday.value.strftime("%d.%m.%Y")


@input_error
def birthdays(args: List[str], book: AddressBook) -> str:
    upcoming = book.get_upcoming_birthdays()
    if not upcoming:
        return "No birthdays in the next 7 days."
    return "\n".join(f"{u['name']} -> {u['congratulation_date']}" for u in upcoming)


@input_error
def search_contact(args: List[str], book: AddressBook) -> str:
    if not args:
        return "Enter search query."
    
    query = args[0]
    results = book.search(query)

    if not results:
        return "No matching contacts found."
    
    # Виводимо кожен знайдений рекорд з нового рядка
    return "\n".join(str(record) for record in results)


@input_error
def delete_contact(args: List[str], book: AddressBook) -> str:
    name = args[0]
    book.delete(name)
    return f"Contact {name} deleted."


@input_error
def edit_contact_name(args: List[str], book: AddressBook) -> str:
    old_name, new_name = args
    record = book.find(old_name)
    if record is None:
        raise KeyError

    # Створюємо новий запис з новим ім'ям, але старими даними
    new_record = Record(new_name)
    new_record.phones = record.phones
    new_record.birthday = record.birthday

    book.add_record(new_record)
    book.delete(old_name)
    return f"Contact {old_name} renamed to {new_name}."

@input_error
def show_birthday_after(args: List[str], book: AddressBook) -> str:
    if not args:
        raise ValueError("Please provide the number of days. Usage: birthday-after [days]")
    
    try:
        days = int(args[0])
    except ValueError:
        return "Days must be a number."

    # Викликаємо метод, який ми раніше додали в models.py
    contacts = book.get_birthdays_exactly_in_days(days)
    
    if not contacts:
        # Ваша умова: виводити конкретне повідомлення, якщо нікого не знайдено
        return f"No birthdays in {days} days"
    
    result = [f"Birthdays in {days} days:"]
    for record in contacts:
        result.append(str(record))
        
    return "\n".join(result)