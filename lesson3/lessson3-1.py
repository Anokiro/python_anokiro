# Урок 3, задача 1.
# Задача с функцией
def main(price, earnings):
    try:
        multiplier = price / earnings
        print('Ваш мультипликатор равен: ')
        print(format(multiplier, '.2f'))
    except ZeroDivisionError as err:
        print('Деление на ноль запрещено!')


main(int(input("Введите цену акции (целое число): ")),
           int(input("Введите показатель прибыли на акцию (млн. руб, целое число): ")))
