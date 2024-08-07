from datetime import datetime, timedelta
from record import Record

FORMAT = "%d.%m.%Y"
BD_INTERVAL = 7


def get_congrats_date(record_bd_now: datetime) -> datetime:
    result = record_bd_now
    if record_bd_now.weekday() == 5:
        result = record_bd_now + timedelta(days=2)
    if record_bd_now.weekday() == 6:
        result = record_bd_now + timedelta(days=1)
    return result


def is_bd_in_range(record: Record) -> datetime:
    today = datetime.today()
    record_bd_now = record.birthday.bd_date.replace(year=today.year)
    if record_bd_now < today or record_bd_now > (today + timedelta(days=BD_INTERVAL)):
        record_bd_now = None
    return record_bd_now
