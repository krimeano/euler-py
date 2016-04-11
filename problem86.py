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

M = 2000
ss = dict((x ** 2, True) for x in range(1, 3 * M + 1))
print(M, ss)
tt = []


def find_mm_nn(a):
    out = []
    n_max = math.floor(max(((a - 1) / 2), a ** 0.5))
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


def find_brute(a):
    out = []
    for b in range(1, a + 1):
        for c in range(1, b + 1):
            s2 = a ** 2 + (b + c) ** 2
            if s2 not in ss:
                continue
            t = (a, b, c)
            # print(t, s2)
            out.append(t)
    return out


ttb = []
for a in range(1, 100 + 1):
    ttb += find_brute(a)
print(len(ttb))

uu = []
for t in ttb:
    u = (t[0], t[1] + t[2])
    if u not in uu:
        uu.append(u)

y = 0
uu1 = []
stored_tt = dict()
for a in range(1, M + 1):
    clean_tt = find_mm_nn(a) + find_2mn(a)

    stored_tt[a] = clean_tt
    tt = clean_tt[:]
    dd = mylib.find_composite_dividers(a)
    for d in dd:
        if d < 3 or d == a:
            continue
        if d in stored_tt:
            # print(a, 'stored', stored_tt[d])
            for t in stored_tt[d]:
                t1 = (a, t[1] * a // d)
                if t1 not in tt:
                    # print(a, ' <- ', t1)
                    tt.append(t1)
                # tt += [x for x in stored_tt[d]]
    uu1 += tt
    if not len(tt):
        continue
    z = 0

    for p in tt:
        k = p[1] // 2
        if p[1] > p[0]:
            k -= p[1] - p[0] - 1
        # k *= 3
        #
        # print(' ', p, k)
        z += k
    y += z
    print(a, tt, z, y)

# print(uu)
# print(uu1)
