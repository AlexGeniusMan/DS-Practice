def main():
    operation = input(
        """
Выберите операцию:
1. Сложение
2. Вычитание
3. Деление
4. Деление (целочисленное)
5. Модуль
6. Возвредение в степень
Введите номер: """)
    a = int(input("Введите число 1: "))
    if operation == "5":
        print(abs(a))
        return
    b = int(input("Введите число 2: "))
    if operation == "1":
        print(a + b)
    elif operation == "2":
        print(a - b)
    elif operation == "3":
        print(a / b)
    elif operation == "4":
        print(a // b)
    elif operation == "6":
        print(a ** b)


if __name__ == '__main__':
    main()
