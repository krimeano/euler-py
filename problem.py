import mylib


def sigma2(x):
    return sum(y ** 2 for y in mylib.find_composite_dividers(x))


m = 64000000

ss = dict()
print("making squares \n")
for a in range(1, m * 2):
    ss[a ** 2] = a
    print("\033[F\033[K", a)
# ss = dict((x ** 2, x) for x in range(1, m * 2))
print("\033[F\033[K", end="")
print("\033[F\033[K", end="")
print("finding sigma2 as perfect squares")
result = []
for a in range(1, m + 1):
    s = sigma2(a)
    print("\033[F\033[K", a, s)
    if s in ss:
        print('   ', ss[s], "\n")
        result.append(a)
print("\033[F\033[K", end="")
print(sum(result))
