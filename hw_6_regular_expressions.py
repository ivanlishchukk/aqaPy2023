#Task_1
import re
def result():
    print('Напишіть будь-який текст:')
    test_str = input()
    check_upper = re.findall(r'[A-Z]', test_str)
    check_lower = re.findall(r'[a-z]', test_str)
    check_num = re.findall(r'[0-9]', test_str)
    check_underline = re.findall(r'[_]', test_str)
    check_exception = re.findall(r'[^A-Za-z0-9_]', test_str)
    if check_upper and check_lower and check_num and check_underline and not check_exception:
        print("Стрічка містить лише великі і малі літери, числа та нижнє підкреслення одночасно.")
    else:
        print("Стрічка НЕ містить лише великі і малі літери, числа та нижнє підкреслення одночасно.")
result()

#Task_2
def result(items_list):
    pattern = '\(|\S+\)'
    for x in items_list[:]:
        check_cages = re.sub(pattern, '', x)
        print(check_cages)
result(['example (.com)', 'github (.com)', 'stackoverflow (.com)'])

#Task_3
print('Напишіть будь-який текст:')
test_text = input()
added_space = re.sub(r'[A-Z]', ' \1', test_text)
print(added_space)