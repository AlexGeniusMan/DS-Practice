def circle():
    return print("Площадь круга: ", 3.14 * int(input("Введите радиус круга: ")) ** 2)


def rectangle():
    return print("Площадь прямоугольника: ",
                 int(input("Введите длину прямоугольника: ")) * int(input("Введите ширину прямоугольника: ")))


def triangle():
    return print("Площадь треугольника: ",
                 0.5 * int(input("Введите основание треугольника: ")) * int(input("Введите высоту треугольника: ")))


def main():
    figure = input("Выберите фигуру:\n1. Круг\n2. Прямоугольник\n3. Треугольник\nВведите номер: ")
    if figure == "1":
        circle()
    elif figure == "2":
        rectangle()
    elif figure == "3":
        triangle()
    else:
        print("Неверный ввод.")

if __name__ == '__main__':
    main()
