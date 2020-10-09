#Урок 1, задача 2.
#Алгоритм конвертации секунд
def main():
    time_sec = int(input('Введите время в секундах: '))
    time_hour = time_sec / 3600
    time_min = (time_sec % 3600) / 60
    time_sec_remainder = (time_sec % 3600) % 60
    print('Ваше время: 'f'{time_hour:02.0f}:{time_min:02.0f}:{time_sec_remainder:02.0f}')
    print('\t\t\tчч:мм:cc')
main()

