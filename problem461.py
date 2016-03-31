import math


def find_k_by_n(n):
    def f(a):
        return math.log(a + 1) * n

    return f


def func_n(n):
    max_k = math.ceil(find_k_by_n(n)(math.pi))
    ee = tuple(math.e ** (x / n) - 1 for x in range(max_k))

    def f(k):
        return ee[k]

    return f


def approximate(n=200):
    find_k = find_k_by_n(n)
    func = func_n(n)
    a = math.pi
    kk = []
    for i in range(3):
        k = math.floor(find_k(a))
        # print(a, k)
        kk.append(k)
        a -= func(k)
    k = round(find_k(a))
    kk.append(k)
    return tuple(kk)


def almost_pi_by_n(kk, n):
    func = func_n(n)
    s = 0
    for k in kk:
        s += func(k)
    return s


# given_pi_200 = almost_pi_by_n((6, 75, 89, 226,), 200)
# my_pi_200 = almost_pi_by_n(approximate(200), 200)
#
# print(math.pi)
#
# print(given_pi_200, abs(math.pi - given_pi_200))
# print(my_pi_200, abs(math.pi - my_pi_200))

n = 10 ** 4
find_k = find_k_by_n(n)
func = func_n(n)
min_d = math.floor(find_k(math.pi / 4))
max_d = math.floor(find_k(math.pi))
r = 1
rr = (0, 0, 0, 0)
ee = tuple(math.e ** (k / n) for k in range(max_d))
print(min_d, max_d, "\n")

for d in range(min_d, max_d + 1):
    f_d = func(d)
    diff_d = math.pi - f_d
    min_c = math.floor(find_k(diff_d / 3))
    max_c = min(d, math.floor(find_k(diff_d)))
    for c in range(min_c, max_c + 1):
        f_c = func(c)
        diff_c = diff_d - f_c
        min_b = math.floor(find_k(diff_c / 2))
        max_b = min(c, math.floor(find_k(diff_c)))
        for b in range(min_b, max_b + 1):
            f_b = func(b)
            diff_b = diff_c - f_b
            a = round(find_k(diff_b))
            f_a = func(a)
            f_pi = f_a + f_b + f_c + f_d
            pi_diff = abs(math.pi - f_pi)
            print("\033[F\033[K", d, c, b, a, f_pi, pi_diff)
            if pi_diff < r:
                print()
                r = pi_diff
                rr = (a, b, c, d)
print(rr, sum(x ** 2 for x in rr))
