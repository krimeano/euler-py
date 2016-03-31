import mylib
import math

L = 20
r = math.floor(L ** 0.5)
pp = sorted(x for x in mylib.primes_from_file(r) if x <= r)
print(pp)
for m in pp:
    print(m)
