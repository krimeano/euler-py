"""
The smallest number m such that 10 divides m! is m=5.
The smallest number m such that 25 divides m! is m=10.

Let s(n) be the smallest number m such that n divides m!.
So s(10)=5 and s(25)=10.
Let S(n) be ∑s(i) for 2 ≤ i ≤ n.
S(100)=2012.

Find S(108).
"""

import math
import mylib


def p_to_m(n):
    max_p = 8 * math.log(10, n)
    if max_p < n:
        return []
    print(max_p)
    max_p = math.floor(max_p)

    out = [0] * max_p
    mp = []
    for x in range(max_p + 1):
        arr = []
        y = x
        while y:
            arr.append(y)
            y = y // n
        # print(x, arr)
        if sum(arr) > max_p:
            break
        mp.append(sum(arr))
    # print(mp)
    for i in range(len(mp)):
        # print(i, mp[i - 1], mp[i])
        for j in range(mp[i - 1], mp[i]):
            out[j] = i
    # out[mp[len(mp) - 1]] = len(mp) - 1
    return tuple([0] + out)


pm = {
    2: p_to_m(2),
    3: p_to_m(3),
    5: p_to_m(5),
    7: p_to_m(7)
}
for x in pm:
    print(x, pm[x], len(pm[x]))

M = 10 ** 8
pp = mylib.primes_from_file(M)

f_cashed = dict()


def get_f(dd):
    if dd in f_cashed:
        return f_cashed[dd]
    # print(' ', dd)
    d = dd[0]
    p = len(dd)
    if d in pm:
        p = pm[d][p]
    f_cashed[dd] = d * p
    return f_cashed[dd]


def find_y(x):
    if x in pp:
        return x
    ddd = mylib.gather_dividers(x)
    # print(x, ddd)
    dd = [get_f(y) for y in ddd]
    return max(dd)


# print(pp)
print()
s = 0
for x in range(2, M + 1):
    # f = 0
    y = find_y(x)
    # if x != y:
    #     f = mylib.factorial(y)
    # assert not f % x
    # if f:
    #     assert (f // x) % x
    print("\033[F\033[K", end="")
    s += y
    print(x, str(y) + '!', s)
print(s)
# print(f_cashed)
