import math

limit = 10 ** 6

a_min = 3
a_max = math.floor(limit / 4 + 1)
s = 0
for a in range(a_min, a_max + 1):
    a2 = a ** 2
    b_min = 2 - a % 2
    b_max = 0
    if a2 > limit:
        b_min = math.ceil((a2 - limit) ** 0.5)
        if b_min % 2 != a % 2:
            b_min += 1
    if a > 1:
        b_max = a - 2
    n = 1
    if b_min != b_max:
        n = (b_max - b_min) // 2 + 1
    s += n
    print(a, '|', b_min, b_max, '|', a2 - b_min ** 2, a2 - b_max ** 2, '|', n, s)
