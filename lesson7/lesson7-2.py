# Урок 7, задача 2.
# Расчет рахода ткани.
def main():
    from abc import ABC, abstractmethod

    class Clother(ABC):

        @abstractmethod
        def my_method_1_size(self):
            pass

        @abstractmethod
        def my_method_2_height(self):
            pass

    class MyClassCoat(Clother):
        # Конструктор класса MyClassCoat
        def __init__(self, size_decorator):
            self.size_decorator = size_decorator

        # Создаем свойство размера пальто
        @property
        def size_decorator(self):
            return self.__size_decorator

        # сеттер для создания свойств
        @size_decorator.setter
        def size_decorator(self, size_decorator):
            if size_decorator < 30:
                self.__size_decorator = 30
                print('Размер взят', self.__size_decorator)
            elif size_decorator > 80:
                self.__size_decorator = 80
                print('Размер взят', self.__size_decorator)
            else:
                self.__size_decorator = size_decorator

        def my_method_1_size(self):
            print('Потребление ткани на пальто: ', self.size_decorator / 6.5 + 0.5)
            return self.size_decorator / 6.5 + 0.5

        def my_method_2_height(self):
            pass

    class MyClassSuit(Clother):
        # Конструктор класса MyClassSuit
        def __init__(self, rost_decorator):
            self.rost_decorator = rost_decorator

        # Создаем свойство роста
        @property
        def rost_decorator(self):
            return self.__rost_decorator

        # сеттер для создания свойств
        @rost_decorator.setter
        def rost_decorator(self, rost_decorator):
            if rost_decorator < 100:
                self.__rost_decorator = 100
                print('Рост взят', self.__rost_decorator)
            elif rost_decorator > 200:
                self.__rost_decorator = 200
                print('Рост взят', self.__rost_decorator)
            else:
                self.__rost_decorator = rost_decorator

        def my_method_1_size(self):
            pass

        def my_method_2_height(self):
            print('Потребление ткани на костюм: ', 2 * self.rost_decorator + 0.3, '\n')
            print('-------------------------')
            return 2 * self.rost_decorator + 0.3

    mc = MyClassCoat(float(input('Введите число, размер пальто (30 - 80): ')))
    ms = MyClassSuit(float(input('Введите число, рост (100 - 200): ')))
    print('Общий объем потребляемой ткани равен: ', format(mc.my_method_1_size() + ms.my_method_2_height(), '.2f'))


main()
