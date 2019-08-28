"""
70 colored balls are placed in an urn, 10 for each of the seven rainbow colors.

What is the expected number of distinct colors in 20 randomly picked balls?

Give your answer with nine digits after the decimal point (a.bcdefghij).
"""
a = 7
b = 10
c = 20
d = a * b


def get_p(m, n):
    if not m:
        if not n:
            return 1
        return 0
    if m > n:
        return 0

    if m * b < n:
        return 0

    return b * (a - m) / (d - n)


def get_q(m, n):
    if not m:
        return 0

    if m > n:
        return 0

    if m * b < n:
        return 0

    return (b * m - n) / (d - n)


def get_s(m, n):
    if not m:
        if not n:
            return 1

    if m > n:
        return 0

    if m * b < n:
        return 0

    if m == n:
        return get_s(m - 1, n - 1) * get_p(m - 1, n - 1)

    return get_s(m - 1, n - 1) * get_p(m - 1, n - 1) + get_s(m, n - 1) * get_q(m, n - 1)


if __name__ == '__main__':
    for x in range(a + 1):
        for y in range(x, c):
            pv = get_p(x, y)
            qv = get_q(x, y)
            print(x, y,
                  '>', '%d/%d' % (d - b * x, d - y), '=', round(1000 * pv) / 1000,
                  '>', '%d/%d' % (b * x - y, d - y), '=', round(1000 * qv) / 1000,
                  '>', pv + qv
                  )

    for y in range(1, 21):
        ss = [get_s(x, y) for x in range(1, min(a + 1, y + 1))]
        m = sum([(i + 1) * ss[i] for i in range(len(ss))])
        print(y, sum(ss), m, ss)
