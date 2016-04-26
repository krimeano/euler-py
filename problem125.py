import math

m = 10 ** 8
n_max = math.floor(((2 * m - 1) ** 0.5 + 1) / 2)
print(m, n_max, n_max ** 2, n_max ** 2 + (n_max - 1) ** 2, n_max ** 2 + (n_max + 1) ** 2)
ss = [i ** 2 for i in range(n_max + 1)]

print(ss[:5], '.' * round(math.log((len(ss) - 10), 10)), ss[-5:])

r = 0
for i in range(n_max, 1, -1):
    s = ss[i]
    for j in range(i - 1, 0, -1):
        s += ss[j]
        if s > m:
            break
        if str(s) == str(s)[::-1]:
            r += s
            print(i, j, s, r)

print(r)
# 2916867073
