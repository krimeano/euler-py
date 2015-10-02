__author__ = 'sergeyp'
import math


def solve():
    r = 0

    with open("p099_base_exp.txt", "r") as f:
        aa = [tuple(int(y) for y in x.split(',')) for x in f.readlines()]

    max_e = 0
    for i in range(len(aa)):
        a = aa[i]
        e = math.log(a[0]) * a[1]
        if e > max_e:
            max_e = e
            r = i

    print(r, max_e)
    return r + 1


if __name__ == '__main__':
    print(solve())
