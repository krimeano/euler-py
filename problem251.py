import math, mylib


class CardanoTriplets():
    def __init__(self, limit):
        self.triplets = []
        self.limit = limit
        return

    def find_brute(self):
        self.triplets = []
        for a in range(1, int(self.limit / 2) + 1):
            p = self.a_polynom(a)
            if p % 27:
                continue
            b_max = min(int((p / 27) ** 0.5 // 1), self.limit - a)
            for b in range(1, b_max + 1):
                c = self.a_polynom(a) / 27 / b ** 2
                if not c % 1 and a + b + c <= self.limit:
                    t = [a, b, int(c)]
                    tv = self.check_triplet(t)
                    print(t, tv)
                    self.triplets.append(t)
        return self

    @staticmethod
    def solve_cubic_1_3b_c_d(b, c, d):
        p = 3 * b ** 2 - c
        q = b * c - 2 * b ** 3 - d
        z = q / 2
        y = (z ** 2 - (p / 3) ** 3) ** 0.5
        m = z - y
        s = 1
        if m < 0:
            m = -m
            s = -1
        t = (z + y) ** (1 / 3) + s * m ** (1 / 3) - b
        return t

    @staticmethod
    def a_polynom(a):
        return 8 * a ** 3 + 15 * a ** 2 + 6 * a - 1

    @staticmethod
    def check_triplet(t):
        m = (t[0] - t[1] * t[2] ** 0.5)
        s = 1
        if m < 0:
            m = -m
            s = -1

        return (t[0] + t[1] * t[2] ** 0.5) ** (1 / 3) + s * m ** (1 / 3)

    @staticmethod
    def get_square_dividers(c):
        ddd = mylib.gather_dividers(c)
        out = []
        for dd in ddd:
            if len(dd) < 2:
                continue
            for i in range(len(dd) // 2):
                out.append(dd[0])
        return out

    def find_by_k(self):
        """
        a = 3k - 1
        b = k
        c = 8 * k - 3
        :return:
        """
        self.triplets = []
        for bk in range(1, self.get_max_q()):
            ck = (8 * bk - 3)
            ak = 3 * bk - 1
            sq_d = self.get_square_dividers(ck)
            if ak + bk + ck > self.limit:
                if mylib.is_prime(ck) and not len(sq_d):
                    continue
            m0 = mylib.mult(sq_d)
            b0 = bk * m0
            c0 = int(ck / m0 / m0)
            if c0 > self.limit - ak - 1:
                continue
            b_limit = self.limit - ak - c0
            bm_bm = [(x, int(b0 / x) ** 2) for x in mylib.find_composite_dividers(b0, b_limit)]
            for bm in bm_bm:
                b = bm[0]
                c = c0 * bm[1]
                if ak + b + c > self.limit:
                    continue
                t = [ak, b, c]
                self.triplets.append(t)
                print(t, len(self.triplets))
            continue
        return self

    def get_max_q(self):
        a = self.solve_cubic_1_3b_c_d(1 / 12, 3 / 2, -(4 * self.limit ** 3 + 1) / 12)
        print(a)
        return math.floor((a + 1) / 3)


class Problem251:
    @staticmethod
    def test():
        ct = CardanoTriplets(1000)
        ct.find_by_k()
        return len(ct.triplets) == 149

    @staticmethod
    def solve():
        ct = CardanoTriplets(110000000)
        ct.find_by_k()
        return len(ct.triplets)


if __name__ == '__main__':
    if Problem251.test():
        print('*' * 79)
        print(Problem251.solve())
    else:
        print('NOT SOLVED YET')
