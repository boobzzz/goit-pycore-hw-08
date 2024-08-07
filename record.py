from name import Name
from phone import Phone, PhoneData
from commands import Commands
from birthday import Birthday


class Record:
    def __init__(self, name: str):
        self.__name = Name(name)
        self.__phones = []
        self.__birthday = None

    def __str__(self):
        return (f"Contact name: {self.__name.value}, phones: {'; '.join(p.value for p in self.__phones)}, "
                f"birthday: {self.__birthday.value if self.__birthday else "none"}")

    @property
    def name(self):
        return self.__name

    @property
    def phones(self):
        return self.__phones

    @property
    def birthday(self):
        return self.__birthday

    def add_phone(self, phone: str) -> str:
        new_phone = Phone(phone)
        if not new_phone.value:
            return Commands.errors.get(Commands.INVALID_PHONE)

        if not self.find_phone(new_phone):
            self.__phones.append(new_phone)
        else:
            return Commands.errors.get(Commands.PHONE_EXISTS)

    def edit_phone(self, current: str, new: str) -> str:
        found_phone = self.find_phone(Phone(current))
        if not found_phone:
            return Commands.errors.get(Commands.PHONE_NOT_FOUND)

        new_phone = Phone(new)
        if found_phone["phone"].value == new_phone.value:
            return Commands.errors.get(Commands.PHONE_EXISTS)

        self.__phones[found_phone["index"]] = new_phone

    def remove_phone(self, phone: str) -> str:
        found_phone = self.find_phone(Phone(phone))
        if not found_phone:
            return Commands.errors.get(Commands.PHONE_NOT_FOUND)

        self.__phones.pop(found_phone["index"])

    def find_phone(self, phone: Phone) -> PhoneData:
        values = [p.value for p in self.__phones]
        found = None
        if phone.value in values:
            found = {
                "phone": phone,
                "index": values.index(phone.value)
            }
        return found

    def add_birthday(self, date: str):
        self.__birthday = Birthday(date)
