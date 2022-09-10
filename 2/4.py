def main():
    a = [1, 2, 3, 4, 2, 1, 3, 4, 5, 6, 5, 4, 3, 2]
    b = ['a', 'b', 'c', 'c', 'c', 'b', 'a', 'c', 'a', 'a', 'b', 'c', 'b', 'a']
    result = {}
    for i, el in enumerate(b):
        if el in result:
            result[el] += a[i]
        else:
            result[el] = a[i]
    print(result)


if __name__ == '__main__':
    main()
