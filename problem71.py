__author__ = 'krimeano'

import math, mylib


def solve():
    result = 0
    f0 = 3 / 7
    print(3, '/', 7, '=', f0)
    print('-' * 79)
    best_result = (1, 1, 1, 1, [], [])
    for x in range(1000000, 1, -1):
        n = math.floor(f0 * x)
        f = n / x
        d = f0 - f
        if d and d < best_result[2]:
            best_result = (n, x, d, f, mylib.find_dividers(n, distinct=True), mylib.find_dividers(x, distinct=True))
            print(best_result)
    print('-' * 79)
    print(best_result)
    return best_result[0]


if __name__ == '__main__':
    r = solve()
    print('\n' + '-' * 79)
    print(r)
