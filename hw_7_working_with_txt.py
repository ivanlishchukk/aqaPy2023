#Task_1
import re
def task_one(filename_1):
    output_1 = open(filename_1, 'r')
    list_task_one = []
    for i in output_1.readlines():
        pattern = '^.|\n'
        result_i = re.sub(pattern, '', i)
        list_task_one.append(result_i)
    output_1.close()
    return list_task_one
print(task_one('domains.txt'))

#Task_2
def task_two(filename_2):
    output_2 = open(filename_2, 'r')
    list_task_two = []
    for i in output_2.readlines():
        splited_list = i.split(', ')
        list_task_two.append(splited_list[1])
    output_2.close()
    return list_task_two
print(task_two('names.txt'))

#Task_3
def task_three(filename_3):
    output_3 = open(filename_3, 'r')
    list_task_three = []
    dict_list = []
    dict_final = {}
    for i in output_3.readlines():
        split_list_1 = i.split('- ')[0]
        list_task_three.append(split_list_1.rstrip())
    for x in list_task_three:
        date_len = len(x.split())
        if date_len > 1:
            k = 'date'
            dict_final[k] = x
            dict_list.append(dict_final.copy())
    output_3.close()
    return dict_list
print(task_three('authors.txt'))
'''
я включив у результат "December 1817" хоч він і без дати з тієї причини, що, враховуючи особливості тієї епохи,
дійсно могло статися так, що дата не відома до дня, тільки до року та місяця.
'''