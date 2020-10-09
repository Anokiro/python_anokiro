# Урок 1, задача 3.
# Сумма чисел
def main():
    num = input('Введите число суммирования: ')
    num2 = str(num) + str(num)
    num3 = str(num) + str(num) + str(num)
    num_summ = float(num) + float(num2) + float(num3)
    print('Сумма чисел равна:\n', num, '+', num2, '+', num3, '=', f"{num_summ:.0f}")
main()

