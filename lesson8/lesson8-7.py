# Урок 8, задача 7.
# Операции с комплексными числами
def main():

    class ComplexNum:
        def __init__(self):
            self.num1 = complex(3, 1) #первое значение:
            self.num2 = complex(2, -3) #второе значение:

        def __add__(self, other):
            return f'Сумма комплексных чисел равна: {self.num1 + self.num2}'

        def __mul__(self, other):
            return f'Произведение комплексных чисел равно: {self.num1 * self.num2}'

    c = ComplexNum()
    print(c + c)
    print(c * c)


main()
