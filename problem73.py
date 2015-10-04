import mylib, math


def is_proper_fraction(n, d):
    return n and n < d and not \
        len(set(mylib.find_dividers(n, distinct=True)) & set(mylib.find_dividers(d, distinct=True)))


def solve():
    ff = []
    min_f, max_f = 1 / 3, 1 / 2
    r = 0
    for d in range(2, 12001):
        if not d % 100:
            print(d)
        for n in range(math.floor(min_f * d), math.ceil(max_f * d)):
            if mylib.hcf(n, d) == 1:
                r += 1
    return r


if __name__ == '__main__':
    print(solve())
