# Урок 4, задача 4.
# Поиск чисел без повторений
def main():
    list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    list2 = []
    [list2.append(el) if el not in list2 else list2.remove(el) for el in list]
    print(list2)


main()

def main2():
    list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
    list2 = []
    for el in list:
        if el not in list2:
            list2.append(el)
        else:
            if el in list2:
                list2.remove(el)
    print(list2)


main2()
