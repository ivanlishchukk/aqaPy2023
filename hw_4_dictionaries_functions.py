#Task1
def sharedValues(list_1, list_2):
    result_task_1 = sorted(set([x for x in list_1 + list_2 if x in list_1 and x in list_2]))
    print(f"Спільні числа зі списку у зростаючому порядку:", result_task_1)

sharedValues([1, 2, 4, 5, 7, 8], [0, 2, 3, 5, 6, 8, 9])

#Task2
import numpy as np
students_data = {'John':98, 'Mike':80, 'Jeremy':92, 'Juls':100, 'Randal':75}
def mark_upper_intermediate():
    average_mark = np.mean(list(students_data.values()))
    result_task_2 = set([x for x in students_data.values() if x > average_mark])
    print(f"\nCередній бал дорівнює:", average_mark)
    print("Студенти, чий бал вище середнього:", result_task_2)

mark_upper_intermediate()

#Task3
''' 
3.Створіть списки із значеннями для name, surname, location, наприклад name = ['Alex', 'John', 'Simba']. 
Напишіть програму, яка створює словники з даними випадкових людей на основі ваших списків, роздрукуйте результат. 
Для випадковості значень скористайтесь модулем random. приклад згенерованого словника:
{'name':'Liza', 'surname':'Djoconda', 'location':'Florence'}
'''
import random
keys_list = ['name', 'surname', 'location']
name_list = ['John', 'Hanah', 'Stieven', 'Andre', 'Laura', 'Marie']
surname_list = ['Maigan', 'Smith', 'Belskii', 'Cooper', 'Niegels', 'Jordan']
location_list = ['Kyiv', 'Vancouver', 'Washington', 'Warsaw', 'Berlin', 'Paris']
def random_list():
    random_name_value = random.choice(name_list)
    random_surname_value = random.choice(surname_list)
    random_location_value = random.choice(location_list)
    randomised_list = [random_name_value, random_surname_value, random_location_value]
    result = dict(zip(keys_list, randomised_list))
    print('\n', result)
random_list()
