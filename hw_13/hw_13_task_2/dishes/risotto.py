from .dishFactory import DishFactory

class Risotto(DishFactory):
    _dish_type = 'risotto'
    def __init__(self):
        self.name = 'Italian'
        self.__positions = ['classic', 'mushrooms']
    @property
    def positions(self):
        return self.__positions
    def get_dish(self, name):
        if name == 'classic':
            return 'here`s your classic risotto'
        elif name == 'mushrooms':
            return 'here`s your risotto with mushrooms'
