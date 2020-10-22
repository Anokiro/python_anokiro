# Урок 5, задача 1.
# Запись информации в файл.
def main():
    with open('lesson5-1.txt', 'a') as file:
        take = input("Введите данные, которые будут записаны в файл: ")
        file.write(f"{take}\n")
    read_file = open('lesson5-1.txt', 'r')
    print('Вот что записано в файл: \n', read_file.read())
    read_file.close()


main()
