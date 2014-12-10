"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2^2 × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
"""
__author__ = 'sergeyp'

import mylib


def solve():
    a = 0
    for a in range(1000, 1000000):
        d = mylib.find_dividers(a, distinct=True)
        if len(d) < 4:
            continue
        c = False
        e = []
        for b in range(a + 1, a + 4):
            dd = mylib.find_dividers(b, distinct=True)
            if len(dd) < 4:
                c = True
                break
            e.append(str(b) + ' ' + str(dd))
        if len(e) > 2:
            print(a, d, e)
        if not c:
            break

    return a


if __name__ == '__main__':
    print(solve())
