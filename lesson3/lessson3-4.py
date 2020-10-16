# Урок 3, задача 3.
# Задача с функцией о данных пользователя
def my_func(x, y):
    x = abs(x)
    if y > 0:
        sub = (x) ** (int(y) / -1)
    if y < 0:
        sub = (x) ** (int(y))
    return sub


print(my_func(float(input('Введите число х (целое или дробное): ')),
              int(input('Введите число y (только целое): '))))
