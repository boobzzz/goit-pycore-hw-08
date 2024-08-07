from datetime import datetime
from field import Field

FORMAT = "%d.%m.%Y"


class Birthday(Field):
    def __init__(self, value: str):
        try:
            super().__init__(value)
            self.__bd_date = datetime.strptime(value, FORMAT)
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    @property
    def bd_date(self) -> datetime:
        return self.__bd_date
