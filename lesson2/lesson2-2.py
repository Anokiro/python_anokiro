# Урок 2, задача 2.
# Обмен значений соседних элементов
def main():
    proceed = 'y'
    result_list = []
    while proceed == 'y':
        num = (input('Введите значение: '))
        result_list.append(num)
        proceed = input("Продолжить ввод? (y - да, другая клавиша - нет) ")
    print(f"Список введенных значений: {result_list}")
    index = 0
    for i in range(int(len(result_list) / 2)):
        result_list[index], result_list[index + 1] = result_list[index + 1], result_list[index]
        index += 2
    print(f"Список с обменом соседних значений: {result_list}")
main()

