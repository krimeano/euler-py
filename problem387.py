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
import mylib


class Harshad:
    debug = False

    def __init__(self, number):
        self.number = number
        self.digits = len(str(number))
        self.isHarshad = not self.number % self.digits
        self.isRightTruncatable = self.isHarshad and self._checkIsRightTruncatable()
        self.isStrong = self.isHarshad and mylib.isPrime(self.number / self.digits)
        if Harshad.debug:
            print(self)

    def _checkIsRightTruncatable(self):
        x = self.number // 10
        if x in Harshads.right:
            return True
        while x > 0:
            h = Harshad(x)
            if not h.isHarshad:
                return False
            x //= 10
        return True

    def __str__(self):
        return '<{number}:{isH}:{isT}:{isS}>' \
            .format(number=self.number, digits=self.digits, isH=self.isHarshad, isT=self.isRightTruncatable,
                    isS=self.isStrong)


class Harshads:
    harshads = []
    not_harshads = []
    right = []
    right_strong = []
    primes = []

    @staticmethod
    def append(n):
        if n in Harshads.harshads:
            return True
        if n in Harshads.not_harshads:
            return False
        if n > 0 and not n % 1:
            h = Harshad(n)
            if h.isHarshad:
                Harshads.harshads.append(n)
                if h.isRightTruncatable:
                    Harshads.right.append(n)
                    if h.isStrong:
                        Harshads.right_strong.append(n)
                return True
            else:
                Harshads.not_harshads.append(n)
        return False

    @staticmethod
    def seed(p):
        for i in range(0, p):
            min_x, max_x, step_x = Harshads.find_harshad_least(10 ** i), 10 ** (i + 1), i + 1
            for x in range(min_x, max_x, step_x):
                Harshads.append(x)

    @staticmethod
    def find_harshad_least(n):
        if Harshads.append(n):
            return n
        else:
            return Harshads.find_harshad_least(n + 1)

    @staticmethod
    def construct_right_harshads(p):
        Harshads.seed(2)
        if p < 3:
            return
        for i in range(2, p):
            skip_x = 10 ** (i - 1)
            min_x = 10 ** i
            for x in Harshads.right:
                if x < skip_x or x >= min_x:
                    continue
                min_y, max_y, step_y = Harshads.find_harshad_least(x * 10), (x + 1) * 10, i + 1
                if min_y > max_y:
                    continue
                for y in range(min_y, max_y, step_y):
                    Harshads.append(y)
        return

    @staticmethod
    def find_primes(p):
        Harshads.construct_right_harshads(p - 1)
        print(Harshads.right_strong)
        for s in Harshads.right_strong:
            min_x = s * 10 + 1
            max_x = min_x + 9
            for x in range(min_x, max_x, 2):
                if mylib.isPrime(x):
                    Harshads.primes.append(x)


def test():
    # 54 54 100
    # 204 354 1000
    # 579 2604 10000
    p = 4
    # Harshad.debug = True
    Harshads.find_primes(p)
    print(Harshads.right[len(Harshads.right) - 1])
    print(len(Harshads.right_strong), len(Harshads.right), len(Harshads.harshads), 10 ** p)
    r = sum(Harshads.primes)
    print(r, 90619 - r, Harshads.primes)

    return r == 90619


def solve():
    r = 0
    return r


if __name__ == '__main__':
    if test():
        print(solve())
    else:
        print('not solved yet')
