#Task_2
def some(a,b):
    try:
        return a/b
    except ArithmeticError as e:
        print('This is Arithmetic Error')
    finally:
        print('finally text')
    print('post code')
some(2,0)


#Task_3
import datetime
date_n_time_enter = input('Введіть дату та час у форматі yyyy,mm,dd,hh,mm,ss:\n')
year, month, day, hours, minutes, seconds = map(int, date_n_time_enter.split(','))
date_n_time = datetime.datetime(year, month, day, hours, minutes, seconds)
some_days = int(input('Введіть кількість днів:\n'))
action = input('Оберіть дію (додавання - напишіть "+", віднімання - напишіть "-":\n')
def task_2(date_n_time, some_days, action):
    if action == '+':
        result_sum = date_n_time + datetime.timedelta(days = some_days)
        return result_sum
    else:
        result_diff = date_n_time - datetime.timedelta(days = some_days)
        return result_diff
print(task_2(date_n_time, some_days, action))


#Task_4
import datetime
def your_age(age):
    time_start = age
    time_end = datetime.datetime.now()
    age_dt = time_end - time_start
    age_ts = datetime.datetime.timestamp(time_end) - datetime.datetime.timestamp(time_start)
    return f"Вік у форматі datetime: {age_dt} \nВік у форматі timestamp: {age_ts}"
print(your_age(datetime.datetime(year=1998, month=7, day=5, hour=7, minute=15, second=5)))