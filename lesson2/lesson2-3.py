# Урок 2, задача 3.
# Времена года.
def main():
    num = int(input('Введите целое число от 1 до 12: '))
    my_dict = {'zz': 'зима', 'vv': 'весна', 'll': 'лето', 'oo': 'осень'}
    if num in [1, 2, 12]:
        print(f"Время года:", my_dict.get('zz'))
    elif num in [3, 4, 5]:
        print(f"Время года: ", my_dict.get('vv'))
    elif num in [6, 7, 8]:
        print(f"Время года: ", my_dict.get('ll'))
    elif num in [9, 10, 11]:
        print(f"Время года: ", my_dict.get('oo'))
    elif num >= 13:
        print('Вас просили ввести значение от 1 до 12!')
main()

