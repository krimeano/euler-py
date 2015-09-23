__author__ = 'palutser'


def pretender_generator():
    a = 1010101030
    b = 40
    while True:
        yield a
        a += b
        b = 100 - b


def solve():
    prets = pretender_generator()
    p = prets.__next__()
    max_p = int(1929394959697989990 ** 0.5)
    expected = '1234567890'

    print(max_p)
    r = []
    # return r
    while p < max_p:
        s = str(p ** 2)
        m = ''.join(s[x] for x in range(len(s)) if not x % 2)
        if m == expected:
            print(p, s, m)
            r.append(p)
            # break
        p = prets.__next__()
    return r


if __name__ == '__main__':
    print(solve())
