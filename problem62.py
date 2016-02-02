import math


def solve():
    cubes = dict()
    l_max = 0
    for i in range(1, 10000):
        c = i ** 3
        sc = ''.join(sorted(str(c)))
        if sc not in cubes:
            cubes[sc] = []
        cubes[sc].append(c)
        l = len(cubes[sc])
        if l > l_max:
            l_max = l

        if l == l_max:
            print(len(cubes[sc]), cubes[sc])


if __name__ == '__main__':
    solve()
