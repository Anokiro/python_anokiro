# Урок 1, задача 5.
#Просчет финансоваого состояния компании
def main():
    revenue = int(input('Введите значение выручки компании: '))
    costs = int(input('Введите значение издержек компании: '))
    if revenue > costs:
        rent = float(revenue / costs)
        print(f"Баланс вашей компании положительный (прибыль):\n \
            рентабельность составляет: {rent:.2f}%.")
        employees = int(input('Введите численность сотрудников компании: '))
        profit_employees = revenue / employees
        print(f"Прибыль на одного сотрудника составляет: {profit_employees:.2f} руб.")
    if costs > revenue:
        print('Баланс вашей компании отрицательный (убыток).')
main()

