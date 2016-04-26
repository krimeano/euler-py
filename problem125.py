import math

m = 10 ** 8
n_max = math.floor(((2 * m - 1) ** 0.5 + 1) / 2)
print(m, n_max, n_max ** 2, n_max ** 2 + (n_max - 1) ** 2, n_max ** 2 + (n_max + 1) ** 2)
ss = [i ** 2 for i in range(n_max + 1)]

print(ss[:5], '.' * round(math.log((len(ss) - 10), 10)), ss[-5:])

r = 0
aa = dict()
for i in range(n_max, 1, -1):
    a = ss[i]
    for j in range(i - 1, 0, -1):
        a += ss[j]
        # t = sum([x ** 2 for x in range(j, i + 1)])
        if a > m:
            break
        if str(a) == str(a)[::-1]:
            if a in aa:
                print(a, 'is already counted:', aa[a])
            else:
                r += a
                aa[a] = (j, i)
            print(i, j, a, r)

print(r)
# 2916867073
