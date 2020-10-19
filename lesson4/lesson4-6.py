# Урок 4, задача 6.
# Пара скриптов
try:
    from sys import argv
    file_name, num = argv
    from itertools import count
    num = int(num)
    my_list = []
    for el in count(num):
        if el > num + 9:
            break
        else:
            my_list.append(el)
    print('Вот список с count: ', my_list)
    from itertools import cycle
    file_name, next_list = argv
    c = 0
    my_list2 = []
    for el in cycle(next_list):
        if c > (len(my_list) - 1):
            break
        my_list2.append(el)
        c += 1
    ask = list(map(int, my_list2))
    print('Вот список с cycle: ', ask)
except Exception as err:
   print("Введите целое число!")
