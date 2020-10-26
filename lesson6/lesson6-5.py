# Урок 6, задача 5.
# Канцелярские принадлежности
def main():
    class Stationery:
        def __init__(self, title):
            self.title = title

        def draw(self):
            print('Запуск отрисовки...\n')

    class Pen(Stationery):
        def draw(self):
            print(f"{self.title} пишет синими чернилами")

    class Pencil(Stationery):
        def draw(self):
            print(f"{self.title} пишет графитом")

    class Handle(Stationery):
        def draw(self):
            print(f"{self.title} пишет красным цветом")

    s = Stationery('')
    s.draw()

    pn = Pen('Ручка')
    pn.draw()

    pe = Pencil('Карандаш')
    pe.draw()

    ha = Handle('Маркер')
    ha.draw()


main()
