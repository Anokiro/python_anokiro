# Урок 6, задача 7.
# Списки фирм
def main():
    file = open("lesson5-7.txt", 'r', encoding='utf-8')
    total_list = []
    total_list_loss = []
    result = {}
    result_profit = {}
    result_loss = {}
    profit_list = []
    for line in file:
        firm_name, ownership, income, cost = line.split()
        profit = int(income) - int(cost)
        if profit > 0:
            profit_list.append(int(profit))
            print(firm_name, 'прибыль составляет: ', profit)
            result[firm_name] = profit
        else:
            print(firm_name, 'понесла убытки.')
            result_loss[firm_name, 'loss_firms'] = profit
    average_profit = sum(profit_list) / len(profit_list)
    print('Средняя прибыль составляет (безубыточные фирмы): ', average_profit)
    print('-------------------------------------------------------------------')
    result_profit['average_profit'] = average_profit
    total_list.append(result)
    total_list.append(result_profit)
    total_list_loss.append(result_loss)
    print(total_list)
    print(total_list_loss)
    """Записываем данные во второй файл"""
    file2 = open("lesson5-7(2).txt", 'w', encoding='utf-8')
    file2.write(str(total_list))
    file2.write(str(total_list_loss))
    file.close()
    file2.close()
    """Открываем файл .json и записываем в него информацию из второго файла .py"""
    json_converting()

def json_converting():
    import json
    file_json = open('lesson5-7.json', 'w', encoding='utf-8')
    file_python = open('lesson5-7(2).txt', 'r', encoding='utf-8')
    for line in file_python:
        json.dump(line, file_json)
    print('Произведена сериализация в файл', file_json.name)
    file_json.close()
    file_python.close()


main()
