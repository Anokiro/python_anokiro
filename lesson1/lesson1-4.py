# Урок 1, задача 4.
# Вывод большего числа
def main():
    num = int(input('Введи число: '))
    score = -1
    #Напишем условие
    while (num // 10) != 0:
        number = num % 10
        num = num // 10
        if number > score:
            score = number
    if num > score:
        score = num
    print(score)
main()

