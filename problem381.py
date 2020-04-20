import mylib

L = 10 ** 8
pp = mylib.primes_from_file(L)

k = {1: 3, 3: 1, 5: 7, 7: 5}


def s3(p):
    return (p * k[p % 8] - 3) // 8


sigma = 0
for a in pp:
    if a < 5 or a >= L:
        continue
    sa = s3(a)
    sigma += sa
    print("\033[F\033[K", end="")
    print(a, sa)
print(sigma)
