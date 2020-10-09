# Урок 6, задача 6.
# Задача со спортсменом
def main():
    day_result = int(input("Введите результат за первый день (км.): "))
    limit_result = int(input("Какое количество км. Вы хотели бы пробежать в сумме: "))
    progress = 0.1 #Спортсмен увеличивает результат каждый день на 10%
    day_counter = 1
    if day_result >= limit_result:
        print("Лимит превышен. Снизьте интенсивность тернировок.")
    else:
        while day_result < limit_result:
            day_counter += 1
            day_result += (day_result * progress)
            print(f"{day_counter:.0f}-й день: {day_result:.2f}")
    print(f"на {day_counter}-й день спортсмен достиг результата - не менее {day_result:.0f} км.")
main()

