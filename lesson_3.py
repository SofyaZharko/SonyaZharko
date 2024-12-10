print("-------------number1-------------")

n = int(input("Введите число от 1 до 100: \n"))
sum = 0
for i in range(1, n+1):
	sum += i**3
print(sum)

print("-------------number2-------------")



def print_multiplication_table():
    # Заголовок таблицы
    print("    ", end="")
    for i in range(1, 10):
        print(f"{i:>4}", end="")
    print()

    # Разделитель
    print("    " + "----" * 9)

    # Основной цикл для формирования строк таблицы
    for i in range(1, 10):
        print(f"{i:>2} |", end="")
        for j in range(1, 10):
            print(f"{i * j:>4}", end="")
        print()

# Вызов функции для отображения таблицы
print_multiplication_table()


