# Урок 6, задача 3.
# Работник
def main():
    class Worker:
        def __init__(self):
            self.name = 'Anton'
            self.surname = 'Ivanov'
            self.position = 'specialist'
            self._income = {"wage": 20000, "bonus": 5000}

    class Position(Worker):
        def get_full_name(self):
            print(f'{self.name} {self.surname}')

        def get_total_income(self):
            total = self._income['wage'] + self._income['bonus']
            print('Доход равен:', total)

    p = Position()
    p.get_full_name()
    p.get_total_income()

main()
