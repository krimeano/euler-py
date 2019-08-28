import math
import time

rr = set()
rr.add(1)
M = 10 ** 10

r3 = math.floor(M ** (1 / 3))
print(M, r3)

t = time.time()
for a in range(2, r3 + 1):
    r2 = math.floor((M / a) ** 0.5)
    for b in range(a, r2 + 1):
        r1 = min(a * b, math.floor(M / a / b))
        for c in range(b, r1 + 1):
            r = a * b * c
            rr.add(r)
            print(r3, a, r2, b, r1, c, r, len(rr), time.time() - t)
