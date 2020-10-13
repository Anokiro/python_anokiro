# Урок 2, задача 4.
# Вывод слов.
def main():
    text = input('Введите что-нибудь членораздельное: ')
    list = text.split()
    print(f"Вот нумерованный список: ")
    for i, j in enumerate(list, 1):
        j = j[0:10]
        print(i, j)
main()

