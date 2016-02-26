import math

m = 10 ** 8
n_max = math.floor(((2 * m - 1) ** 0.5 + 1) / 2)
print(m, n_max, n_max ** 2, n_max ** 2 + (n_max - 1) ** 2, n_max ** 2 + (n_max + 1) ** 2)
s = 0
ss = [0]
for i in range(1, n_max + 2):
    s += i ** 2
    ss.append(s)
    print(i, i ** 2, s)
k = 0
r = 0
for i in range(2, len(ss)):
    for j in range(i - 2, -1, -1):
        a = ss[i] - ss[j]
        if a > m:
            break
        if str(a) == str(a)[::-1]:
            r += a
            k += 1
            # print(a, end=" ")
            print(i, '-', j, ':', ss[i], '-', ss[j], '=', a, k, r)
            # 2916867073
print("\n\n", r)
