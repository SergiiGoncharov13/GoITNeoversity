from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)
    

class Name(Field):
    pass


class Phone(Field):
    def value(self, value):
        if len(value) < 10 or len(value) > 12:
            raise ValueError("Phone must contains 10 symbols")
        elif not value.isnumeric():
            raise ValueError('Wrong phones.')
        self._value = value


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone):
        self.phones.append(Phone(phone))
        return f"The phone was added"
   
    def remove_phone(self,phone):
        for r_phone in self.phones:
            if r_phone.value == phone:
                self.phones.remove(r_phone)
                return f"The phone was deleted"
            else:
                return f"The phone {phone} isn't in your contact book"
    
    def edit_phone(self, phone, new_phone):
        for val in self.phones:
            if val.value == phone:
                val.value = new_phone
                return f"This phone was changed"
            else:
                return f"This phone {phone} isn't in your contact book"

    def find_phone(self, phone):
        for phone in self.phones:
            if phone in self.phones:
                return f"{phone}"
            else:
                return f"This phone {phone} isn't in your contact book"


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record
        return f"New contact was added"

    def delete_record(self, name):
        del self.data[name]
        return f"{self.data[name]} was removed"

    def get_record(self, name) -> Record:
        return self.data.get(name)
    
    def search(self, value):
        if self.has_record(value):
            return self.get_record(value)
        for record in self.get_all_record().values():
            for phone in record.phones:
                if phone.value == value:
                    return record
        raise ValueError('Contact not found')


