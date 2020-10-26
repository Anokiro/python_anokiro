# Урок 2, задача 2.
# Дорога
def main():
    class Road:
        def __init__(self):
            self._lenght = 20
            self._width = 5000
        def calculate(self):
            formula = (self._lenght * self._width * 25 * 5) / 1000
            return f"{formula:.0f} т"

    r = Road()
    print(r.calculate())


main()
