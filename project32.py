def isPanDigital(a, b, c):
    s = ''.join(sorted(str(a) + str(b) + str(c)))
    return s == '123456789'


if __name__ == '__main__':
    n = 0
    p = set()
    for a in range(1, 10):
        for b in range(1, 10):
            if b == a:
                continue
            for c in range(1, 10):
                if c == b or c == a:
                    continue
                for d in range(1, 10):
                    if d == c or d == b or d == a:
                        continue
                    for e in range(1, 10):
                        if e == d or e == c or e == b or e == a:
                            continue
                        ab = 10 * a + b
                        cde = 100 * c + 10 * d + e
                        bcde = 1000 * b + cde
                        m1 = a * bcde
                        m2 = ab * cde
                        if a > 1 and m1 < 10000 and isPanDigital(a, bcde, m1):
                            print(a, bcde, m1)
                            p.add(m1)
                            n+=1
                        if m2 < 10000 and isPanDigital(a, bcde, m2):
                            print(ab, cde, m2)
                            p.add(m2)
                            n+=1
    print('ok', n, p)
    s = 0
    for m in p:
        s += m
    print(s)