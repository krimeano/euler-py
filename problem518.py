import math, mylib


class Triplets():
    def __init__(self, limit):
        self.limit = limit
        self.triplets = []

    def find_triplets(self):
        for y in range(2, self.limit - 1):
            if not mylib.isPrime(y):
                continue
            sub_limit = self.limit / (y + 1)
            dd = [d for d in mylib.find_rational_dividers(y + 1) if (d > 1) and (d < sub_limit)]
            if not len(dd):
                continue
            # print(y, dd)
            for d in dd:
                x, z = round((y + 1) / d) - 1, round((y + 1) * d) - 1
                # print(x, y, z)
                if not (mylib.isPrime(x) and mylib.isPrime(z)):
                    continue
                t = (x, y, z)
                self.triplets.append(t)
                print(t, len(self.triplets))
        return self

    def sum(self):
        return sum([sum(x) for x in self.triplets])


class Problem:
    @staticmethod
    def test():
        t = Triplets(100)
        t.find_triplets()
        return t.sum() == 1035

    @staticmethod
    def solve():
        t = Triplets(10 ** 8)
        t.find_triplets()
        return t.sum()


if __name__ == '__main__':
    if Problem.test():
        print('*' * 79)
        print(Problem.solve())
    else:
        print('PROBLEM IS NOT SOLVED YET')
