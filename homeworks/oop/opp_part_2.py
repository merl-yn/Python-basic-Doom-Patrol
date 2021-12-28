import dataclasses
from collections import namedtuple

# 1


class Laptop:
    def __init__(self):
        battery_1 = Battery(f"Charge level first battery is 100%")
        battery_2 = Battery(f"Charge level second battery is 89%")
        self.batteries = (battery_1, battery_2)


class Battery:
    def __init__(self, charge_level):
        self.charge_level = charge_level


laptop = Laptop()


# 2

class Guitar:
    def __init__(self, guitar_string):
        self.guitar_string = guitar_string


class GuitarString:
    def __init__(self):
        pass


guitar_str = GuitarString()
guitar = Guitar(guitar_str)


# 3

class Calc:
    @staticmethod
    def add_nums(a, b, c):
        return a + b + c


# 4

class Pasta:
    carbonara = ['forcemeat', 'tomatoes']
    bolognaise = ['bacon', 'parmesan', 'eggs']

    TYPES = (carbonara, bolognaise)

    def __init__(self, *ingredients):
        self.ingredients = ingredients

    @classmethod
    def carbon(cls):
        return cls(cls.TYPES[0])

    @classmethod
    def bolog(cls):
        return cls(cls.TYPES[1])


# 5

class Concert:
    max_visitors_num = 0

    def __init__(self):
        self._visitors_count = 0

    @property
    def visitors_count(self):
        return self._visitors_count

    @visitors_count.setter
    def visitors_count(self, value):
        if value <= self.max_visitors_num:
            self._visitors_count = value
        else:
            self._visitors_count = self.max_visitors_num


# 6

@dataclasses.dataclass
class AddressBookDataClass:
    key: int
    name: str
    phone_number: str
    address: str
    email: str
    birthday: str
    age: int


# 7

AddressBookClass = namedtuple('AddressBookClass', ['key',
                                                   'name',
                                                   'phone_number',
                                                   'address',
                                                   'email',
                                                   'birthday',
                                                   'age'])


# 8

class AddressBook:
    def __init__(self, key, name, phone_number, address, email, birthday, age):
        self.key = int(key)
        self.name = str(name)
        self.phone_number = str(phone_number)
        self.address = str(address)
        self.email = str(email)
        self.birthday = str(birthday)
        self.age = int(age)

    def __str__(self):
        return f'{self.key}, {self.name},' \
               f' {self.phone_number}, {self.address},' \
               f' {self.email}, {self.birthday}, {self.age}'


class Person:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    @property
    def get_new_age(self):
        return self.age

    @get_new_age.setter
    def get_new_age(self, value):
        self.age = value


# 10

class Student:
    def __init__(self, idi, name):
        self.id = idi
        self.name = name


student = Student(0, "Alex")
setattr(student, 'email', 'alexmail@gmail.com')
print(getattr(student, 'email'))

# 11


class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def convert_cel_to_fahr(self):
        return self._temperature * 1.8 + 32


obj = Celsius(36)
print(obj.convert_cel_to_fahr)
