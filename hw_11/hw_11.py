from abc import ABC, abstractmethod
from dateutil.utils import today
class ArtObject(ABC):
    def __init__(self, type, is_present, year:int):
        self.__type = type
        self.is_present = is_present
        self.year = year
    @property
    def obj_type (self):
        return self.__type
    @obj_type.setter
    def obj_type (self, new_type):
        self.__type = new_type
    @abstractmethod
    def get_object_presence(self):
        pass
    @staticmethod
    def get_age(year):
        time_start = year
        time_end = today().year
        age = time_end - time_start
        return print(f"{age} year(s)")


class Painting(ArtObject):
    def __init__(self, name, creator, type, is_present, year:int, state):
        super().__init__(type, is_present, year)
        self.name = name
        self.creator = creator
        self.state = state
    def __get_name(self):
        return print(self.name)
    def __get_creator(self):
        return print(self.creator)
    def get_object_presence(self):
        if self.is_present is not None:
            print("Object is present")
        else:
            print("Object is out of the museum")
    def get_info(self):
        self.__get_name()
        self.__get_creator()
        self.get_object_presence()


class Monument(ArtObject):
    def __init__(self, name, creator, material, type, is_present, year, state):
        super().__init__(type, is_present, year)
        self.name = name
        self.creator = creator
        self.material = material
        self.state = state
    def __get_name(self):
        return print(self.name)
    def __get_creator(self):
        return print(self.creator)
    def __get_material(self):
        if self.material is not None:
            return print(self.material)
        else:
            return (print('Unknown year'))
    def get_object_presence(self):
        if self.is_present is not None:
            print("Object is present")
        else:
            print("Object is out of the museum")
    def __get_state(self):
        if self.state is not None:
            print('State is checked.')
        else:
            print('Unknown state.')
    def get_info(self):
        self.__get_name()
        self.__get_creator()
        self.__get_material()
        self.get_object_presence()
        self.__get_state()




print('1) Picture:')
picture = Painting('Mona Lisa', 'Da Vinci', 'Picture','+', 1503, None)
picture.get_info()
print(picture.get_age(1503))


print('2) Monument:')
monument = Monument('Le Penseur', 'August Roden', 'Rock', 'Monument', None, 1880, 'OK')
monument.get_info()
monument.obj_type = 'Instalation'
print(monument.obj_type)
