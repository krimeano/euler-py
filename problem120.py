__author__ = 'sergeyp'


def solve():
    s = 0
    for x in range(3, 1001):
        y = (x - 1) // 2
        r = x * y * 2
        s += r
    return s


if __name__ == '__main__':
    print(solve())
