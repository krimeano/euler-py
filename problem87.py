import math, mylib


class PowerTriples:
    def __init__(self, limit):
        self.limit = limit
        self.triples = set()

    def find_triples(self):
        """
        a = b ** 2 + c ** 3 + d ** 4
        b,c,d - primes
        min a = 4 + 8 + 16
        a <= self.limit
        :return:
        """
        self.triples = set()
        d_primes = mylib.findPrimesToLimit((self.limit - 12) ** (1 / 4), True)
        # print(self.limit, d_primes)
        for d in d_primes:
            d4 = d ** 4
            c_primes = mylib.findPrimesToLimit((self.limit - d4 - 4) ** (1 / 3), True)
            # print(d, d4, c_primes)
            for c in c_primes:
                c3 = c ** 3
                b_primes = mylib.findPrimesToLimit((self.limit - d4 - c3) ** (1 / 2), True)
                # print(d, d4, c, c3, b_primes)
                for b in b_primes:
                    b2 = b ** 2
                    a = b2 + c3 + d4
                    print(a, b, c, d)
                    if a > self.limit:
                        raise AssertionError('WRONG FORMULA!!')
                    self.triples.add(a)
        return self


class Problem87:
    @staticmethod
    def test():
        pt = PowerTriples(5 * 10)
        pt.find_triples()
        return len(pt.triples) == 4

    @staticmethod
    def solve():
        pt = PowerTriples(5 * 10 ** 7)
        pt.find_triples()
        return len(pt.triples)


if __name__ == '__main__':
    if Problem87.test():
        print('*' * 79)
        print(Problem87.solve())
    else:
        print('NOT SOLVED YET')
