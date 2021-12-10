# 1

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


# 2

class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity):
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity


# 3

bus_obj = Bus(150, 400, 22)
print(type(bus_obj))

# 4

school_bus = Bus(120, 780, 40)
print(isinstance(school_bus, Vehicle))


# 5

class School:
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students


# 6

class SchoolBus(School, Bus):
    def __init__(self, get_school_id, number_of_students, max_speed, mileage, seating_capacity, bus_school_color):
        School.__init__(self, get_school_id, number_of_students)
        Bus.__init__(self, max_speed, mileage, seating_capacity)
        self.bus_school_color = bus_school_color


# 7

class Bear:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        return f'Bear says {self.sound}'


class Wolf:
    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        return f"Wolf says {self.sound}"


darkBear = Bear("rrrrrr")
greyWolf = Wolf("aauuuu")

animals = (darkBear, greyWolf)

for sounds in animals:
    print(sounds.make_sound())


# 8

class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __new__(cls, name, population):
        new_instance = super(City, cls).__new__(cls)
        if population > 1500:
            return new_instance
        else:
            return "Your city is too small"


city_Lviv = City("Lviv", 900)
city_Kyiv = City("Kyiv", 1600)

cyties = (city_Lviv, city_Kyiv)

for city in cyties:
    print(city)

