import math, mylib


class Triplets:
    def __init__(self, limit):
        self.limit = limit
        self.triplets = []

    def find_triplets(self):
        self.triplets = []
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

    def find_triplets_2(self):
        self.triplets = []
        squares = [x ** 2 for x in range(1, int(self.limit ** 0.5 // 1) + 1)]
        bases = dict()

        def find_base(n, dd=(), n_initial=0):
            if n in bases:
                # print('taken from cache', bases[n], dd)
                return bases[n][0], bases[n][1] + dd
            r = int(n ** 0.5 // 1) + 1
            last_d = dd[-1] if len(dd) else 0
            # print(n, r, last_d, n_initial)
            if (last_d or 2) > r:
                # bases[n_initial or n] = (n, dd)
                return n, dd
            for d in range((last_d or 2), r):
                d2 = d ** 2
                m = int(n / d2 // 1)
                if m * d2 == n:
                    if m == 1:
                        bases[n_initial or n] = (n, dd,)
                        return n, dd
                    dd = dd + (d,)
                    return find_base(m, dd, n_initial or n)
            bases[n_initial or n] = (n, dd,)
            return n, dd

        max_x = int((self.limit ** 0.5 - 1) ** 2 // 1) + 1
        # print(max_x)
        for x in range(2, max_x):
            if not mylib.isPrime(x):
                continue
            # print(x)
            b1, dd = find_base(x + 1)
            d_min = mylib.mult(dd) + 1
            d_max = int((self.limit / b1) ** 0.5 // 1)
            # print(x, b1, dd, d_min, d_max)
            # print(z, z1, b1, d_max)
            for d in range(d_min, d_max + 1):
                z = b1 * d ** 2 - 1
                if not mylib.isPrime(z):
                    continue
                y = int(((x + 1) * (z + 1)) ** 0.5) - 1
                if not mylib.isPrime(y):
                    continue
                t = (x, y, z,)
                self.triplets.append(t)
                print(t)
        # x = b1 * d ** 2 - 1
        #     if x < 2:
        #         continue
        #     if not mylib.isPrime(x):
        #         continue
        #     y = int(((x + 1) * z1) ** 0.5) - 1
        #     if not mylib.isPrime(y):
        #         continue
        #     t = (x, y, z,)
        #     self.triplets.append(t)
        #     print(t, len(self.triplets))
        return self

    def sum(self):
        return sum([sum(x) for x in self.triplets])

    def find_triplets_3(self):
        pp = mylib.make_primes_sieve(self.limit)

        ss = [x ** 2 for x in range(1, int((self.limit // 2) ** 0.5) + 1)]
        print(len(ss), ss[:10], ss[-10:])
        input('press enter to continue')
        max_x0 = self.limit // 4
        for x0 in range(2, max_x0):
            if x0 in ss:
                continue

            x_ss = [s for s in ss if (s > 1) and (s <= x0 / 2)]
            if len([s for s in x_ss if not x0 % s]):
                continue
            print(x0)
            m_max = min(math.floor((self.limit / x0) ** 0.5), len(ss))
            # print(x0, m_max)
            for m in range(m_max):
                x = x0 * ss[m] - 1
                if x not in pp:
                    continue
                # print(x0, ss[m], x + 1)
                for n in range(m + 1, m_max):
                    z = x0 * ss[n] - 1
                    if z not in pp:
                        continue
                    y = round(((x + 1) * (z + 1)) ** 0.5) - 1
                    if y not in pp:
                        continue
                    t = (x, y, z,)
                    if t in self.triplets:
                        raise ('triplet already found', t)
                    self.triplets.append(t)
                    print(x0, t)
        print()
        print('.' * 79)
        return self

    def find_triplets_4(self):
        pp = mylib.make_primes_sieve(self.limit)
        for p in pp:
            for q in [x for x in pp if x > p]:
                sq = (p + 1) * (q + 1)
                s = round(sq ** 0.5)
                if s ** 2 != sq:
                    continue
                if s-1 not in pp:
                    continue
                t = (p, s - 1, q)
                self.triplets.append(t)
                print("\033[F\033[K", t, len(self.triplets))
        return self


class Problem:
    @staticmethod
    def test():
        t = Triplets(10 ** 2)
        t.find_triplets_4()
        return t.sum() == 1035

    @staticmethod
    def solve():
        t = Triplets(10 ** 8)
        t.find_triplets_4()
        return t.sum()


if __name__ == '__main__':
    if Problem.test():
        print('*' * 79)
        print(Problem.solve())
    else:
        print('PROBLEM IS NOT SOLVED YET')
