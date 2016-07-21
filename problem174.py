"""
https://projecteuler.net/problem=174
We shall define a square lamina to be a square outline with a square "hole" so that the shape possesses vertical
and horizontal symmetry.

Given eight tiles it is possible to form a lamina in only one way: 3x3 square with a 1x1 hole in the middle.
However, using thirty-two tiles it is possible to form two distinct laminae.


If t represents the number of tiles used, we shall say that t = 8 is type L(1) and t = 32 is type L(2).

Let N(n) be the number of t ≤ 1000000 such that t is type L(n); for example, N(15) = 832.

What is ∑ N(n) for 1 ≤ n ≤ 10?


t_max = 10**6
aa - bb = t
b % 2 = a % 2
0 < b < a
a = b + 2d
(b + 2d)**2 - bb = bb + 4bd + 4dd - bb = 4d(b+d) = t
d_min = 1
d_max ~ b_min=1
4dd + 4d - t <=0
D/4 = 4 + 4t
d_max = (-2 ± 2 * (t+1) ** .5) / 4 = ((t+1) /4) ** 0.5 - 0.5
b(d,t) = t/4d - d
b_max = t/4 - 1
"""
import mylib, math

t_max = 10 ** 6
d_max = math.floor(((t_max + 1) / 4) ** 0.5 - 0.5)
ll = {}
for d in range(1, d_max + 1):
    b_max = math.floor(t_max / d / 4 - d)
    print(d)
    for b in range(1, b_max + 1):
        t = 4 * d * (b + d)
        a = b + 2 * d
        if t not in ll:
            ll[t] = set()
        ab = (a, b, d)
        ll[t].add(ab)
        # print(t, ll[t])
nn = [ll[x] for x in ll if len(ll[x]) == 15]
ff = [ll[x] for x in ll if len(ll[x]) <= 10]
print('-' * 79)
print(len(nn))
print(len(ff))
