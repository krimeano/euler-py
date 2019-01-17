import mylib, math

pp = sorted(mylib.primes_from_file(10 ** 6 + 1))

ends = dict((x, [x * y % 10 for y in range(10)]) for x in [1, 3, 7, 9])
# print(ends)

ends_map = dict()
for p in ends:
    ends_map[p] = [0 for x in range(10)]
    for i in range(len(ends[p])):
        ends_map[p][ends[p][i]] = i
print(ends_map)


def divide(x, y):
    x_str = str(x)
    z = x * 1
    pwr = len(x_str)

    d = 0
    e = y % 10
    print('*' + str(x), '/', y, end=' ')
    for c in range(pwr):
        n = z % 10
        m = ends_map[e][n]
        d += m * 10 ** c
        z = (z - m * y) // 10
        print(' > ', n, m, m * y, end=' ')
    print(' : ', d * y, '/', y, '=', d)
    return d * y


xx = [35]
for i in range(3, len(pp) - 1):
    xx.append(divide(pp[i], pp[i + 1]))
print(xx[0:10], xx[-10:])
print(sum(xx))
