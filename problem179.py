import mylib


# 1 - [1] - No
# 2 - [1, 2] - Yes
# 3 - [1, 3] - No
# 4 - [1, 2, 4] - No
# 5 - [1, 5] - No
# 6 - [1, 2, 3, 6] - No
# 7 - [1, 7] - No
# 8 - [1, 2, 4, 8] - No
# 9 - [1, 3, 9] - No
# 10 - [1, 2, 5, 10] - No
# 11 - [1, 11] - No
# 12 - [1, 2, 3, 4, 6, 12] - No
# 13 - [1, 13] - No
# 14 - [1, 2, 7, 14] - Yes
# 15 - [1, 3, 5, 15] -

def get_number_of_composite_dividers(a):
    if a == 1:
        return 1
    n = 1
    for dd in mylib.gather_dividers(a):
        n *= len(dd) + 1
    return n


k = 1
for x in range(15, 10 ** 7, 2):
    if mylib.isPrime(x):
        continue
    c = get_number_of_composite_dividers(x - 1)
    d = get_number_of_composite_dividers(x)
    e = get_number_of_composite_dividers(x + 1)
    # print(x, c, d, e)
    if c == d:
        print(x - 1, x, d)
        k += 1
    if d == e:
        print(x, x + 1, d)
        k += 1
print(k)