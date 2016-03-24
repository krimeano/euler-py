"""
An even positive integer N will be called admissible, if it is a power of 2
or its distinct prime factors are consecutive primes.
The first twelve admissible numbers are 2,4,6,8,12,16,18,24,30,32,36,48.

If N is admissible, the smallest integer M > 1 such that N+M is prime, will be called the pseudo-Fortunate number for N.

For example, N=630 is admissible since it is even and its distinct prime factors are the consecutive primes 2,3,5 and 7.
The next prime number after 631 is 641; hence, the pseudo-Fortunate number for 630 is M=11.
It can also be seen that the pseudo-Fortunate number for 16 is 3.

Find the sum of all distinct pseudo-Fortunate numbers for admissible numbers N less than 10**9.
"""

import math
import mylib

top = 10 ** 9

pp_100 = sorted(mylib.primes_from_file(100))
bb = []
m = 1
for x in pp_100:
    m *= x
    if m >= top:
        m //= x
        break
    bb.append(x)
print(bb, m)

rrr = [[1]]
for b in bb:
    mm = sorted(rrr[len(rrr) - 1])
    p = math.floor(math.log(top, b))
    nn = [b ** (x + 1) for x in range(p)]
    rr = []
    for m in mm:
        for n in nn:
            r = m * n
            if r >= top:
                break
            rr.append(r)
    rrr.append(rr)

aa = []

for rr in rrr[1:]:
    aa += rr
aa = sorted(aa)
print(aa[-10:])
pp = sorted(mylib.primes_from_file(top))
print()
i_max = len(pp)
i_min = 0
ff = []
for a in aa:
    for i in range(i_min, i_max):
        p = pp[i]
        f = p - a
        print("\033[F\033[K", a, p, f)
        if f > 1:
            print("\033[F\033[K", a, p, f)
            ff.append(f)
            break
        i_min = i - 1
print(sum(ff))
