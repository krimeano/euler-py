import math, mylib


class Triplets:
    def __init__(self, limit):
        self.limit = limit
        self.triplets = []

    def sum(self):
        return sum([sum(x) for x in self.triplets])

    def find_triplets(self):
        # self.triplets = []
        pp = mylib.make_primes_sieve_atkin(self.limit)
        bb = dict()
        r = int(self.limit ** 0.5 // 1)
        ss = [x ** 2 for x in pp if x < r]
        print(len(pp), "primes, last 10:", sorted(pp)[-10:])
        print(len(ss), "squares, last 10:", ss[-10:], "\n")
        for a in pp:
            print("\033[F\033[K", a, "filtering")
            a1 = a + 1
            for s in ss:
                if s > a1:
                    bb[a] = (a1, 1)
                    break
                if not a1 % s:
                    b = a1 // s
                    if (b - 1) in bb and bb[b - 1][0] != b:
                        bb[a] = (bb[b - 1][0], a1 // b * bb[b - 1][1])
                    else:
                        bb[a] = (b, a1 // b)
                    break
            else:
                bb[a] = (a1, 1)
                continue
        _aaa = dict()
        for a in bb:
            print("\033[F\033[K", a, 'combining')
            b = bb[a][0]
            if b not in _aaa:
                _aaa[b] = dict()
            _aaa[b][a] = round(bb[a][1] ** (1 / 2))

        aaa = dict()
        n = 0
        for b in _aaa:
            l = len(_aaa[b])
            if l > 1:
                print("\033[F\033[K", b, "use elements with len > 1:", l)
                aaa[b] = _aaa[b]
                n += l * (l - 1) // 2
                # else:
                #     print("\033[F\033[K", k, "remove elements with len = 1")
        k = len(aaa)
        print("TOTAL", k, "keys to iterate")
        print("TOTAL", n, "iterations\n")
        bb = sorted(aaa.keys())

        k1 = 0
        n1 = 0
        for b in bb:
            k1 += 1
            aa = aaa[b]
            rr = sorted(aa.keys())
            l = len(rr)
            print(k1, "/", k, ":", b, l, rr, "\n")
            for i in range(0, l):
                for j in range(i + 1, l):
                    n1 += 1
                    p = rr[i]
                    q = rr[j]
                    r = b * aa[p] * aa[q] - 1
                    if r not in pp:
                        continue
                    t = (p, r, q)
                    self.triplets.append(t)
                    print("\033[F\033[K", n1, "/", n, t, len(self.triplets))

        return self


class Problem:
    @staticmethod
    def test():
        t = Triplets(10 ** 2)
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
