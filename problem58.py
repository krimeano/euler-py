"""
problem 58
"""
__author__ = 'palutser'
import mylib


def coil_generator():
    x = 1
    s = 0
    while True:
        s += 2
        yield [x + s, x + s * 2, x + s * 3, x + s * 4]
        x += s * 4


def solve():
    coils = coil_generator()

    numbers_prime = []
    numbers_complex = []
    r = 1
    i = 0
    coil = []
    while r >= 0.1:
        coil = coils.__next__()
        # print(coil)
        for x in coil:
            if mylib.is_prime(x):
                numbers_prime.append(x)
            else:
                numbers_complex.append(x)
        # print(numbers_prime)
        # print(numbers_complex)
        # print(len(numbers_complex), len(numbers_prime))
        r = len(numbers_prime) / (1 + len(numbers_complex) + len(numbers_prime))
        i += 1
        print(i, r, len(numbers_complex), len(numbers_prime))
    # print(numbers_prime)
    # print(numbers_complex)
    print(coil)
    return i * 2 + 1


if __name__ == '__main__':
    print(solve())
