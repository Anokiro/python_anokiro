# Урок 5, задача 6.
# Вычисление суммы времени занятий
def main():
    file = open("lesson5-6.txt", 'r', encoding='utf-8')
    result = {}
    for line in file:
        num_list = []
        for word in line.split():
            num = ''
            for unit in word:
                if unit.isdigit():
                    num = num + unit
                else:
                    if num != '':
                        num_list.append(int(num))
                        num = ''
            if num != '':
                num_list.append(int(num))
        result[line.split()[0].rstrip(':')] = sum(num_list)
    print(result)
    file.close()


main()
