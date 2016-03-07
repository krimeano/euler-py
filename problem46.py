__author__ = 'sergeyp'

import math
import mylib

def process_number(n):
    rn = math.floor(n ** 0.5)
    for i in range(1, rn+1):
        k = n -  2 * i ** 2
        #print(n, rn, i, k)
        if mylib.is_prime(k):
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
        if not mylib.is_prime(n):
            r = process_number(n)
        n += 2
    return True

if __name__ == '__main__':
    solve()
