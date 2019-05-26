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
        self.sum = self.to_sum()
        self.is_harshad = not self.n % self.sum

    def __str__(self):
        return str(self.n)

    def is_right(self):
        return self.n > 0 and (self.n < 10 or (self.is_harshad and Harshad(self.n // 10).is_harshad))

    def is_strong(self):
        return self.is_harshad and mylib.is_prime(self.n // self.sum)

    def to_sum(self):
        return sum([int(z) for z in str(self.n)])

    def gen_next_right_harshads(self):
        n = self.n * 10
        return dict((y, True) for y in [Harshad(x) for x in range(n, n + 10)] if y.is_harshad)

    def gen_next_primes(self):
        return dict((y, True) for y in [self.n * 10 + x for x in (1, 3, 7, 9)] if mylib.is_prime(y))


class Problem387():
    hhh = [dict(), dict((Harshad(x), True) for x in range(1, 10))]
    ss = dict()
    rr = dict()

    @staticmethod
    def init_primes(p):
        mylib.known_primes = mylib.primes_from_file(10 ** math.ceil(p / 2))
        print('primes:', '... ' + ', '.join([str(x) for x in (sorted(mylib.known_primes)[-10:])]))

    def make_right_harshads(self, p):
        print('make right harshads', p)
        if len(self.hhh) < p:
            self.make_right_harshads(p - 1)
        hh = dict()
        for g in self.hhh[p - 1]:
            hh.update(g.gen_next_right_harshads())
        self.hhh.append(hh)
        return self

    def filter_strong(self):
        print('filter strong')
        self.ss = dict()
        for i in range(1, len(self.hhh)):
            print('\t', i, len(self.hhh[i]))
            self.ss.update(dict((x, True) for x in self.hhh[i] if x.is_strong()))
        return self

    def make_primes(self):
        print('make primes')
        self.rr = dict()
        for s in self.ss:
            print('make primes for', s.n)
            self.rr.update(s.gen_next_primes())
        return self

    def test(self):
        p = 4
        self.init_primes(p)
        self.make_right_harshads(p - 1).filter_strong().make_primes()
        for hh in self.hhh:
            print([h.n for h in hh])
        print(sorted(s.n for s in self.ss))
        print(sum(self.rr), 90619 - sum(self.rr), sorted(self.rr))
        return 90619 == sum(self.rr)

    def solve(self):
        p = 14
        self.init_primes(p)
        self.make_right_harshads(p - 1).filter_strong().make_primes()
        return sum(self.rr)


if __name__ == '__main__':
    problem = Problem387()
    if problem.test():
        print(problem.solve())
    else:
        print('not solved yet')
