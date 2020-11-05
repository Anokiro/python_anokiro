# Урок 8, задача 2.
# Собственное исключение.
class MyOwnEr(Exception):
    def __init__(self, txt):
        self.txt = txt


print('На что будем делить число 75?')
data_check = input('Введите число: ')

try:
    data_check = float(data_check)
    if data_check == 0:
        raise MyOwnEr('На ноль делить нельзя!')
except (ValueError, MyOwnEr) as err:
    print('Нужно ввести число!')
else:
    print('Результат: ', format(75.0 / data_check, '.1f'))
