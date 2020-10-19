# Урок 4, задача 5.
# Список с умножением
def main():
    from functools import reduce
    list = [el for el in range(100, 1001) if el % 2 == 0]
    end_list = reduce(lambda x,y: x * y, list)
    print(f'Вот ваше ооочень длинное число: {end_list}')

main()