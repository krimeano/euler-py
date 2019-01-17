import math


def hallway(n):
    zz = {}
    m = int((n - 1) ** 0.5)
    print(n, m)
    for a in range(2, m + 1):
        aa = a * a
        k = min(a - 1, int((n - aa) ** 0.5))
        # print(n, m, a, aa, k)
        for b in range(1, k + 1):
            bb = b * b
            # print(n, m, a, aa, k, b, bb)
            c = aa + bb
            print('   ', a, b, c)
            if c in zz:
                print('!!!')
                del zz[c]
            else:
                zz[c] = 1
    # print(zz, len(zz))
    return len(zz)


def solve():
    print('solving')
    # cases = ((5, 1), (100, 27), (1000, 233), (10 ** 6, 112168))
    cases = ((5, 1), (100, 27), (1000, 233))
    for c in cases:
        r = hallway(c[0])
        if r != c[1]:
            print('NOT SOVED WHEN n =', c[0], ' expected:', c[1], ' received:', r)
            break
    else:
        print('YEAH')
        # return hallway(10 ** 9)
    return 0


if __name__ == '__main__':
    print(solve())
