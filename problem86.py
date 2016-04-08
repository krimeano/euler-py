"""
It can be shown that there are exactly 2060 distinct cuboids, ignoring rotations, with integer dimensions,
up to a maximum size of M by M by M, for which the shortest route has integer length when M = 100.
This is the least value of M for which the number of solutions first exceeds two thousand;
the number of solutions when M = 99 is 1975.


M => a >= b >= c

aa + (b+c)^2 = ss
b+c = d
a = M
d <= 2M

M = mm - nn, 2mn
d = 2mn, mm - nn

n_min = 2
m_min = n_max+1

1) a = mm - nn = 2n + 1
n_max = (a - 1) / 2
2mn <= 2M
m <= M
m_max = M

"""
import math, mylib

M = 100
ss = dict((x ** 2, True) for x in range(1, 2*M + 1))
print(M, ss)
tt = []


def find_mm_nn(a):
    out = []
    n_max = math.floor(min(((a - 1) / 2), a ** 0.5))
    if not n_max:
        return out
    for n in range(1, n_max + 1):
        nn = n * n
        mm = a + nn
        if not mm or mm <= nn or mm not in ss:
            continue
        m = round(mm ** .5)
        d = 2 * m * n
        if d > 2 * a:
            continue
        t = (a, d)
        out.append(t)
        # print(t)
    return out


def find_2mn(a):
    out = []
    if a % 2:
        return out
    dd = mylib.find_composite_dividers(a // 2)
    _dd = dd[::-1]
    l = len(dd)
    # print(a, dd)
    for i in range(l // 2):
        d = _dd[i] ** 2 - dd[i] ** 2
        if d > 2 * a:
            continue
        t = (a, d)
        out.append(t)
    return out


y = 0
for a in range(1, M + 1):
    tt = find_mm_nn(a) + find_2mn(a)
    if not len(tt):
        continue
    z = 0

    for p in tt:
        k = p[1] // 2
        if p[1] > p[0]:
            k -= p[1] - p[0] - 1
        print(' ', p, k)
        z += k
    y += z
    print(a, tt, z, y)
