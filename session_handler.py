from address_book import AddressBook
import pickle
import os

FILENAME = "session_data.pkl"


def save_data(book):
    with open(FILENAME, "wb") as file:
        pickle.dump(book, file)


def load_data() -> AddressBook:
    data: AddressBook = AddressBook()
    if os.path.getsize(FILENAME) > 0:
        try:
            with open(FILENAME, "rb") as file:
                data = pickle.load(file)
        except FileNotFoundError:
            pass
    return data
