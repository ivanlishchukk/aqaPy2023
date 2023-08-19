from .dishFactory import DishFactory


class Pasta(DishFactory):
    _dish_type = 'pasta'

    def __init__(self):
        self.name = 'Italian'
        self.__positions = ['boloiese', 'carbonara']

    @property
    def positions(self):
        return self.__positions

    def get_dish(self, name):
        if name == 'boloniese':
            return 'here`s your pasta boloniese'
        elif name == 'carbonara':
            return 'here`s your pasta carbonara'
