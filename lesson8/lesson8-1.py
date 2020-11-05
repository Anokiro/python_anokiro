# Урок 8, задача 1.
# Время года
def main():
    try:
        class Data:
            def __init__(self, data):
                self.data = data

            @classmethod
            def check_string(cls, data):
                data_list = []
                check_list = ''
                for i in data:
                    if i.isdigit():
                        check_list += i
                    elif i.isalpha() == False:
                        data_list.append(check_list)
                        check_list = ''
                if check_list != '':
                    data_list.append(check_list)
                if len(data_list) != 3:
                    print(f'Вы ввели {data_list}, значение некорректно (введите через пробел: чч мм гггг)')
                else:
                    print(f'Введенная Вами дата: ', end='')
                    for i in data_list:
                        print(f'{i}.', end='')
                return list(map(int, data_list))

            @staticmethod
            def valid_list(data):
                if 1 <= data[0] <= 31:
                    if 1 <= data[1] <= 12:
                        if 2020 >= data[2] >= 0:
                            return f'\nВсё ок'
                        else:
                            return f'\nНеверно введен год'
                    else:
                        return f'\nНеверно введен месяц'
                else:
                    return f'\nНеверно введен день'

        d = Data.check_string(input('Введите дату через пробел: чч мм гггг - '))
        print(Data.valid_list(d))

    except Exception as err:
        print('Должен быть 1 пробел.')

main()
