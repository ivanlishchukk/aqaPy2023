from abc import ABC, abstractmethod

class DishFactory(ABC):
    _dish_type = ''
    @abstractmethod
    def get_dish(self, name):
        pass
