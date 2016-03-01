import mylib, math


class Problem401:
    def __init__(self):
        self.modulo = 10 ** 9

    def sigma2(self, n):
        r = math.floor(n ** 0.5)
        pp = mylib.make_primes_sieve_atkin(n)
        modulo_plus = self.modulo * 10
        nm = n % modulo_plus
        out = ((nm - 1) + int((nm * (nm + 1) * (2 * nm + 1) / 6))) % self.modulo
        for p in pp:
            k = n // p
            pm = p % self.modulo
            out = (out + (pm ** 2) * (k - 1)) % self.modulo
            print(p, '/', n, out)
        print(out)
        return out

    def test(self):
        return self.sigma2(6) == 113

    def solve(self):
        return self.sigma2(10 ** 15)


if __name__ == '__main__':
    problem = Problem401()
    if not problem.test():
        print('The problem is not solved yet')
        exit(1)
    print("\n" + "=" * 79 + "\n")
    print(problem.solve())
