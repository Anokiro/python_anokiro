# Урок 5, задача 2.
# Подсчет количества строк и слов
def main():
    file = open("lesson5-2.txt", 'r')
    my_list = []
    count = 1
    for i in file:
        splitt = i.split()
        print(f"Количество слов в строке {count}: ", len(splitt))
        my_list.append(splitt)
        count += 1
    print("Всего строк: ", len(my_list))
    file.close()


main()
