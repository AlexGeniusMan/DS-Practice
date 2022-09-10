def main():
    counter = 0
    n = int(input('Enter a number: '))
    for number in range(1, n+1):
        for i in range(1, number+1):
            if counter >= n:
                break
            print(number, end=' ')
            counter += 1


if __name__ == '__main__':
    main()
