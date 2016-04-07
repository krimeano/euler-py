import math, fractions

ss = dict((x ** 2, True) for x in range(math.ceil(1000 ** 0.5)))
print(ss)


class Diophantine:
    def __init__(self, d):
        self.d = d

    def find_minimal_x_solution(self):
        print("LOOKING FOR D = ", self.d, "\n")
        if self.is_square(self.d):
            print(self.d, "is square :(")
            return 0, 0
        y = 1
        while True:
            x2 = self.d * y * y + 1
            print("\033[F\033[K", "x ** 2 =", self.d, '*', y, '** 2 + 1 = ', x2)
            if self.is_square(x2):
                return int(x2 ** 0.5), y
            y += 1

    @staticmethod
    def is_square(n):
        return (n ** 0.5 // 1) ** 2 == n


class Problem66:
    @staticmethod
    def check(d, x, y):
        return not (x * x - d * y * y - 1)

    @staticmethod
    def find_max_x(d_max=1):
        max_x = 0
        r = 0
        for d in range(1, d_max):
            if d in ss:
                continue
            q = fractions.SquareRootFraction(d)
            k = 1
            a = q.get_approximation(1)
            print(d, '[', k, ']', a.n, '** 2 -', d, '*', a.d, '** 2 =', a.n ** 2 - d * a.d ** 2)
            while not Problem66.check(d, a.n, a.d):
                k += 2
                a = q.get_approximation(k)
                print('    [', k, ']', a.n, '** 2 -', d, '*', a.d, '** 2 =', a.n ** 2 - d * a.d ** 2)
            if a.n > max_x:
                max_x = a.n
                r = d
        return r

    def test(self):
        return self.find_max_x(8) == 5

    def solve(self):
        return self.find_max_x(1001)


if __name__ == '__main__':
    problem = Problem66()
    if problem.test():
        print("\n", problem.solve())
    else:
        print("the  problem is not solved yet")
        exit(1)
