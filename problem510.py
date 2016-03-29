import mylib, math

L = 10 ** 9
r = math.floor(L ** 0.5)

s = 0
pp = tuple(x + 1 for x in range(r))
dd = dict()
ff = dict()
for q in pp:
    for p in pp:
        if p > q:
            break
        t = p * q / (p + q)
        if not t % 1:
            t = round(t)
            a = p ** 2
            b = q ** 2
            c = t ** 2
            d = (a, b, c)
            f = b / a
            print("\033[F\033[K", d, f)
            if f not in ff:
                print()
                ff[f] = True
                dd[d] = True
print("\033[F\033[K")
# print(dd)
# print(ff)

print("summation\n")

for d in dd:
    x = L // d[1]
    m = x * (x + 1) // 2
    print("\033[F\033[K", d, "x", x, " xx ", m)
    s += sum(d) * m
print("\033[F\033[K")

print(s)
