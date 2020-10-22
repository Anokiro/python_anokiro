# Урок 5, задача 4.
# Перевод на русский
# pip install googletrans выполнить в cmd для установки модуля
def main():
    from googletrans import Translator
    translator = Translator()
    file = open("lesson5-4.txt", 'r')
    file2 = open("lesson5-4(2).txt", 'w')
    for i in file:
        word, tire, num = i.split()
        transll = translator.translate(word, scr='en', dest='ru')
        print(transll.text)
        file2.write(f"{transll.text} {tire} {num}\n")
    print("Перевод текста завершен. Он записан в файл: ", file2.name)
    file.close()
    file2.close()

main()
