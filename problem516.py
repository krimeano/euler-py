import math, mylib, time

"""
5-smooth numbers are numbers whose largest prime factor doesn't exceed 5.
5-smooth numbers are also called Hamming numbers.
Let S(L) be the sum of the numbers n not exceeding L such that Euler's totient function φ(n) is a Hamming number.
S(100)=3728.

Find S(10^12). Give your answer modulo 2^32.
"""


class Problem516:
    def __init__(self):
        self.limit = 100
        self.numbers_smooth = []
        self.numbers_not_smooth = []
        self.primes = [2]

    def find_sum(self, limit, modulo=(2 ** 32)):
        out = 0
        self.limit = limit
        self.primes = mylib.make_primes_sieve_atkin(limit)
        print('found', len(self.primes), 'primes')
        not_hamming = self.make_sieve()
        return (int((self.limit * (self.limit + 1)) // 2) - sum(not_hamming)) % modulo

    @staticmethod
    def is_hamming_brute(n):
        t = mylib.totient(n)
        dd = mylib.find_dividers(t, distinct=True)
        # print(n, t, max(dd))
        return max(dd) < 6

    def make_sieve(self):
        not_hamming = dict()
        pp = [p ** 2 for p in self.primes if 6 < p <= int(self.limit ** 0.5)]
        for p in pp:
            for j in range(1, self.limit // p + 1):
                not_hamming[p * j] = True
                print(p, j, p * j)
        pp = [p for p in self.primes if 6 < p < self.limit // 2]

        for p in pp:
            print(p)
            for k in range(1, (self.limit - 1) // 2 // p + 1):
                d = p * 2 * k + 1
                if d in self.primes:
                    for j in range(1, self.limit // d + 1):
                        if j == d or j in not_hamming:
                            continue
                        n = d * j
                        if n in not_hamming:
                            continue
                        not_hamming[n] = True
                        print(p, n, d, j)
        return sorted([x for x in not_hamming])

    def test(self):
        # pp = self.make_primes_sieve(10 ** 2)
        # print("\033[F\033[K", pp[:10], '...', pp[-10:])
        return self.find_sum(100) == 3728

    def solve(self):
        return self.find_sum(10 ** 12)


if __name__ == '__main__':
    print("2 ** 32 =", 2 ** 32)
    the_problem = Problem516()
    if the_problem.test():
        print(the_problem.solve())
    else:
        print('THE PROBLEM IS NOT SOLVED YET')
