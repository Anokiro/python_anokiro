# Урок 6, задача 1.
# Светофор
def main():
    from time import sleep
    from itertools import cycle
    class TrafficLight:
        __color = ['красный', 'желтый', 'зеленый', 'желтый']

        def running(self):
            c = 0
            for el in cycle(self.__color):
                if el == 'красный':
                    print(f'\r{el}', end='')
                    sleep(7)
                elif el == 'желтый':
                    print(f'\r{el}', end='')
                    sleep(2)
                elif el == 'зеленый':
                    print(f'\r{el}', end='')
                    sleep(5)
                if c > 5:
                    print(f'\rПрограмма светофора завершена.')
                    break
                c += 1

    t = TrafficLight()
    t.running()


main()
