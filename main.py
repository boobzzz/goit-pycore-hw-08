from typing import Tuple
from handler import get_response, save_session
from commands import Commands


def parse_input(user_input: str) -> Tuple:
    if not user_input:
        return Commands.INVALID_CMD

    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    print("Welcome to the assistant bot!")
    while True:
        cmd, *args = parse_input(input("Enter a command: "))
        if cmd in [Commands.CLOSE, Commands.EXIT]:
            save_session()
            print(Commands.messages[Commands.EXIT])
            break

        if cmd in Commands.commands:
            get_response(cmd, args)
        else:
            print(Commands.messages[Commands.INVALID_CMD])


if __name__ == "__main__":
    main()
