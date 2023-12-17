from classes_for_bot import AddressBook, Record

USERS = AddressBook()


def error_handler(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "This contact doesnt exist, please try again"
        except ValueError as exception:
            return exception.args[0]
        except IndexError:
            return "This contact cannot be added, it exists already"
        except TypeError:
            return "Unknown command, please try again"
        except AttributeError:
            return "Opps"
    return inner


@error_handler
def add_contact(args):
    name, phone = args
    if name in USERS:
        raise ValueError("This user already exist")
    record = Record(name)
    record.add_phone(phone)
    USERS.add_record(record)
    return f"User {name}: {phone} added"

@error_handler
def change_contact(args):
    name, phone = args
    USERS[name] = phone
    return f"User {name} have a new phone number"

@error_handler
def show_phone(args):
    user = args[0]
    phone = USERS[user]
    return f"{user}: {phone}"
   
@error_handler
def show_all(_):
    result = ""
    for name, phone in USERS.items():
        result += f"{name}: {phone} \n"
    return result

@error_handler
def add_birthday(data):
    name, data = data.strip().split(" ")
    record = USERS[name]
    record.add_birthday(data)
    return f"For {name} you add birthday {data}"

@error_handler
def show_birthday(args):
    user = args[0]
    birthday = USERS[user]
    return f"{user}: {birthday}"

@error_handler
def save_address_book(*_):
    return USERS.save_to_file()

@error_handler
def load_address_book(*_):
    return USERS.load_from_file()
    
def hello(_):
    return "How can I help you?"
    
def exit(_):
    return "Good bye!"


HANDLERS = {
    "hello": hello,
    "close": exit,
    "exit": exit,
    "add": add_contact,
    "change": change_contact,
    "all": show_all,
    "phone": show_phone,
    "add-birthday": add_birthday,
    "show-birthday": show_birthday,
    "save": save_address_book,
    "load": load_address_book
}


@error_handler
def parser_input(user_input):
    cmd, *args = user_input.strip().split(' ')
    try:
        handler = HANDLERS[cmd.lower()]
    except KeyError:
        if args:
            cmd = f"{cmd} {args[0]}"
            args = args[1:]
        handler = HANDLERS[cmd.lower(), "Unknown command"]
    return handler, args


def main():
    while True:
        user_input = input("Enter command> ")
        if user_input in ("close", "exit"):
            print("Good bye!")
            break
        handler, *args = parser_input(user_input)
        result = handler(*args)
        if not result:
            print("Good bye!")
            break
        print(result)


if __name__ == "__main__":
    main()