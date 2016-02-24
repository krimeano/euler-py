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

    def find_sum(self, limit, modulo=(2 ** 32)):
        out = 0
        return out
        self.limit = limit
        not_hamming = self.make_sieve()

        return (int((self.limit * (self.limit + 1)) // 2) - sum(not_hamming)) % modulo

    @staticmethod
    def is_hamming_brute(n):
        t = mylib.totient(n)
        dd = mylib.find_dividers(t, distinct=True)
        # print(n, t, max(dd))
        return max(dd) < 6

    def is_smooth(self, n, n_original=0):
        if n < 6:
            if n_original:
                self.numbers_smooth.append(n_original)
            return True
        if n in self.numbers_smooth:
            if n_original:
                self.numbers_smooth.append(n_original)
            return True
        if n in self.numbers_not_smooth:
            if n_original:
                self.numbers_not_smooth.append(n_original)
            return False

        pp = mylib.findPrimesToLimit(n)
        for p in pp:
            if n % p:
                continue
            if p > 6:
                return False
            return self.is_smooth(n // p, n_original or n)
        self.numbers_not_smooth.append(n_original or n)
        return False

    def is_hamming(self, n, previous_d=1):
        if n < 6:
            return True
        if n == previous_d:
            # print(n * previous_d, 'is square')
            return False
        if n < 23:
            return True
        pp = mylib.findPrimesToLimit(n)
        # print(n, pp)
        for p in pp:
            if n % p:
                continue
            if p == previous_d and p > 6:
                # print(n, 'is divided by not smooth square')
                return False
            # print(n, p, n // p)
            if p > 22:
                if not self.is_smooth(p // 2):
                    # print(p, 'is not smooth divider, therefore', n, 'is not hamming')
                    return False
            return self.is_hamming(n // p, p)
        s = self.is_smooth(n // 2)
        # print(n, 'is prime,', int(n // 2), s)
        return s

    def make_sieve(self):
        not_hamming = dict()
        pp = [p ** 2 for p in mylib.findPrimesToLimit(self.limit, False) if p > 6]
        for p in pp:
            for j in range(1, self.limit // p + 1):
                not_hamming[p * j] = True
                # print(p, j, p * j)
        pp = [p for p in mylib.findPrimesToLimit(self.limit // 2, True) if p > 6]

        for p in pp:
            print(p)
            for k in range(1, (self.limit - 1) // 2 // p + 1):
                d = p * 2 * k + 1
                if mylib.isPrime(d):
                    for j in range(1, self.limit // d + 1):
                        if j == d or j in not_hamming:
                            continue
                        n = d * j
                        if n in not_hamming:
                            continue
                        not_hamming[n] = True
                        print(p, n, d, j)
        return sorted([x for x in not_hamming])

    def make_primes_sieve(self, limit):
        r = math.floor(limit ** 0.5)
        known_primes = self.make_primes_sieve_old(r)
        p_max = max(known_primes)
        print(limit, r, known_primes[-10:], "\n")
        modulo = 1
        p_min = 1
        pp = set()
        for x in known_primes:
            if modulo * x > r:
                break
            modulo *= x
            p_min = x
            pp.add(x)
        for p in [1] + [x for x in known_primes if (x > p_min) and (x < modulo)]:
            print("\033[F\033[K", p, modulo)
            pp |= set(range(p, limit, modulo))
        # print(sorted(pp))
        if 1 in pp:
            pp.remove(1)
        for p in [x for x in known_primes if x > p_min]:
            print("\033[F\033[K", p, '/', p_max, end=' ')
            ss = set(range(p ** 2, limit + 1, p))
            print('-', len(ss), 'items')
            pp -= ss

            # pp -= set(range(p, r + 1, p))
            # for q in [x for x in known_primes if x >= p]:
            #     # print(p, q)
            #     x = p * q
            #     if x in pp:
            #         pp.remove(x)
        # print(sorted(pp))
        return sorted(pp)

    def make_primes_sieve_old(self, L):
        r = int(L ** 0.5 // 1)
        pp = set(range(5, L + 1, 6)) | set(range(7, L + 1, 6))
        dd = set(range(5, r + 1, 6)) | set(range(7, r + 1, 6))
        pp.add(2)
        pp.add(3)
        print("\033[F\033[K", 1, ', len = ', len(dd))
        while len(dd):
            d = min(dd)
            pp -= set(range(d * 2, L + 1, d))
            dd -= set(range(d, r + 1, d))
            print("\033[F\033[K", d, ', len =', len(dd))
        return sorted(pp)

    def test(self):
        pp = self.make_primes_sieve(10 ** 8)
        print("\033[F\033[K", pp[:10], '...', pp[-10:])
        return self.find_sum(100) == 37281

    def solve(self):
        return self.find_sum(10 ** 4)


if __name__ == '__main__':
    print("2 ** 32 =", 2 ** 32)
    the_problem = Problem516()
    if the_problem.test():
        print(the_problem.solve())
    else:
        print('THE PROBLEM IS NOT SOLVED YET')
