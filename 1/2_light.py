figure = input("1. Круг\n2. Прямоугольник\n3. Треугольник\nВведите номер: ")
if figure == "1":
    rad = int(input(" Введите радиус круга: "))
    print("S: ", 3.14 * rad ** 2)
elif figure == "2":
    dlina = int(input("Введите длину прямоугольника: "))
    shirina = int(input("Введите ширину прямоугольника: "))
    print("S: ",
           dlina * shirina)
elif figure == "3":
    osnov = int(input("Введение основание треугольника: "))
    visota = int(input("Введите высоту треугольника: "))
    print("S: ",
          0.5 * osnov * visota)
else:
    print("Неверный ввод.")
