# Урок 2, задача 6.
# Структура данных "товары"
def main():
    quantity = int(input("Какое количество товара Вы хотите ввести: "))
    my_list = []
    for err in range(quantity):
        name = input("Введите название: ")
        price = input("Введите цену: ")
        volume = input("Введите количество: ")
        thing = input("Введите ед. измерения (например, шт.): ")
        new_list = dict(название_=name, цена_=price, количество_=volume, eд_=thing)
        print("Значения введены в список.")
        my_list.append(new_list)
    print("\nВот введенные значения: ")
    for i, j in enumerate(my_list, 1):
        print(i, j.get('название_'), ('по цене: '), j.get('цена_'),('в количестве: '), j.get('количество_'))
main()

