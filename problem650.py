"""
S(5)=5736 , S(10)=141740594713218418 and S(100) mod 1000000007=332792866.

Find S(20000) mod 1000000007.
"""
import time

import mylib

mod = 1000000007
cached_dividers = [((1),)]


def make_dividers(n):
    m = n
    dmap = dict()
    while m > 1:
        p = n - 1 + (m - n) * 2
        # print(m, p, ddd)
        if p:
            for dd in cached_dividers[m]:
                d = dd[0]
                q = len(dd)
                dmap[d] = (d in dmap and dmap[d] or 0) + q * p
        m = m - 1
    return dmap


mm = dict()


def get_multiplier(d, p):
    k = tuple((d, p))
    # print(k)
    if k not in mm:
        mm[k] = (pow(d, p + 1, mod) - 1) * pow(d - 1, mod - 2, mod) % mod
    return mm[k]


def sum_dividers(dmap):
    out = 1
    for d in dmap:
        out = out * get_multiplier(d, dmap[d]) % mod
    return out


if __name__ == '__main__':

    # print(mylib.find_dividers(mod - 2))
    t_start = time.time()
    k = 20000
    r = 0

    for i in range(1, k + 1):
        cached_dividers.append(mylib.gather_dividers(i))

    print(cached_dividers[-10:])

    for i in range(1, k + 1):
        # print('-' * 70)
        ddd = make_dividers(i)
        if not i % 100:
            print(i, len(ddd), round(time.time() - t_start, 3), 's')
        # print(ddd)
        s = sum_dividers(ddd)
        # print(s)
        r = (r + s) % mod
    print('=' * 70)
    t_end = time.time()
    print(r, round(t_end - t_start, 3), 's')
