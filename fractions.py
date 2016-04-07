import mylib


class Fraction:
    def __init__(self, numerator=1, denominator=1):
        self.n = int(numerator)
        self.d = int(denominator)
        self.fix_sign()  # simplify()

    def fix_sign(self):
        if self.d < 0:
            self.n = -self.n
            self.d = -self.d
        return self

    def simplify(self):
        if not self.d:
            return self.d

        if self.d == self.n:
            self.d = 1
            self.n = 1
            return

        def get_common_dividers():
            return list(set(mylib.find_dividers(abs(self.n))).intersection(
                set(mylib.find_dividers(self.d))))

        cd = get_common_dividers()
        while len(cd):
            for x in cd:
                self.n = int(self.n / x)
                self.d = int(self.d / x)
            cd = get_common_dividers()
        return self

    def revert(self):
        return Fraction() / self

    def __int__(self):
        return int(self.n / self.d)

    def __float__(self):
        return self.n / self.d

    def __str__(self):
        if not self.d:
            if self.n != 0:
                return 'infinity'

        if not self.n:
            return '0'

        if self.d == 1:
            return str(self.n)

        return '/'.join([str(self.n), str(self.d)])

    def __add__(self, other):
        return Fraction(self.n * other.d + self.d * other.n, self.d * other.d)

    # def __iadd__(self, other):
    #     return self + other

    def __sub__(self, other):
        return Fraction(self.n * other.d - self.d * other.n, self.d * other.d)

    def __mul__(self, other):
        return Fraction(self.n * other.n, self.d * other.d)

    def __truediv__(self, other):
        return Fraction(self.n * other.d, self.d * other.n)

    def __floordiv__(self, other):
        return Fraction(self.n * other.d // (self.d * other.n))

    def __mod__(self, other):
        d = self.d * other.n
        return Fraction(self.n * other.d % d, d)

    def __divmod__(self, other):
        return self // other, self % other


class ContinuedFractionRepresentation:
    def __init__(self, base, period=()):
        self.base = base
        self.period = period

    def get_element(self, n):
        if not n:
            return self.base
        k = (n - 1) // len(self.period) + 1
        i = (n - 1) % len(self.period)
        x = self.period[i]

        return sum(x[j] * k ** j for j in range(len(x)))

    def get_representation(self, n=1):
        # terms = (self.get_element(x) for x in range(2, 1))
        return self.base, tuple(self.get_element(x) for x in range(1, n)) if len(self.period) else ()

    def get_representation_plain(self, n=1):
        r = self.get_representation(n)
        return [r[0]] + [x for x in r[1]]


class ContinuedFraction:
    def __init__(self, base, period=()):
        self.representation = ContinuedFractionRepresentation(base, period)

    def get_convergent(self, i):
        r = self.representation.get_representation_plain(i + 1)
        return self.bootstrap(r, None)

    def bootstrap(self, r, a):
        if not len(r):
            return a or Fraction(0)
        b = Fraction(r[-1])
        # print(r[:-1], b, a)
        if a:
            b += Fraction() / a
        return self.bootstrap(r[:-1], b)


class SquareRootFraction:
    def __init__(self, n):
        self.n = n
        self.r = self.calculate_representation()

    def calculate_representation(self):
        base = int(self.n ** (1 / 2) // 1)
        period = []
        if base ** 2 == self.n:
            return base, period
        steps_history = []
        step = (base, 1, -base)
        while step not in steps_history:
            steps_history.append(step)
            if len(steps_history) > 1:
                period.append(step[0])
            step = self.next_period_step(*step)
            # print(step)

        return base, period

    def next_period_step(self, c, a, b):
        """
        a / (sqrt(n) + b)
        :param a:
        :param b:
        :return:
        """
        a_new = (self.n - b ** 2) / a
        # gcd = mylib.find_gcd(a, new_d)
        b_new = -b
        c_new = 0
        n = 0
        m = (2 * self.n ** (1 / 2)) // 1 + 1
        while n < m and (self.n - (b_new - a_new) ** 2) / a_new > 0:
            n += 1
            if n >= m:
                raise RuntimeError('WTF ' + str(self.n) + ' ' + str(m))
            b_new -= a_new
            c_new += 1
            # print(a_new, b_new, c_new, (self.n - b_new ** 2) / a_new)
        return c_new, a_new, b_new

    def get_approximation(self, n=0):
        a0 = self.r[0]
        if not n:
            return a0
        p = len(self.r[1])
        qq = [a0] + [self.r[1][x % p] for x in range(n)]
        # print(a0,self.r[1], qq, qq[::-1])
        a = None
        for x in qq[::-1]:
            if not a:
                a = Fraction(x, 1)
            else:
                a = Fraction(x * a.n + a.d, a.n)
        return a