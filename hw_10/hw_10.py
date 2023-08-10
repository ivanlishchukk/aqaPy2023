from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, brand: str, year: int, price: int):
        self.brand = brand
        self.year = year
        self.price = price

    @abstractmethod
    def get_brand(self):
        pass

    @abstractmethod
    def get_year(self):
        pass

    def get_price(self):
        return self.price


class Car(Vehicle):
    def __init__(self, brand, year, price, colour: str, seats: int):
        super().__init__(brand, year, price)
        self.colour = colour
        self.seats = seats

    def get_brand(self):
        print(f"Brand is {self.brand}")

    def get_year(self):
        print(f"Year is {self.year}")

    def get_price(self):
        print(f"Price is {self.price}")

    def get_colour(self):
        return self.colour

    def get_seats(self):
        return self.seats


class Specialised(Car):
    def __init__(self, brand, year, price, colour, seats, belt):
        super().__init__(brand, year, price, colour, seats)
        self.belt = belt

    def get_price(self):
        print(f"Price is {self.price}")

    def get_colour(self):
        return self.colour

    def get_seats(self):
        return self.seats

    def is_belt(self):
        return self.belt


is_car = Car('Reno', 1998, 2000, 'black', 4)

is_specialised = Specialised('Volvo', 2004, 7000, 'red', 2, True)

is_car.get_brand()
is_car.get_year()
is_car.get_price()

is_specialised.get_brand()
is_specialised.get_year()
is_specialised.get_price()

