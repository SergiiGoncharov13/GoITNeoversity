from collections import UserDict
from datetime import datetime
import pickle


class Field:
    def __init__(self, value):
        self._value = None
        self.value = value

    def __str__(self):
        return str(self.value)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = value
    

class Name(Field):
    pass


class Phone(Field):
    @Field.value.setter
    def value(self, value):
        if len(value) < 10 or len(value) > 12:
            raise ValueError("Phone must contains 10 symbols")
        elif not value.isnumeric():
            raise ValueError('Wrong phones.')
        self._value = value


class Birthday(Field):
    @Field.value.setter
    def value(self, value):
        today = datetime.now().date()
        birth_date = datetime.strptime(value, "%d-%m-%Y").date() 
        if birth_date > today:
            raise ValueError("Wrong input")
        self._value = value
 

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

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

    def add_birthday(self, date):
        self.birthday = Birthday(date)
        return f"The birthday was set successfully"


class AddressBook(UserDict):
    def __init__(self):
        super().__init__()
        self.load_from_file()

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

    def save_to_file(self):
        with open('contacts_book.bin', 'wb') as file:
            pickle.dump(self.data, file)
        return f"contacts book saved"

    def load_from_file(self):
        try:
            with open('contacts_book.bin', 'rb') as file:
                self.data = pickle.load(file)
            return f"loaded from contact book"
        except FileNotFoundError:
            pass

