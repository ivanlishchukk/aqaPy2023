#Task_1
list_1 = {1, 2, 5, 'test', 0, 'aqa'}
list_2 = {0, 3, 7, 'set', '4', 'aqa'}
result_1 = lambda x, y: set.intersection(x, y)
print(result_1(list_1,list_2))

#Task_2
print('\nВведіть дані у рядок:')
raw = input()
result_2 = lambda x: x.isnumeric()
answer = result_2(raw)
if answer is True:
    answer = "Ваш рядок є числом"
else:
    answer = "Ваш рядок не є числом"
print(answer)

#Task_3
list_3 = ['wow', 'what', 'a', 'long', 'list', '!']
list_4 = ['no', 'this', 'list', 'is', 'longer', 'then']
list_5 = ['take', 'my', 'beer', 'guys', 'if', 'you', 'think', 'I am not']
result_3 = lambda a, b, c: min(len(a), len(b), len(c))
result_4 = lambda a, b, c: max(len(a), len(b), len(c))
res_min = result_3(list_3,list_4,list_5)
res_max = result_4(list_3,list_4,list_5)

if res_min==len(list_3) and res_min==len(list_4):
    result_3 = "перший та другий"
elif res_min==len(list_3) and res_min==len(list_5):
    result_3 = "перший та третій"
elif res_min==len(list_4) and res_min==len(list_5):
    result_3 = "другий та третій"
elif res_min==len(list_3):
    result_3 = "перший"
elif res_min==len(list_4):
    result_3 = "другий"
else:
    result_3 = "третій"

if res_max==len(list_3) and res_min==len(list_4):
    result_4 = "перший та другий"
elif res_max==len(list_3) and res_min==len(list_5):
    result_4 = "перший та третій"
elif res_max==len(list_4) and res_min==len(list_5):
    result_4 = "другий та третій"
elif res_max==len(list_3):
    result_4 = "перший"
elif res_max==len(list_4):
    result_4 = "другий"
else:
    result_4 = "третій"

print("\nСписок(-ки) з мінімальною довжиною - ", result_3, "\nСписок(-ки) з максимальною довжиною - ", result_4)