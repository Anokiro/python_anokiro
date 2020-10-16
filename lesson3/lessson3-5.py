# Урок 3, задача 5.
# Обработка запроса пользователя
def main():
    try:
        my_list = []
        while True:
            take_num = input('Введите целые числа через пробел (или q в конце для выхода): ')
            share = take_num.split()
            test0 = ''.join(share)
            test = test0.isdigit()
            if test == True:
                convert_in_list = list(map(int, share))
                summa = sum(convert_in_list)
                print('Промежуточный счет: ', summa)
                my_list.append(summa)
                print('Итоговый счет: ', sum(my_list))
            elif test == False:
                share2 = share
                test_false = share2.remove('q')
                convert_in_list2 = list(map(int, share2))
                summa2 = sum(convert_in_list2)
                my_list.append(summa2)
                print('Итоговый счет:', sum(my_list), ' Подсчет завершен.')
                break
    except ValueError as err:
        print('---Введите целое числовое значение!!!---\n''---Пример заполнения: 1 2 7\n'
            '---Пример для выхода из программы: 1 2 7 q (в конце поставьте q)')


main()
