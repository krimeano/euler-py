import mylib


def binom_c(n, k):
    out = 1
    for x in range(1, k + 1):
        out *= (n - x + 1) / x
    return round(out)


def binom_dd(n, k):
    out = []
    ee = []
    for x in range(1, k + 1):
        out += mylib.find_dividers(n - x + 1)
        if x < 2:
            continue
        ee += mylib.find_dividers(x)
    # print("+", sorted(out),"\n-", sorted(ee))
    for x in ee:
        if x in out:
            ix = out.index(x)
            out = out[:ix] + out[ix + 1:]
    return tuple(sorted(out))


def binom_list(n):
    return [binom_c(n, x) for x in range(n // 2 + 1)]


def binom_list_dd(n):
    return [binom_dd(n, x) for x in range(n // 2 + 1)]


r = set()
for i in range(51):
    for j in range(i // 2 + 1):
        dd = binom_dd(i, j)
        dd_distinct = tuple(sorted(set(dd)))
        if len(dd) == len(dd_distinct):
            a = mylib.mult(dd)
            r.add(a)
            print(i, j, a, dd, len(r))

print(sum(r), sorted(r))
