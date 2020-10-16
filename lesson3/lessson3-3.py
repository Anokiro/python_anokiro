# Урок 3, задача 3.
# Задача с функцией о данных пользователя
def my_func(num1, num2, num3):
        my_list = [num1, num2, num3]
        minim = min([num1, num2, num3])
        my_list.remove(minim)
        my_list = sum(my_list)
        return my_list


print(my_func(float(input('Введите первое число: ')), float(input('Введите второе число: ')),
              float(input('Введите третье число: '))))
