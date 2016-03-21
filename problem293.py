import mylib, math

top = 10 ** 9
pp = mylib.make_primes_sieve_atkin(int(top + 100))

top_r = math.floor(top ** .5)
top_half = top // 2

bb = mylib.make_primes_sieve_atkin(top_r)
bb = mylib.make_primes_sieve_atkin(math.floor(top / max(bb)))

qq = sorted(pp)
bb_sorted = sorted(bb)
w = math.floor(math.log(top, 2))
rrr = [[2 ** x for x in range(1, w + 1)]]
print(rrr)
to_remove = set()
for b in sorted(bb):
    if b < 3:
        continue
    w = math.floor(math.log(top, b))
    mm = [1] + rrr[-1]
    nn = [b ** x for x in range(1, w + 1)]
    to_remove |= set(nn)
    rr = []
    for m in mm:
        for n in nn:
            r = m * n
            if r > top:
                break
            rr.append(r)
    rrr.append(sorted(rr))
    print("\033[F\033[K", end="")
    print(b, w)
aa = set()
for rr in rrr:
    aa |= set(rr)

aa ^= to_remove
# 2,4,6,8,12,16,18,24,30,32,36,48...
print(sorted(aa))
# print(sorted(to_remove))
j_max = len(qq)
j_min = 0
ff = []
print()
for a in sorted(aa):
    for j in range(j_min + 1, j_max + 1):
        q = qq[j]
        if q < a:
            j_min = j
            continue
        f = q - a
        if f > 1:
            print("\033[F\033[K", end="")
            print(a, q, f)
            ff.append(f)
            break
print(sum(ff))
