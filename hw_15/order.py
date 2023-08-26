from hw_15.dishes.pizza import Pizza
from hw_15.dishes.risotto import Risotto
from hw_15.dishes.pasta import Pasta


class OrderFactory:
    def __init__(self, dish_type, dish_option):
        self.__dish_type = dish_type
        self.__dish_option = dish_option

    def change_dish_type(self, new_dish_type):
        if new_dish_type not in ['pizza', 'risotto', 'pasta']:
            raise Exception('Dish type change is not allowed here')
        self.__dish_type = new_dish_type

    @staticmethod
    def get_dish(dish_type):
        if dish_type == 'pizza':
            return Pizza()
        elif dish_type == 'risotto':
            return Risotto()
        elif dish_type == 'pasta':
            return Pasta()

    @property
    def dish_type(self):
        return self.__dish_type

    @property
    def dish_option(self):
        return self.__dish_option
