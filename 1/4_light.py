from math import sqrt

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))
p = (a + b + c) / 2
print(sqrt(p * (p - a) * (p - b) * (p - c)))
