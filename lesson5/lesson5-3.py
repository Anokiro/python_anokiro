# Урок 5, задача 3
# Вычисление зарплаты
def main():
    file = open("lesson5-3.txt", 'r', encoding='utf-8')
    min_rate = 20000.0
    list = []
    list2 = []
    list3 = []
    for i in file:
        splitt = i.split()
        list2.append(i)
        for j in splitt:
            check = j.isalpha()
            if check == False:
                list.append(float(j))
                list3.append(float(j))
                if list[0] < min_rate:
                    print(f"Доход меньше 20 тыс. руб.: {list2[0]}", end='')
                    list.clear()
                    list2.clear()
                else:
                    list.clear()
                    list2.clear()
    print(f"\nСредняя величина дохода всех сотрудников составляет: {sum(list3) / 10:.2f}")
    file.close()

main()
