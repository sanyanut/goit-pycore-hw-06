from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value)


class Phone(Field):
    def __init__(self, value):
        if not (len(value) == 10 and value.isdigit()):
            raise ValueError("Given value hasn't 10 digits")
        super().__init__(value)


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу

    def add_phone(self, value):
        for phone in self.phones:
            if phone.value == value:
                raise ValueError(f"Phone {value} is already in the list")
        self.phones.append(Phone(value))

    def edit_phone(self, old_phone, new_phone):
        if Phone(old_phone) and Phone(new_phone):  # additional checks for input data
            for phone in self.phones:
                if phone.value == old_phone:
                    phone.value = new_phone
                    return phone.value

    def find_phone(self, phone):
        if Phone(phone):  # additional validation for input data through Phone class
            for phone_item in self.phones:
                if phone_item.value == phone:
                    return phone_item.value

    def remove_phone(self, phone):
        if Phone(phone):
            for phone_item in self.phones:
                if phone_item.value == phone:
                    self.phones.remove(phone_item)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record):
        # add new record data by the name value nested in record attribute
        self.data[record.name.value] = record

    def find(self, name):
        for name_item in self.data:
            if name_item == name:
                return self.data[name_item]
        return None

    def delete(self, name):
        if name in self.data:
            del self.data[name]


# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

# Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "1112223333")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

# Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# additional print check if specific phone is removed
# john.remove_phone("5555555555")
# print(john)

# Видалення запису Jane
book.delete("Jane")


# additional print loop to check Jane is deleted from the book.data
# for name, record in book.data.items():
#     print(record)
