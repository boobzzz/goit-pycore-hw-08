from collections import UserDict
from record import Record


class AddressBook(UserDict):
    def __str__(self):
        records = ""
        for name in self:
            records += f"{self[name]}\n"
        return records

    def add_record(self, name: str):
        self[name] = Record(name)

    def delete_record(self, name: str):
        self.pop(name)

    def find_record(self, name: str) -> Record:
        record = None
        if name in self:
            record = self[name]
        return record
