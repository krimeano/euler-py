import mylib, math

__author__ = 'krimeano'

dividers_hash = []


def is_proper_fraction(n, d):
    return n and n < d and not \
        len(dividers_hash[n] & dividers_hash[d])


def dividable_by_any(n, dd):
    for x in dd:
        if not n % x:
            return True
    return False


def count_fractions_old(v):
    for i in range(0, v + 1):
        if len(dividers_hash) <= i:
            dividers_hash.append(set(mylib.find_dividers(i, distinct=True)))
    print('hash constructed to', len(dividers_hash) - 1)
    out = 0
    for d in range(2, v + 1):
        for n in range(1, d):
            r = is_proper_fraction(n, d)
            out += r
            if not d % 1000 and not n % 1000:
                print(n, '/', d, out)
                # print(n, '/', d, '=', r)
    return out


def count_fractions_for_denominator(d):
    dd = mylib.find_dividers(d, distinct=True)
    if len(dd) == 1:
        if dd[0] == d:
            return d - 1
        return int((dd[0] - 1) * d / dd[0])

    out = d
    for x in dd:
        out = (x - 1) * out / x
    return out
    # nn = (([1] * (dd[0] - 1) + [0]) * int(d / dd[0]))[:-1]
    #
    # # print(d, dd, nn)
    # for x in dd[1:]:
    #     for y in range(x - 1, d - 1, x):
    #         nn[y] = 0
    # # print(d, dd, nn)
    # return sum(nn)


def count_fractions(v):
    out = 0
    for d in range(2, v + 1):
        r = count_fractions_for_denominator(d)
        # print (r, 'for', d)
        out += r
        if not d % 1000:
            print(d, out)
    # print(out)
    return out


def test():
    v = 8
    e = 21
    return count_fractions(v) == e


def solve():
    return count_fractions(1000000)
# 10: 31
# 100: 3043
# 1000: 304191
# 10000: 30397485

if __name__ == '__main__':
    if test():
        print('-' * 79)
        print('TEST PASSED; SOLVING')
        print('-' * 79)
        print(solve())
    else:
        print('NOT SOLVED YET')
