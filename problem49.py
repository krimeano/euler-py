__author__ = 'sergeyp'

import mylib


def extract_progression(m):
    out = []
    for i in range(len(m) - 2):
        for j in range(i + 1, len(m) - 1):
            a = 2 * m[j] - m[i]
            if a in m:
                # print(m[i], m[j], '(', a, ')', a in m)
                out = [m[i], m[j], a]
                break
        if len(out):
            break
    return out


def solve():
    for a in range(0, 10):
        for b in range(a, 10):
            for c in range(b, 10):
                for d in range(c, 10):
                    if mylib.dividable(a + b + c + d, 3):
                        continue
                    s = [a, b, c, d]
                    m = [y for y in [int(x) for x in mylib.mutate(s)] if int(y) > 1000 and mylib.isPrime(y)]
                    if len(m) < 3:
                        continue
                    pr = extract_progression(m)
                    if len(pr):
                        print(''.join([str(x) for x in pr]))
    return True


if __name__ == '__main__':
    print(solve())
