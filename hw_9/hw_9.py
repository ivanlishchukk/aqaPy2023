#Task_1
class lion:
    def __init__(self, name, age:int, weight:int, city:str):
        self.name = name
        self.age = age
        self.weight = weight
        self.city = city
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_weight(self):
        return self.weight
    @staticmethod
    def get_info():
        print('Welcome to the zoo!')

#Task_2
class company:
    def __init__(self, logo, found_date, employees = 5000000, country = 'USA'):
        self.logo = logo
        self.found_date = found_date
        self.employees = employees
        self.country = country
    def get_logo(self):
        return self.logo
    def get_employees(self):
        return self.employees
    def get_found_date(self):
        return self.found_date
    @classmethod
    def logo_and_found_date (cls, logo, found_date, country):
        return cls(logo, found_date, country)

#Task_3
def func_name(func):
    def result_name(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__}\n{result}")
        return result
    return result_name

@func_name
def mult_1(x, y):
    mult_math = x*y
    return mult_math
mult_1(5,10)

@func_name
def summ_1(x, y):
    summ_math = x+y
    return summ_math
summ_1(5,10)

#Task_4
import random

new_list = [random.randint(1, 10) for _ in range(100)]
count_result = {i:new_list.count(i) for i in new_list}
print(count_result)
