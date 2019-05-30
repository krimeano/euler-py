"""
The radical of n, rad(n), is the product of the distinct prime factors of n. For example, 504 = 23 × 32 × 7, so rad(504) = 2 × 3 × 7 = 42.

If we calculate rad(n) for 1 ≤ n ≤ 10, then sort them on rad(n), and sorting on n if the radical values are equal, we get:

Let E(k) be the kth element in the sorted n column; for example, E(4) = 8 and E(6) = 9.

If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000).
"""
import mylib


def rad(n):
    out = 1
    for e in (d[0] for d in mylib.gather_dividers(n)):
        out *= e
    return out


up = 100000
nn = tuple((x, rad(x),) for x in range(1, up + 1))
nns = sorted(nn, key=lambda x: x[1])
print(nns[10000 - 1])
