"""
Problem 357
Consider the divisors of 30: 1,2,3,5,6,10,15,30.
It can be seen that for every divisor d of 30, d+30/d is prime.

Find the sum of all positive integers n not exceeding 100 000 000
such that for every divisor d of n, d+n/d is prime.
"""
import math, mylib


class Problem357:
    @staticmethod
    def solve():
        m = 100000000
        data = [2]
        for a in range(6, m, 4):
            if not mylib.is_prime(a + 1) or not mylib.is_prime(a / 2 + 2):
                continue
            dd = mylib.find_composite_dividers(a)
            if len(dd) % 2:
                continue
            # print(a, dd)
            all_primes = True
            for i in range(2, len(dd) // 2):
                b = dd[i] + dd[len(dd) - i - 1]
                all_primes = all_primes and mylib.is_prime(b)
                # print('   ', dd[i], dd[len(dd) - i - 1], b, all_primes)
                if not all_primes:
                    break
            if all_primes:
                print(a, dd)
                data.append(a)
        # print(data)
        return sum(data)


if __name__ == '__main__':
    print(Problem357.solve())
