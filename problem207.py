"""
 P(5) = 1/1
   P(10) = 1/2
   P(15) = 2/3
   P(20) = 1/2
   P(25) = 1/2
   P(30) = 2/5
   ...
   P(180) = 1/4
   P(185) = 3/13
"""

import math


def log2(a):
    return math.log(a, 2)


def solve_t(k):
    s = ((4 * k + 1) ** .5 + 1) / 2
    return log2(s)


for x in range(1, 10):
    print(x, 4 ** x - 2 ** x)
