# Урок 4, задача 3.
# Поиск чисел
def main():
    a = [el for el in range(20, 241) if el % 20 == 0 or el % 21 == 0]
    print(a)


main()
