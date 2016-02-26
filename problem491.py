from datetime import datetime

fact = [1]


def get_n_elements(n, ss):
    l = len(ss)
    out = set()

    if n == l:
        out.add(tuple(ss[:]))
        return out
    for i in range(0, l - n + 1):
        x = (ss[i],)
        if n > 1:
            for y in get_n_elements(n - 1, tuple(ss[i + 1:])):
                out.add(x + y)
        else:
            out.add(x)
    return out


def count_variants(ss, no_leading_zeroes=False):
    l = len(ss)
    v = fact[l] / 2 ** (l - len(set(ss)))
    if no_leading_zeroes and ss[0] == 0:
        v -= count_variants(ss[1:])
    return v


if __name__ == '__main__':
    t1 = datetime.now()
    ss = [int(x) for x in '00112233445566778899']
    total = sum(ss)
    k = len(ss) // 2
    f = 1
    for i in range(1, k + 1):
        f *= i
        fact.append(f)
    n = 0
    aa = get_n_elements(k, ss)
    for a in aa:
        c = sum(a)
        if abs(total - 2 * c) % 11:
            continue
        n += count_variants(a, True) * count_variants(a)
    t2 = datetime.now()
    print(n, t2 - t1)
