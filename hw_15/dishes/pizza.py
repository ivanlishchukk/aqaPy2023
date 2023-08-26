from .dishFactory import DishFactory

class Pizza(DishFactory):
    _dish_type = 'pizza'

    def __init__(self):
        self.name = 'Italian'
        self.__positions = ['vegan', 'meet']

    @property
    def positions(self):
        return self.__positions

    def get_dish(self, name):
        if name == 'vegan':
            return 'here`s your vegan pizza'
        elif name == 'meet':
            return 'here`s your meet pizza'