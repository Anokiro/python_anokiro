# Урок 4, задача 1.
# Реализация скрипта.
try:
    from sys import argv
    file_name, work_hour, rate_per_hour, bonus = argv
    work_hour = int(work_hour)
    rate_per_hour = int(rate_per_hour)
    bonus = int(bonus)
    print(file_name)
    print("Выработка в часах: ", work_hour)
    print("Ставка в час: ", rate_per_hour)
    print("Премия: ", bonus)
    result = (work_hour * rate_per_hour + bonus)
    print("Итого Ваша з.п.: ", result)
except Exception as err:
    print("Вы неправильно ввели данные!\nПример правильного заполнения(целые числа, через пробел): 5 180 2000 (выработка, ставка, премия)")