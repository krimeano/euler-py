"""
It is easily proved that no equilateral triangle exists with integral length sides and integral area.
However, the almost equilateral triangle 5-5-6 has an area of 12 square units.

We shall define an almost equilateral triangle to be a triangle
for which two sides are equal and the third differs by no more than one unit.

Find the sum of the perimeters of all almost equilateral triangles with integral side lengths
and area and whose perimeters do not exceed one billion (1,000,000,000).

2 pythagorean triangles (a, b, c) --> triangle (c, c, 2a), (c, c, 2b)

S = ab
p = 2a+c, 2b+c

2a = c ± 1,
2b = c ± 1

a = m2 - n2
b = 2mn
c = m2 + n2

a) 2a = 2m2 - 2n2 = m2 + n2 ±1
m2 = 3n2 ± 1
m = 3x ± 1  -->
m2 = 9x2 ± 6x + 1 = 3n2 ± 1 => m2 = 3n2 + 1 => 2a = c + 1
a = 3n2 + 1 - n2 = 2n2 + 1
b = 2 * sqrt(3n2 + 1) * n
c = 3n2 + 1 + n2 = 4n2 + 1
S = ab = 2n * (2n2 + 1) *  sqrt(3n2 + 1)  lil more than 4*sqrt(3) * n4
P = 2a + 2c = 2m2 - 2n2 + 2m2 + 2n2 = 4m2 = 12n2 + 4
max n = (L / 4 / sqrt(3)) ** 0.25

b) 2b = 4mn = m2 + n2 ± 1
m2 - 4mn + n2 ± 1 = 0
D / 4 = 4n2 - n2 ± 1 = 3n2 ± 1 = 3n2 + 1 = k2

m = 2n ± sqrt(3n2 + 1)
m > n -> 2n - sqrt(3n2 + 1) > n -> n > sqrt(3n2 + 1) -> n2 > 3n2 + 1 - impossible
=> m = 2n + sqrt(3n2 + 1) = 2n + k
m2 = 7n2 + 4nk + 1
a = m2 - n2 = 6n2 + 4nk + 1
b = 2n(2n + k) = 4n2 + 2nk
c = 8n2 + 4nk + 1
P = 2b + 2c = 8n2 + 4nk + 16n2 + 8nk + 2 = 24n2 + 12nk + 2  lil more than 12*(2 + sqrt(3))*n2
S = ab = (6n2 + 4nk + 1) * (4n2 + 2nk) = 24n4 + 16n3*k + 4n2 + 12n3 * k + 8n2(3n2+1) + 2nk
= 48n4 + 28kn3 + 12n2 + 2nk   lil more than 4n4 * (12 + 7 * sqrt((3)

"""
import math
import mylib

L = 1000000000
r = math.floor((L / 12) ** (1 / 2))
print(r)

s = 0
for n in range(1, r + 1):
    n2 = n ** 2
    m2 = 3 * n2 + 1
    m = round(m2 ** .5)
    if m ** 2 != m2:
        continue
    w = 2 * n + m
    w2 = w ** 2
    print(n, n2, m2, w2, mylib.find_gcd(m, n), mylib.find_gcd(w, n))

    a = m2 - n2
    b = 2 * m * n
    c = m2 + n2

    x = w2 - n2
    y = 2 * w * n
    z = w2 + n2

    pc = 2 * (a + c)
    if pc <= L:
        s += pc
    pz = 2 * (y + z)

    if pz <= L:
        s += pz
    print((a, b, c,), pc, (x, y, z,), pz)

print(s)
