# Урок 6, задача 4.
# Ловим нарушителя на автомобиле
def main():
    from random import choice, randint
    from time import sleep
    class Car:
        def __init__(self):
            my_list = ['yellow', 'green', 'black', 'white', 'blue']
            my_list2 = ['Alpha-Romeo', 'Ford', 'Fiat', 'BMW']
            my_list3 = [True, False]
            self.speed = randint(0, 100)
            self.color = choice(my_list)
            self.name = choice(my_list2)
            self.is_police = choice(my_list3)
            self.lawbreaker = 'Выявлен нарушитель!'

        def go(self):
            if self.speed > 14:
                print('Состояние: машина в движении')
                sleep(1)

        def stop(self):
            if self.speed <= 14:
                print(f'Состояние: машина остановилась или тормозит')

        def turn(self):
            if self.speed > 60:
                my_list4 = ['на восток', 'на запад', 'на север', 'на юг']
                print('Машина повернула',choice(my_list4))

        def show_speed(self):
            print(f'Радар включен...')
            sleep(2)

    class TownCar(Car):
        def show_speed(self):
            print('Городской автомобиль движется со скоростью (км/ч): ', self.speed)
            sleep(1)
            if self.speed > 60:
                print(f"{self.lawbreaker} {self.color} {self.name}")
                sleep(2)

    class SportCar(Car):
        def sport_car(self):
            self.speed = randint(50, 70)
            print('\nСпортивный автомобиль движется со скоростью (км/ч): ', self.speed)
            sleep(1)
            if self.speed > 60:
                print(f"{self.lawbreaker} {self.color} {self.name}")
                sleep(2)

    class WorkCar(Car):
        def show_speed(self):
            my_list3 = ['Lada', 'Niva', 'Peugeot', 'bus Ikarus', 'bus PAZ']
            self.speed = randint(0, 60)
            self.name = choice(my_list3)
            sleep(1)
            print('\nРабочий автомобиль движется со скоростью (км/ч): ', self.speed)
            if self.speed > 40:
                print(f"{self.lawbreaker} {self.color} {self.name}")
                my_list5 = ['на восток', 'на запад', 'на север', 'на юг']
                print('Машина повернула', choice(my_list5))
                sleep(2)

    class PoliceCar(Car):
        def pursuit(self):
            self.speed = randint(80, 90)
            if self.is_police == True:
                print(f'\nМигалки включены, это машина полиции, едет со скоростью {self.speed}')
            if self.is_police == False:
                print(f'\nМашина полиции едет со скоростью(км/ч) {self.speed} без мигалок. Необходимо снизить скорость или включить мигалки')

    c = Car()
    c.show_speed()

    t = TownCar()
    t.show_speed()
    t.go()
    t.stop()
    t.turn()

    s = SportCar()
    s.sport_car()
    s.go()
    s.stop()
    s.turn()

    w = WorkCar()
    w.show_speed()
    w.go()
    w.stop()
    w.turn()

    p = PoliceCar()
    p.pursuit()


main()
