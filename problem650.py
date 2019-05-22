"""
S(5)=5736 , S(10)=141740594713218418 and S(100) mod 1000000007=332792866.

Find S(20000) mod 1000000007.
"""
import time

import mylib

mod = 1000000007

cached_dividers = dict()


def make_cached_dividers(n):
    for x in range(1, n + 1):
        cached_dividers[x] = mylib.gather_dividers(x)


cached_dmap = {1: {}}


def make_cached_dmap(n):
    dmap_minus = dict()
    for x in range(2, n + 1):
        dmap = cached_dmap[x - 1].copy()

        for dd in cached_dividers[x]:
            d = dd[0]
            p = len(dd)
            dmap_minus[d] = (d in dmap_minus and dmap_minus[d] or 0) - p
            dmap[d] = (d in dmap and dmap[d] or 0) + p * x

        for d in dmap_minus:
            dmap[d] = dmap[d] + dmap_minus[d]
        dmap = {d: p for (d, p) in dmap.items() if p}
        # print(x, dmap)
        cached_dmap[x] = dmap


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
    make_cached_dividers(k)
    print('dividers are cached', round(time.time() - t_start, 3), 's', cached_dividers[k])
    make_cached_dmap(k)
    print('dmap is cached', round(time.time() - t_start, 3), 's', cached_dmap[k])

    for i in range(1, k + 1):
        #     # print('-' * 70)
        ddd = cached_dmap[i]
        if not i % 100:
            print(i, len(ddd), round(time.time() - t_start, 3), 's')
        #     print(i, ddd)
        s = sum_dividers(ddd)
        #     # print(s)
        r = (r + s) % mod
    print('=' * 70)
    t_end = time.time()
    print(r, round(t_end - t_start, 3), 's')
