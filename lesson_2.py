

x, y = input("Введите числа через пробел:").split()
if x.isdigit() and y.isdigit():
    x, y = map(int, (x, y))
    if y != 0:
        print("Результат деления:", x/y)
    else:
        print("Деление на ноль невозможно")
else:
    print("Вводите целые числа")



s = input("Введите стоимость покупок:")
if s.isdigit():
    sum = int(s)
    if sum > 20:
        discount = sum * 0.65
        print(f"{discount} руб. конечная цена, {sum - discount} руб. скидка")
    else:
        print(f"{sum} руб. конечная цена, {0} руб. скидка")
else:
    print("Введите стоимость покупок")


    number = input("Введите число от 1 до 12: \n")
Months = ["Январь - Зима", "Февраль - Зима", "Март - Весна", "Апрель - Весна", "Май - Весна", "Июнь - Лето", "Июль - Лето", \
          "Август - Лето", "Сентябрь - Осень", "Октябрь - Осень", "Ноябрь - Осень", "Декабрь - Зима"]
if number.isdigit():
    number = int(number)
    if number >= 1 and number <= 12:
        print(Months[number-1])
    else:
        print("Такого не существует. Всего 12 месяцев в году!")
else:
    print("Введи целое число от 1 до 12!!!")