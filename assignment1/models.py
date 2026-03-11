from collections import UserDict
from datetime import datetime, date, timedelta
from typing import Optional


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __init__(self, value: str):
        if not value:
            raise ValueError("Phone number cannot be empty.")

        # 1. Очищення: залишаємо лише цифри
        cleaned = "".join(filter(str.isdigit, value))

        # 2. Нормалізація: зведення до формату 0XXXXXXXXX (10 цифр)
        if len(cleaned) == 12 and cleaned.startswith("380"):
            cleaned = cleaned[2:]
        elif len(cleaned) == 11 and cleaned.startswith("80"):
            cleaned = cleaned[1:]

        # 3. Валідація довжини
        if len(cleaned) != 10:
            raise ValueError(f"Invalid phone length: '{value}'. Expected 10 digits.")

        # 4. Валідація коду оператора
        if not cleaned.startswith("0"):
            raise ValueError(
                "Ukrainian phone number must start with '0' (e.g., 095...)."
            )

        super().__init__(cleaned)


class Birthday(Field):
    def __init__(self, value: str):
        try:
            date_obj = datetime.strptime(value, "%d.%m.%Y").date()
            super().__init__(date_obj)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


class Email(Field):
    def __init__(self, value: str):
        # Базова валідація наявності @ та крапки після неї
        if "@" not in value or "." not in value.split("@")[-1]:
            raise ValueError("Invalid email format. Expected: example@mail.com")
        super().__init__(value)


class Address(Field):
    pass


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones: list[Phone] = []
        self.birthday: Optional[Birthday] = None
        self.email: Optional[Email] = None  # Додати цей рядок
        self.address: Optional[Address] = None  # І цей рядок

    def add_phone(self, phone: str) -> None:
        new_phone = Phone(phone)
        if any(p.value == new_phone.value for p in self.phones):
            raise ValueError(f"Phone number {phone} already exists for this contact.")
        self.phones.append(new_phone)

    def remove_phone(self, phone: str) -> None:
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return
        raise ValueError("Phone not found")

    def edit_phone(self, old_phone: str, new_phone: str) -> None:
        for p in self.phones:
            if p.value == old_phone:
                p.value = Phone(new_phone).value
                return
        raise ValueError("Phone not found")

    def find_phone(self, phone: str) -> Optional[str]:
        for p in self.phones:
            if p.value == phone:
                return p.value
        return None

    def add_birthday(self, birthday: str) -> None:
        self.birthday = Birthday(birthday)

    def add_email(self, email: str) -> None:
        self.email = Email(email)

    def add_address(self, address: str) -> None:
        self.address = Address(address)

    def __str__(self) -> str:
        phones_str = "; ".join(p.value for p in self.phones)

        # Перевіряємо наявність атрибутів, щоб не було помилки зі старими даними
        bday = (
            self.birthday.value.strftime("%d.%m.%Y")
            if getattr(self, "birthday", None)
            else "—"
        )
        email_str = self.email.value if getattr(self, "email", None) else "—"
        address_str = self.address.value if getattr(self, "address", None) else "—"

        return (
            f"Contact name: {self.name.value}, phones: {phones_str}, "
            f"birthday: {bday}, email: {email_str}, address: {address_str}"
        )


class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def find(self, name: str) -> Optional[Record]:
        return self.data.get(name)

    def delete(self, name: str) -> None:
        if name in self.data:
            del self.data[name]
        else:
            raise KeyError("Contact not found")

    def get_upcoming_birthdays(self) -> list:
        today = datetime.today().date()
        upcoming = []

        for record in self.data.values():
            if record.birthday is None:
                continue

            birthday: date = record.birthday.value

            try:
                birthday_this_year = birthday.replace(year=today.year)
            except ValueError:
                birthday_this_year = date(today.year, 2, 28)

            if birthday_this_year < today:
                try:
                    birthday_this_year = birthday.replace(year=today.year + 1)
                except ValueError:
                    birthday_this_year = date(today.year + 1, 2, 28)

            delta_days = (birthday_this_year - today).days

            if 0 <= delta_days <= 7:
                congratulation_date = birthday_this_year

                if congratulation_date.weekday() == 5:
                    congratulation_date += timedelta(days=2)
                elif congratulation_date.weekday() == 6:
                    congratulation_date += timedelta(days=1)

                upcoming.append(
                    {
                        "name": record.name.value,
                        "congratulation_date": congratulation_date.strftime("%d.%m.%Y"),
                    }
                )

        return upcoming

    def search(self, query: str) -> list:
        results = []
        for record in self.data.values():
            # Пошук по імені
            if query.lower() in record.name.value.lower():
                results.append(record)
            # Пошук по телефону
            elif any(query in phone.value for phone in record.phones):
                results.append(record)
            # Пошук по дню народження (тільки день і місяць)
            elif record.birthday:
                birthday = record.birthday.value
                # Форматуємо день і місяць (наприклад, 12.03)
                birthday_str = birthday.strftime("%d.%m")
                if query == birthday_str:
                    results.append(record)

        return results
