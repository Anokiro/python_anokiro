#Урок 1, задача 1.
#Небольшая программа для расчета купли-продажи ценной бумаги.
def main():
    print(' -> Перед Вами простая программа расчета прибыли/убытков <- ')
#Зададим переменные
    COMMISSION_BROKER = 0.05 #коммисия брокера при продаже бумаги
    STOCK_PRICE = 185        #цена покупки акции
    sale_price = int(input('Введите цену акции в настоящее время: '))
    real_price = sale_price - (sale_price * COMMISSION_BROKER)
    margin = real_price - STOCK_PRICE
#Напишем условие
    if real_price > STOCK_PRICE and real_price >= STOCK_PRICE + 15:
        print('Отличная цена для продажи!')
        print(f'Ваша выгода составляет: %d руб.' % (margin))
    elif real_price > STOCK_PRICE:
        print('Можно продать бумагу (прибыль/безубыток).')
        print(f'Ваша выгода составляет: %d руб.' % (margin))
    else:
        print('Вы в убытках. Продавать бумагу рано.')
main()

