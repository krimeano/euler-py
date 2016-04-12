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


def p_to_m(n):
    max_p = 8 * math.log(10, n)
    if max_p < n:
        return []
    max_p = math.floor(max_p)
    print(max_p)

    out = [0] * max_p
    mp = []
    for x in range(max_p + 1):
        arr = []
        y = x
        while y:
            arr.append(y)
            y = y // n
        print(x, arr)
        if sum(arr) > max_p:
            break
        mp.append(sum(arr))
    print(mp)
    for i in range(len(mp)):
        for j in range(mp[i], len(out)):
            out[j] = max(i, out[j])
    return out


pm = {
    2:p_to_m(2),
    3: p_to_m(3),
    5: p_to_m(5),
    7: p_to_m(7)
}
for x in pm:
    print(x, pm[x])
