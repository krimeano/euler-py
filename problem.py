import mylib

g = 13
for x in range(5, 10 ** 15 + 1):
    g += mylib.find_gcd(x, g)
    print("\033[F\033[K", end='')
    print(x, g)

