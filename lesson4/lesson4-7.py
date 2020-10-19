# Урок 4, задача 7.
# Функция с генератором и yield

def generator(g):
    fact = 1
    n = range(1, g + 1)
    for el in n:
        fact *= el
        yield fact
g = 4
print(f"Найти факториал числа {g} ...")
for i in generator(g):
    i
print(f'Он равен({g}!): {i}')


#from math import factorial
#print(factorial(4))