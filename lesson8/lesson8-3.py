# Урок 8, задача 3.
# Собственное исключение.
class MyOwnEr(Exception):
    def __init__(self, txt):
        self.txt = txt

play = 'y'
total_list = []
data_check2 = ''
str_check = '0'

while play == 'y':
    data_check = input('Введите целые числа: ')
    data_check2 = data_check
    data_list = []
    check_list = ''
    for i in data_check:
        if i.isdigit():
            check_list += i
        elif i.isalpha() == True:
            str_check += i
        elif i.isalpha() == False:
            data_list.append(check_list)
            check_list = ''
    if check_list != '':
        data_list.append(check_list)
    total_list.append(data_list)
    play = input("Продолжить ввод? y - да, другая буква - нет: ")

total_list_final = []
for i in total_list:
    for j in i:
        total_list_final.append(j)
print(f'\nВаш список: {list(map(int, total_list_final))} \n', end='')


try:
    for i in str_check:
        if i == '0':
            print('Все ок.', end='')
        else:
            raise MyOwnEr('\nНо Вы ввели не только числа! Мы это исправили: оставлены только числа.')
except (ValueError, MyOwnEr) as err:
    print(err)
