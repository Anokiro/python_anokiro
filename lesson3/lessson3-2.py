# Урок 3, задача 2.
# Задача с функцией о данных пользователя
def main(name, surname, born, town, email, phone):
    name1 = input('Введите ваше имя: ')
    surname1 = input('Введите вашу фамилию: ')
    born1 = input('Введите год рождения: ')
    town1 = input('Введите город, в котором Вы проживаете: ')
    email1 = input('Введите вашу эл.почту: ')
    phone1 = input('Введите номер вашего телефона: ')
    print('Ваше имя:', name1 +', ','Фамилия:', surname1+', ','Год рождения:',
          born1+', ','Город проживания:', town1+', ','Электронная почта:', email1+', ',' Телефон:', phone1+', ')


main(name='',surname='', born='', town='', email='', phone='')
