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


def make_chain(current_chains, nnn):
    if not len(nnn):
        return current_chains
    chains = []
    for i in range(len(nnn)):
        nnn_rest = nnn[:i] + nnn[i+1:]

    return chains

def solve():
    nnn = []
    for x in range(3, 9):
        f = math.ceil(PolyNumber.find_n(x, 1000))
        t = math.ceil(PolyNumber.find_n(x, 9999))
        nn = [int(PolyNumber(x, y)) for y in range(f, t)]
        #print(x, nn)
        nnn.append(nn)
    chain = make_chain([], nnn)
    print(chain)
    return 0


if __name__ == '__main__':
    print(solve())
