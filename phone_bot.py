import re

contacts = {}


def input_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)

        except KeyError as e:
            return f"Error: {e}"
        except ValueError as e:
            return f"Error: {e}"
        except NameError as e:
            return f"Error: {e}"

    return wrapper


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args, contacts):
    if len(args) < 2:
        raise KeyError("You need to provide a name and a phone number. Please retry.")
    name, phone = args

    pattern = r"^\+?\d[\d\s\-()]*\d$"
    if not re.match(pattern, phone):
        raise ValueError(
            f"Incorrect phone number format for contact {name}. Please retry."
        )

    contacts[name] = phone

    return f"Contact {name} added with the phone number {phone}."


@input_error
def change_contact(args, contacts):
    if len(args) < 2:
        raise KeyError(f"You need to provide a name and a new phone number.")
    name, phone = args

    if name in contacts:
        contacts[name] = phone
        pattern = r"^\+?\d[\d\s\-()]*\d$"
        if not re.match(pattern, phone):
            raise ValueError(
                f"Incorrect phone number format for contact {name}. Please retry."
            )
        return f"Contact {name} updated with the phone number {phone}."

    raise NameError(
        f"Contact {name} not found in your contact list. Please create contact {name}, or check the name you wanna change."
    )


@input_error
def get_phone(args, contacts):
    # return args
    if len(args) != 1:
        raise KeyError(
            f"You need to provide the name you want to get the phone number for."
        )
    name = args[0]
    if name in contacts:
        return f"{name}'s phone number is {contacts[name]}"
    else:
        raise NameError(
            f"Contact {name} not found in your contact list. Please create contact {name}, or check the name you wanna change."
        )


@input_error
def get_all_contacts(contacts):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

    raise ValueError(
        "No contacts found in your contact list. Please create at least one contact.aa"
    )


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))

        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(get_phone(args, contacts))

        elif command == "all":
            print(get_all_contacts(contacts))

        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
