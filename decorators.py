from functools import wraps


def input_error(func):
    @wraps(func)
    def inner(*args):
        try:
            return func(*args)
        except Exception as e:
            print(f"{type(e)}: {e}")

    return inner


def show_message(func):
    @wraps(func)
    def inner(*args):
        message = func(*args)
        print(message)

    return inner
