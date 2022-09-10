def main():
    numbers = []
    total = 0
    while True:
        numbers.append(int(input("Enter a number: ")))
        if sum(numbers) == 0:
            break
    for number in numbers:
        total += number ** 2
    print(total)


if __name__ == '__main__':
    main()
