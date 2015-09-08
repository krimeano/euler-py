"""
problem 57
"""
__author__ = 'palutser'


def genRatio():
    a, b = 0, 1
    while True:
        yield (a + b, b)
        a, b = b, a + 2 * b


def solve():
    gr = genRatio()
    n = 0
    for i in range(1001):
        r = gr.__next__()
        rs = [str(x) for x in r]
        L0 = len(rs[0])
        L1 = len(rs[1])
        if L0 > L1:
            n += 1
            print(i, L0, L1, '/'.join(rs), r[0] / r[1])
    return n


if __name__ == '__main__':
    print(solve())
