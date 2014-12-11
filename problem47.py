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
