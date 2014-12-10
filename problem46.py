"""
It was proposed by Christian Goldbach that every odd composite number
can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
__author__ = 'sergeyp'

import math
import mylib

def process_number(n):
    rn = math.floor(n ** 0.5)
    for i in range(1, rn+1):
        k = n -  2 * i ** 2
        #print(n, rn, i, k)
        if mylib.isPrime(k):
            print(n, '=', k, '+ 2 *', i, '^ 2')
            break
    else:
        print(n, ': NOT FOUND')
        return False
    return True

def solve():
    n = 9
    r = True
    while r:
        if not mylib.isPrime(n):
            r = process_number(n)
        n += 2
    return True

if __name__ == '__main__':
    solve()
