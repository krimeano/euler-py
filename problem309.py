import math
import time


def solve(max_len, verbose=False):
    print('\nsolving for', max_len)

    max_m = math.floor(((2 * max_len - 1) ** .5 - 1) / 2)

    if verbose:
        print('max m =', max_m)

    total = 0
    total_f = 0

    triangles = {}

    print('looking for triangles')

    for m in range(1, max_m + 1):
        max_n = math.floor(((max_len - m ** 2) ** 0.5 + 1 - m) / 2)
        if verbose:
            print('for m =', m, 'max n =', max_n)
        total += m * max_n
        d = m ** 2 + (m - 1) ** 2
        for n in range(1, max_n + 1):
            a = (2 * n - 1) * (2 * m + 2 * n - 1)
            b = 2 * m * (m + 2 * n - 1)
            c = 4 * n ** 2 + 4 * n * (m - 1) + d
            if verbose:
                print(m, 'x', n, ' -> ', a, b, c)
            f = 1

            while f * c < max_len:
                total_f += 1
                aa = a * f
                bb = b * f
                cc = c * f

                if verbose:
                    print(m, 'x', n, 'x', f, '->', aa, bb, bb, '(', total_f, ')')

                if aa not in triangles:
                    triangles[aa] = set()
                triangles[aa].add((aa, bb, cc))

                if bb not in triangles:
                    triangles[bb] = set()
                triangles[bb].add((bb, aa, cc))

                f += 1

    print('total variants = ', total, '/', total_f)

    result = []

    print('matching triangles')

    for w in sorted(triangles):
        tt = sorted(triangles[w])
        if len(tt) < 2:
            continue
        if verbose:
            print()
            print(w, tt)
        for ix in range(len(tt) - 1):
            for jy in range(ix + 1, len(tt)):
                t1 = tt[ix]
                t2 = tt[jy]
                a = t1[1]
                b = t2[1]
                h = a * b / (a + b)
                if int(h) == h:
                    result.append((t1[2], t2[2], int(h)))
                    if verbose:
                        print('FOUND!', t1, 'x', t2, '->', h)

    if verbose:
        for r in result:
            print(r)

    return len(result)


if __name__ == '__main__':
    st = time.time()
    if solve(200, True) == 5:
        print(solve(10 ** 6))
    elapsed_time = time.time() - st
    print('Execution time:', elapsed_time, 'seconds')
