"""
The positive integers, x, y, and z, are consecutive terms of an arithmetic progression.
Given that n is a positive integer, the equation, x^2 − y^2 − z^2 = n, has exactly one solution when n = 20:

13^2 − 10^2 − 7^2 = 20

In fact there are twenty-five values of n below one hundred for which the equation has a unique solution.

How many values of n less than fifty million have exactly one solution?
"""

import mylib, math

m = 50 * 10 ** 6
pp = mylib.primes_from_file(m * 2)
r = 0
for x in range(3, m):
    if x in pp:
        if x % 4 == 3:
            b = int((x + 1) / 4)
            pr = (x + b, x, x - b)
            r += 1
            print(x, '+', 'prime, 4k-1:', pr, r)
            continue
        else:
            # print(x, '-', 'prime, 4k+1: impossible')
            continue
    if x % 4 == 1:
        # print(x, '-', '(2k+1)(2(k+2p) + 1): impossible')
        continue
    if x % 4 == 2:
        # print(x, '-', '2(2k+1): impossible')
        continue
    if x % 4 == 3:
        # print(x, '-', '(2k+1)(2(k+2p+1)+1): at least 2 ways')
        continue
    if x % 16 and not x % 8:
        # print(x, '-', '8(2k+1): impossible')
        continue
    dd = mylib.find_composite_dividers(x)
    min_a = (x / 3) ** 0.5
    rr = []
    for i in range(len(dd)):
        a = dd[i]
        if a <= min_a:
            continue
        z = dd[-1 - i]
        s = a + z
        if s % 4:
            continue
        b = int(s / 4)
        pr = (x + b, x, x - b)
        rr.append(pr)
        if len(rr) > 1:
            break
    if len(rr) == 1:
        r += 1
        print(x, '+', rr[0], r)
    # else:
    #     print(x, '-', rr)
print('\n', '-' * 60, '\n', r)
# r = 0
# for x in range(4, m):
#     if x in pp:
#         continue
#     dd = mylib.find_composite_dividers(x)
#     min_a = (x / 3) ** 0.5
#     rr = []
#     # print(x, dd, min_a)
#     for a in dd:
#
#         if a < min_a:
#             continue
#         s = x / a + a
#         if s % 4:
#             continue
#         b = int(s / 4)
#         if b >= a:
#             continue
#         pr = (a + b, a, a - b)
#         rr.append(pr)
#         # print(x, a, b, pr, pr[0] ** 2 - pr[1] ** 2 - pr[2] ** 2)
#     if len(rr) == 10:
#         r += 1
#         print(x, len(rr), rr, r)
# print(r)
