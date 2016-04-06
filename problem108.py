import math, mylib


def ww_to_a(w_list):
    out = 1
    for x in w_list:
        out *= x ** w_list[x]
    return out


def ww_to_n(w_list):
    out = 1
    for x in w_list:
        out *= w_list[x] + 1
    return out


m = 0
s = 2 * 3 * 5 * 7
for n in range(s, 1000, s):
    if mylib.is_prime(n):
        continue
    pd = mylib.find_dividers(n)
    if len(pd) < 4:
        continue
    dd = mylib.find_composite_dividers(n)
    print(n, len(dd), dd)
    ss = set()
    for a in dd:
        for b in dd:
            if b > a:
                continue
            if mylib.find_gcd(a, b) > 1:
                continue
            z = a + b
            x = round(n * z / b)
            y = round(n / a) * z
            print(a, b, x, y, x * y / (x + y))
            ss.add((min(x, y), max(x, y, )))

    sl = len(ss)
    if sl > m:
        m = sl
        print(n, sl, (len(mylib.find_composite_dividers((n ** 2))) + 1)/2)
