import mylib, sys

L = 10 ** 2
pp = mylib.make_primes_sieve_atkin(L)


def my_fact2(p):
    out = 1
    if p < 10:
        for x in range(1, p - 4):
            out = (out * x) % p
        return out
    out = 24 % p
    for x in range(5, (p + 1) // 2):
        out = (((p - out) * x) % p * x) % p
    return out


def s3(p):
    return (my_fact2(p) * 9) % p


sigma = 0
for a in pp:
    if a < 5:
        continue
    sa = s3(a)
    sigma += sa
    print("\033[F\033[K", end="")
    print(a, sa)
print(sigma)
