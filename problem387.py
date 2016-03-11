__author__ = 'sergeyp'
"""
A Harshad or Niven number is a number that is divisible by the sum of its digits.
201 is a Harshad number because it is divisible by 3 (the sum of its digits.)
When we truncate the last digit from 201, we get 20, which is a Harshad number.
When we truncate the last digit from 20, we get 2, which is also a Harshad number.
Let's call a Harshad number that, while recursively truncating the last digit,
always results in a Harshad number a right truncatable Harshad number.

Also:
201/3=67 which is prime.
Let's call a Harshad number that, when divided by the sum of its digits, results in a prime a strong Harshad number.

Now take the number 2011 which is prime.
When we truncate the last digit from it we get 201, a strong Harshad number that is also right truncatable.
Let's call such primes strong, right truncatable Harshad primes.

You are given that the sum of the strong, right truncatable Harshad primes less than 10000 is 90619.

Find the sum of the strong, right truncatable Harshad primes less than 10^14.
"""
import math, mylib


class Harshad:
    def __init__(self, number):
        self.n = number
        self.is_harshad = not self.n % len(str(self.n))

    def __str__(self):
        return str(self.n)

    def is_right(self):
        return self.n < 10 or (self.is_harshad and Harshad(self.n // 10).is_harshad)

    def is_strong(self):
        return self.is_harshad and mylib.is_prime(self.n // len(str(self.n)))


class Problem387:
    hhh = [[], [1, 2, 3, 4, 5, 6, 7, 8, 9]]
    ss = []
    pp = dict()
    rr = []

    def make_right_harshads(self, p):
        if len(self.hhh) < p:
            self.make_right_harshads(p - 1)
        gg = self.hhh[p - 1]
        hh = []
        for g in gg:
            hh += self.gen_next_right_harshads(p, g)
        self.hhh.append(hh)
        return self

    @staticmethod
    def gen_next_right_harshads(p, g):
        out = []
        n = 10 * g
        r = n % p
        if not r:
            out.append(n)
        out += [n + x for x in range(p - r, 10, p)]
        print(p, g, out)
        return out

    def filter_strong(self):
        for i in range(1, len(self.hhh)):
            self.ss += [x for x in self.hhh[i] if (x // i) in self.pp]
        return self

    def make_primes(self):
        self.rr = []
        for x in self.ss:
            for y in (1, 3, 7, 9):
                r = 10 * x + y
                if r in self.pp:
                    # if mylib.is_prime(r):
                    self.rr.append(r)
                else:
                    print(r, 'is not prime', mylib.find_dividers(r))
        return self

    def test(self):
        p = 4
        self.pp = mylib.make_primes_sieve_atkin(10 ** p)
        self.make_right_harshads(p - 1).filter_strong().make_primes()
        for hh in self.hhh:
            print(hh)
        print(self.ss)
        print(sum(self.rr), 90619 - sum(self.rr), self.rr)
        # h = Harshad(3608528850368400786036725)
        # print(h, h.is_harshad, h.is_right())
        # print(len(pp), sum(len(hh) for hh in self.hhh))
        # print(pp)
        # print(self.hhh)
        return False

    def solve(self):
        return 0


if __name__ == '__main__':
    problem = Problem387()
    if problem.test():
        print(problem.solve())
    else:
        print('not solved yet')
