from math import sqrt

a = float(input("Сторона a: "))
b = float(input("Сторона b: "))
c = float(input("Сторона c: "))
p = (a + b + c) / 2
print(sqrt(p * (p - a) * (p - b) * (p - c)))
