class Repunits:
    def __init__(self, limit):
        self.limit = limit
        self.base_max = int(self.find_base_max() // 1)
        print(self.base_max)
        self.numbers = set()

    def find_base_max(self):
        """
        m**2 + m + 1 = L
        m**2 + m - (L-1) = 0
        a = 1, b = 1, c = -(L - 1)
        D = b**2 - 4 * a * c = 1 + 4 (L-1) = 4L - 3
        m = (-b ± d ** .5 )/2 = ((4L-3) ** 0.5 - 1) /2 = (L - 3/4) ** 0.5 - 1/2
        :return:
        """
        return (self.limit - 3 / 4) ** 0.5 - 1 / 2

    def find_numbers(self):
        self.numbers = {1}
        for b in range(2, self.base_max + 1):
            print(b, 'from', self.base_max)
            p = 2
            n = b ** p + b + 1
            while n < self.limit:
                self.numbers.add(n)
                p += 1
                n += b ** p

        return self


class Problem346:
    @staticmethod
    def test():
        r = Repunits(50)
        r.find_numbers()
        print(sorted(r.numbers))
        return sorted(r.numbers) == [1, 7, 13, 15, 21, 31, 40, 43]

    @staticmethod
    def solve():
        r = Repunits(10 ** 12)
        r.find_numbers()
        # print(sorted(r.numbers))
        return sum(r.numbers)


if __name__ == '__main__':
    if Problem346.test():
        print('*' * 79)
        print(Problem346.solve())
    else:
        print('NOT SOLVED YET')
