import numpy as np


def main():
    frame = np.random.rand(3, 3)
    print(frame.flatten(order='C'))


if __name__ == '__main__':
    main()
