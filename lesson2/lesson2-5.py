# Урок 2, задача 5.
# Структура Рейтинг
def main():
    my_list = [5, 7, 8, 9]
    proceed = 'y'
    while proceed == 'y':
        num = int(input("Введите целое число: "))
        my_list.append(num)
        my_list.sort()
        proceed = input("Ввести еще число? (y - да, другая буква - нет) ")
    my_list.reverse()
    print(f"\nВот финальный рейтинг: {my_list}")
main()

