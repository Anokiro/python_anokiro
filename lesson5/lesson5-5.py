# Урок 5, задача 5.
# Сумма цифр.
def main():
    try:
        file = open('lesson5-5.txt', 'w')
        file.write(input("Введите числа через пробел (целые или дробные): "))
        my_list = []
        file.close()
        file = open('lesson5-5.txt', 'r')
        for i in file:
            splitt = i.split()
            for j in splitt:
                my_list.append(float(j))
        print(f"Сумма чисел равна: {sum(my_list)}")
        file.close()
    except Exception as err:
        print('Необходимо ввести числа через пробел.')


main()
