import math


class PolyNumber:
    aa = [x / 2 for x in range(-2, 9)]
    bb = [x / 2 for x in range(4, -7, -1)]

    def __init__(self, p, n):
        self.p = p
        self.n = n
        self.a = self.aa[p]
        self.b = self.bb[p]
        self.N = int(n * (self.a * n + self.b))

    def __int__(self):
        return self.N

    def __str__(self):
        return '<' + str(self.p) + "," + str(self.n) + "=" + str(self.N) + ">"

    @staticmethod
    def find_n(p, N):
        a = PolyNumber.aa[p]
        b = PolyNumber.bb[p]
        return ((b ** 2 + 4 * a * N) ** 0.5 - b) / (2 * a)


def make_chains(old_chains, nnn):
    chains = dict()
    for ii in old_chains:
        for j in range(len(nnn)):

            if j in ii:
                continue
            kk = ii + (j,)
            cc = []
            for mm in old_chains[ii]:
                m = mm[len(mm) - 1]
                for n in nnn[j]:
                    if m % 100 == n // 100 and n not in mm:
                        cc.append(mm + [n])
            if not len(cc):
                continue
            chains[kk] = cc
    return chains


def solve():
    nnn = []
    aaa = dict()  # L=1
    for x in range(3, 9):
        f = math.ceil(PolyNumber.find_n(x, 1000))
        t = math.ceil(PolyNumber.find_n(x, 9999))
        nn = [z for z in [int(PolyNumber(x, y)) for y in range(f, t)] if z % 100 and (z % 100) // 10]
        nnn.append(nn)
    aaa[(0,)] = [[n] for n in nnn[0]]

    fff = aaa
    bbb = make_chains(aaa, nnn)
    while len(bbb):
        fff = bbb
        bbb = make_chains(bbb, nnn)
    r = 0
    for ii in fff:
        for ff in fff[ii]:
            m = ff[len(ff) - 1]
            n = ff[0]
            if m % 100 != n // 100:
                continue
            print(ii, ff)
            r = sum(ff)

    return r


if __name__ == '__main__':
    print(solve())
