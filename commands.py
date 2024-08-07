class Commands:
    ADD = "add"
    CHANGE = "change"
    DELETE = "delete"
    PHONE = "phone"
    ALL = "all"
    ADD_BD = "add-birthday"
    SHOW_BD = "show-birthday"
    HELLO = "hello"
    CLOSE = "close"
    EXIT = "exit"
    INVALID_CMD = "invalid-command"
    INVALID_PHONE = "invalid-phone"
    PHONE_EXISTS = "phone-exists"
    PHONE_NOT_FOUND = "phone-not-found"
    NOT_FOUND = "not-found"
    EMPTY = "empty"

    commands = [ADD, CHANGE, DELETE, PHONE, ALL, ADD_BD, SHOW_BD, HELLO, CLOSE, EXIT]

    messages = {
        HELLO: "How can I help you?",
        ADD: "Record added successfully",
        CHANGE: "Record updated successfully",
        DELETE: "Record deleted successfully",
        EXIT: "Good bye!",
        INVALID_CMD: "Invalid command."
    }

    errors = {
        NOT_FOUND: "Record was not found",
        EMPTY: "Address book is empty",
        INVALID_PHONE: "Invalid phone format",
        PHONE_EXISTS: "Phone already exists",
        PHONE_NOT_FOUND: "Phone was not found"
    }
