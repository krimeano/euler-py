"""
find sum max(x ** 2 % a for x in range(0, a))

1 0 [0]
2 1 [0, 1]
3 1 [0, 1, 1]
4 1 [0, 1, 0, 1]
5 4 [0, 1, 4, 4, 1]
6 4 [0, 1, 4, 3, 4, 1]
7 4 [0, 1, 4, 2, 2, 4, 1]
8 4 [0, 1, 4, 1, 0, 1, 4, 1]
9 7 [0, 1, 4, 0, 7, 7, 0, 4, 1]
10 9 [0, 1, 4, 9, 6, 5, 6, 9, 4, 1]

2 1 [1]
3 1 [1, 1]
4 1 [1, 0, 1]
5 4 [1, 4, 4, 1]
6 4 [1, 4, 3, 4, 1]
7 4 [1, 4, 2, 2, 4, 1]
8 4 [1, 4, 1, 0, 1, 4, 1]
9 7 [1, 4, 0, 7, 7, 0, 4, 1]
10 9 [1, 4, 9, 6, 5, 6, 9, 4, 1]

(a-x)**2 % a = (a**2 - 2*a*x + x**2) % a = x**2 % a
so we can consider numbers 1..a//2

x**2 = k*a-1, k*a-2, ... k*a + a//2 = k*a - b, b in 1..a//2
if b > a//2 -> k = k+1 and b < a//2

x**2 = k*a-b, b in 1..a//2

max x = (a//2)**2
max k = ((a//2)**2 + b) // a

min x = floor(a ** 0.5)
min k = (floor(a ** 0.5) + b) // a


x**2+b = k*a
x**2+b-k+k = k*a
x**2-(k-b) = k*(a-1)
k-b = c**2
k = c**2+b
    x**2 = a*(c**2+b) - b
    c**2 = (x**2 + b) / a - b = ((a//2) ** 2 + b) / a - b
    max_c = ((a//2)**2 + b) // a - b
    min_c = (floor(a ** 0.5) + b // a) - b
    ((a//2) ** 2 + b) / a - b > 0 => b(a-1) < (a//2)**2
    max_b = (a//2)**2 // (a-1)

x**2 - c**2 = k*(a-1)
(x+c)*(x-c) = k*(a-1)
x - c = kd
x = kd + c <= (a//2)**2
d <= c * (a//2) ** 2 / (c**2 + a//2)


a-b > a**0.5
b < a - a**0.5
"""
import math

a_max = 10 ** 6

# ss = dict((x ** 2, True) for x in range(0, a_max // 2 + 1))
# print(len(ss))
s = 0
for a in range(2, a_max + 1):
    # print('=' * 79)
    # mm = [x ** 2 % a for x in range(math.floor((a - 1) ** 0.5), a // 2 + 1)]
    # print(a, max(mm), len(mm), mm)
    # print('-' * 79, "\n")
    max_k = a // 4
    r = 0
    for k in range(1, max_k + 1):
        ka = k * a
        x = math.floor(ka ** 0.5)
        r = max(r, x ** 2 % a)
        print("\033[F\033[K", end="")
        print(a, r, k, '/', max_k)
        if a - r == 1:
            break
    s += r
print("sum=", s)
