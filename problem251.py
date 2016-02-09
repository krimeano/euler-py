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
            # if b_max > self.limit - a:
            #     continue
            # print(p, b_max)
            for b in range(1, b_max + 1):
                c = self.a_polynom(a) / 27 / b ** 2
                if not c % 1 and a + b + c <= self.limit:
                    t = [a, b, int(c)]
                    tv = self.check_triplet(t)
                    print(t, tv)
                    self.triplets.append([a, b, c])
                    # for c in range(1, self.limit - a - b):
                    #     t = [a, b, c]
                    #     tv = self.check_triplet(t)
                    #     if 1000000000 * abs(1 - tv) < 1:
                    #         self.triplets.append(t)
                    #         print('    ', a, b, c, a + b + c, tv)

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
        # print(b, c, d, p, q, z, y)
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

    def split_c(self, c, top_limit):

        ddd = mylib.gather_dividers(c)
        m = 1
        dd_sq = []
        for dd in ddd:
            if len(dd) < 2:
                continue
            for i in range(len(dd) // 2):
                dd_sq.append(dd[0])
                m *= dd[0]
        c_base = int(c / m ** 2)
        return self.multiply_variants(c_base, dd_sq, top_limit)

    def multiply_variants(self, c_base, dd_sq, top_limit):
        b = mylib.mult(dd_sq)
        # print('   ', b, c_base, dd_sq)
        out = []
        if c_base > top_limit:
            return out
        if b + c_base <= top_limit:
            out.append((b, c_base,))
        if b == 1:
            return out
        for i in range(len(dd_sq)):
            new_dd = dd_sq[:i] + dd_sq[i + 1:]

            x = dd_sq[i]
            c = c_base * x * x
            out += self.multiply_variants(c, new_dd, top_limit)
        return list(set(out))

    def find_by_k(self):
        """
        a = 3k - 1
        b = k
        c = 8 * k - 3
        :return:
        """
        self.triplets = []
        for bk in range(1, (self.limit + 1) // 4 + 1):
            ck = (8 * bk - 3)
            ak = 3 * bk - 1
            if ak + bk + ck > self.limit:
                if mylib.isPrime(ck):
                    continue

                ddd = mylib.gather_dividers(ck)

                sq_d = False
                for dd in ddd:
                    p = len(dd) // 2
                    if p:
                        sq_d = True
                        break
                if not sq_d:
                    continue

            # print(ak, bk, ck)
            c0 = ck * bk * bk
            ccc = self.split_c(c0, self.limit - ak)
            if not len(ccc):
                continue
            for cb in ccc:
                t = [ak, cb[0], cb[1]]
                self.triplets.append(t)
                print(t, len(self.triplets))

        return True


class Problem251:
    @staticmethod
    def test():
        """
[314, 315, 93] 1.0
[341, 171, 404] 1.0
[341, 342, 101] 1.0
[347, 290, 148] 1.0
[347, 580, 37] 1.0
[368, 369, 109] 0.9999999999999982
[386, 301, 189] 1.0
[395, 297, 208] 1.0
[395, 396, 117] 0.9999999999999982
[422, 423, 125] 1.0
        :return:
        """
        ct = CardanoTriplets(1000)
        ct.find_by_k()
        # ct.find_brute()
        # print(len(ct.triplets), ct.triplets)
        # ct.find()
        print(len(ct.triplets), ct.triplets)
        print(len(mylib.cache_dividers))
        return len(ct.triplets) == 149

    @staticmethod
    def solve():
        ct = CardanoTriplets(110000000)
        ct.find_by_k()
        return len(ct.triplets)


if __name__ == '__main__':
    # for i in range(1, 101):
    #     print(i, mylib.gather_dividers(mylib.find_dividers(i)))
    #
    # print(110000000, mylib.find_dividers(109999999))

    if Problem251.test():
        print('*' * 79)
        print(Problem251.solve())
    else:
        print('NOT SOLVED YET')
