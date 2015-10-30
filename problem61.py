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


def solve():
    bbb = dict()
    eee = dict()
    for x in range(3, 9):
        f = math.ceil(PolyNumber.find_n(x, 1000))
        t = math.ceil(PolyNumber.find_n(x, 9999))
        nn = [int(PolyNumber(x, y)) for y in range(f, t)]
        print(x, f, t, nn)
        bbb[x] = dict()
        eee[x] = dict()
        for y in nn:
            b = str(y)[:2]
            e = str(y)[2:]
            if b not in bbb[x]:
                bbb[x][b] = []
            if e not in eee[x]:
                eee[x][e] = []
            bbb[x][b].append(y)
            eee[x][e].append(y)
        print(bbb[x])
        print(eee[x])
    for a in eee[3]:
        if a in bbb[4]:
            print(a, eee[3][a], bbb[4][a])
    return 0


if __name__ == '__main__':
    print(solve())
