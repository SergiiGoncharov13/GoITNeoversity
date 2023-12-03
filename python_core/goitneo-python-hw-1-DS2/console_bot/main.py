USERS = {}


def error_handler(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'This contact doesnt exist, please try again'
        except ValueError as exception:
            return exception.args[0]
        except IndexError:
            return 'This contact cannot be added, it exists already'
        except TypeError:
            return 'Unknown command, please try again'
    return inner


@error_handler
def add_contact(args):
    name, phone = args
    if name in USERS:
        raise ValueError('This user already exist')
    USERS[name] = phone
    return f"User {name} added"


@error_handler
def change_contact(args):
    name, phone = args
    old_phone = USERS[name]
    USERS[name] = phone
    return f"User {name} have a new phone number, old was: {old_phone}"


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
}


@error_handler
def parser_input(user_input):
    cmd, *args = user_input.split()
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