# Урок 7, задача 3.
# Клетка
def main():
    class Kletka:
        def __init__(self, value_kletka, value_kletka2):
            self.value_kletka = value_kletka
            self.value_kletka2 = value_kletka2

        def __add__(self, other):
            return f'сумма клеток: {self.value_kletka + other.value_kletka2}'

        def __sub__(self, other):

            if (self.value_kletka - self.value_kletka2) > 0:
                return f'разность клеток: {self.value_kletka - self.value_kletka2}'
            else:
                print("разность: число клеток не может быть нулевым или отрицательным", end='')
                return ''

        def __mul__(self, other):
            return f'произведение клеток: {self.value_kletka * self.value_kletka2}'

        def __floordiv__(self, other):
            return f'целочисленное деление: {self.value_kletka // self.value_kletka2}'

        def make_order(self):
            var = self.value_kletka + self.value_kletka2
            j = 4
            for i in range(var):
                print('*', end='')
                if i + 1 == j:
                    print('\n', end='')
                    j += 4
            return f'\nКол-во клеток(*): {var}'

    k = Kletka(int(input('Первая клетка: ')), int(input('Вторая клетка: ')))
    print(k + k)
    print(k - k)
    print(k * 2)
    print(k // k)
    print(k.make_order())


main()
