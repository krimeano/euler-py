class McCarthyGeneral:
    def __init__(self, m, k, s):
        assert m >= k
        assert m >= s
        self.m = m
        self.k = k
        self.s = s
        self.r = m + k - 2 * s

    def calculate(self, n):
        if n > self.m:
            return n - self.s
        return self.calculate(self.calculate(n + self.k))


# m91 = McCarthyGeneral(100, 11, 10)
# print(m91.r)
#
# for x in range(1, 110):
#     print(x, m91.calculate(x))


t = 0
for k in range(1, 10):
    for s in range(1, k):
        m = McCarthyGeneral(10, k, s)
        rr = [m.calculate(x) for x in range(10)]
        if len(set(rr)) < 2:
            t += sum(set(rr))
        print(10, k, s, rr)
print(t)