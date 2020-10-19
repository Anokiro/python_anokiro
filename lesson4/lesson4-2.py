# Урок 4, задача 2.
# Сравнение элементов списка
def main():
    my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    end_list = []
    [end_list.append(my_list[el + 1]) for el in range(len(my_list) - 1) if my_list[el] < my_list[el + 1]]
    print('Первый вариант: ', end_list)


main()

""" В варианте с индексами и без генератора лучше читается логика посроения алгоритма при Debug!
 И мыслить с конца неудобно как в 1-м варианте! """
def main2():
    my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
    index = 0
    end_list = []
    while index != (len(my_list) - 1):
        if my_list[index] < my_list[index + 1]:
            end_list.append(my_list[index + 1])
        index += 1
    print('Второй вариант (без генератора): ', end_list)


main2()
