# Урок 3, задача 6.
# Функция
def int_func():
    try:
        global upper
        take_word = input("Введите 1 слово из маленьких букв: ")
        share = take_word.split()
        if len(share) > 1:
            print('Вас просили ввести одно слово!')
        elif len(share) == 1:
            upper = take_word.title()
            print('Введенное Вами слово: ', upper)
        take_word_two = input("Ведите строку из слов: ")
        upper2 = take_word_two.title()
        upper3 = upper +' '+ upper2
        print(upper3)
    except NameError as err:
        print('Вернитесь назад и корректно заполните первое поле!')


int_func()
