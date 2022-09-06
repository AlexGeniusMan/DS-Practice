from math import sqrt


def main():
    a = float(input("Введите сторону 1: "))
    b = float(input("Введите сторону 2: "))
    c = float(input("Введите сторону 3: "))
    p = (a + b + c) / 2
    print(sqrt(p * (p - a) * (p - b) * (p - c)))


if __name__ == '__main__':
    main()
