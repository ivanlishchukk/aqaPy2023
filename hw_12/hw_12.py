class Train:
    def __init__(self, company, drivers, route):
        self.id = {}
        self.company = company
        self.__drivers = drivers
        self.__route = route
    def __setitem__(self, key, value):
        self.id[key] = value
    def __getitem__(self, item):
        return self.id[item]
    def __len__(self):
        main_car_count = sum(1 for car in self.id.values() if car.car_type == 'MainCar')
        return len(self.id) - main_car_count

class TrainCar:
    def __init__(self, car_id, car_type):
        self.car_id = car_id
        self.car_type = car_type
        self.__places = 30
        self.passengers = {}
    def __setitem__(self, key, value):
        self.passengers[key] = value
    def __len__(self):
        return len(self.passengers)
    def __getitem__(self, item):
        return self.passengers[item]


class Passenger:
    def __init__(self, pass_id, name, destination, place):
        self.pass_id = pass_id
        self.__name = name
        self.__destination = destination
        self.__place = place
    def __str__(self):
        return f'name:{self.__name}\ndestination:{self.__destination}\nplace:{self.__place}'

train = Train('UZ', 2, 'Kyiv-Odessa')

trainCar_0 = TrainCar(0, 'MainCar')
trainCar_1 = TrainCar(1, 'Car')
trainCar_2 = TrainCar(2, 'Car')

train[0] = trainCar_0
train[1] = trainCar_1
train[2] = trainCar_2

passenger_0 = Passenger(0,'John', 'Mykolaiv', 10)
passenger_1 = Passenger(1,'Mike', 'Odessa', 15)
passenger_2 = Passenger(2,'Lilia', 'Cherkassy', 20)

trainCar_1[0] = passenger_0
trainCar_1[1] = passenger_1
trainCar_1[2] = passenger_2

print(len(train))
print(len(trainCar_1))
print(trainCar_1[2])