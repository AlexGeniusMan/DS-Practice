figure = input("1. Круг\n2. Прямоугольник\n3. Треугольник\nВведите номер: ")
if figure == "1":
    print("S: ", 3.14 * int(input("Радиус круга: ")) ** 2)
elif figure == "2":
    print("S: ",
          int(input("Длина прямоугольника: ")) * int(input("Ширина прямоугольника: ")))
elif figure == "3":
    print("S: ",
          0.5 * int(input("Основание треугольника: ")) * int(input("Высота треугольника: ")))
else:
    print("Неверный ввод.")
