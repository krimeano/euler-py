import math


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
    def find_max_x(d_max=1):
        max_x = 0
        for d in range(1, d_max):
            dio = Diophantine(d)
            s = dio.find_minimal_x_solution()
            print(d, s)
            max_x = max(max_x, s[0])
        return max_x

    def test(self):
        return self.find_max_x(7) == 9

    def solve(self):
        return self.find_max_x(1000)


if __name__ == '__main__':
    problem = Problem66()
    if problem.test():
        print("\n", problem.solve())
    else:
        print("the  problem is not solved yet")
        exit(1)
