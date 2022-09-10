operation = input("""
Выберите операцию:
1. Выполнить сложение
2. Выполнить вычитание
3. Выполнить деление (не целочисленное)
4. Выполнить деление (целочисленное)
5. Выполнить модуль
6. Выполнить возведение в степень
Введите номер: """)
a = int(input("Введите число 1: "))
b = int(input("Введите число 2: "))
if operation == "1":
    print(a + b)
elif operation == "2":
    print(a - b)
elif operation == "3":
    print(a / b)
elif operation == "4":
    print(a // b)
elif operation == "5":
    print('Модуль числа 1:', abs(a))
elif operation == "6":
    print(a ** b)
