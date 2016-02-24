"""
Let ABCD be a quadrilateral whose vertices are lattice points lying on the coordinate axes as follows:

A(a, 0), B(0, b), C(−c, 0), D(0, −d), where 1 ≤ a, b, c, d ≤ m and a, b, c, d, m are integers.

It can be shown that for m = 4 there are exactly 256 valid ways to construct ABCD. Of these 256 quadrilaterals,
42 of them strictly contain a square number of lattice points.

How many quadrilaterals ABCD strictly contain a square number of lattice points for m = 100?
"""
import math


class Problem504:
    def __init__(self):
        self.m = 4
        self.points_table = {}
        self.q_points_table = {}

    def construct_qq(self, m):
        self.m = m
        n = 0
        k = 0
        m1 = m + 1
        max_points = self.count_points_inside_q((m, m, m, m))
        ss = [x ** 2 for x in range(1, math.floor(max_points ** 0.5) + 1)]
        for a in range(1, m1):
            for b in range(1, m1):
                for c in range(1, m1):
                    for d in range(1, m1):
                        q = (a, b, c, d)
                        p = self.count_points_inside_q(q)
                        if p in ss:
                            k += 1
                        n += 1
                        print("\033[F\033[K", q, p, n, k)
        print(n, k, "\n")
        return n, k

    def count_points_inside_q(self, q):
        l = len(q)
        k = 'x'.join([str(q[j]) for j in range(l)])
        if k in self.q_points_table:
            # print(k, 'is in cache')
            return self.q_points_table[k]
        s = 1
        for i in range(l):
            s += self.count_points_under_line(q[i], q[(i + 1) % l])

        # store to cache:
        if q[0] == q[1] == q[2] == q[3]:
            # print('storing', k)
            self.q_points_table[k] = s
            return s

        for i in range(l):
            k = 'x'.join([str(q[(i + j) % l]) for j in range(l)])
            # print('storing', k)
            self.q_points_table[k] = s

        if not (q[0] == q[2] or q[1] == q[3]):
            q1 = (q[0], q[3], q[2], q[1])
            for i in range(l):
                k = 'x'.join([str(q1[(i + j) % l]) for j in range(l)])
                # print('storing', k)
                self.q_points_table[k] = s

        return s

    def count_points_under_line(self, a, b):
        k = str(a) + 'x' + str(b)
        if k in self.points_table:
            return self.points_table[k]
        s = 0
        for x in range(a):
            y = b - b * x / a
            s += math.ceil(y) - 1
            # print(k, x, y, s)
        self.points_table[k] = s
        return self.points_table[k]

    def test(self):
        r = self.construct_qq(4)
        return r == (256, 42)

    def solve(self):
        return self.construct_qq(100)[1]


if __name__ == '__main__':
    problem = Problem504()
    if not problem.test():
        print('NOT SOLVED YET')
        exit(1)
    print(problem.solve())
