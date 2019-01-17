"""
- - 0000000
0 - 1110111
1 - 0000011
2 - 0111110
3 - 0011111
4 - 1001011
5 - 1011101
6 - 1111101
7 - 1010011
8 - 1111111
9 - 1011111
"""
import math, random


class DisplayNumber:
    def __init__(self, value=-1, segments=(0, 0, 0, 0, 0, 0, 0)):
        self.value = value
        self.segments = segments
        self.binary = ''.join(str(x) for x in segments)
        self.decimal = int(self.binary, 2)

    def draw(self):
        def hor(i):
            if self.segments[i]:
                return '|'
            return ' '

        def ver(i, j):
            if self.segments[i]:
                if self.segments[j]:
                    return ':'
                return '_'
            if self.segments[j]:
                return '^'
            return ' '

        return hor(2) + ver(0, 5) + hor(3) + ver(1, 6) + hor(4)


nan = DisplayNumber()
numbers = (
    DisplayNumber(0, (1, 1, 1, 0, 1, 1, 1)),
    DisplayNumber(1, (0, 0, 0, 0, 0, 1, 1)),
    DisplayNumber(2, (0, 1, 1, 1, 1, 1, 0)),
    DisplayNumber(3, (0, 0, 1, 1, 1, 1, 1)),
    DisplayNumber(4, (1, 0, 0, 1, 0, 1, 1)),
    DisplayNumber(5, (1, 0, 1, 1, 1, 0, 1)),
    DisplayNumber(6, (1, 1, 1, 1, 1, 0, 1)),
    DisplayNumber(7, (1, 0, 1, 0, 0, 1, 1)),
    DisplayNumber(8, (1, 1, 1, 1, 1, 1, 1)),
    DisplayNumber(9, (1, 0, 1, 1, 1, 1, 1))
)


# print(nan.value, nan.binary, nan.decimal, nan.draw())
# for n in numbers:
#     print(n.value, n.binary, n.decimal, n.draw())


class Transition:
    a = nan
    b = nan

    def __init__(self, a, b):
        if a >= 0:
            self.a = numbers[a]
        if b >= 0:
            self.b = numbers[b]
        self.axb = self.a.decimal & self.b.decimal
        self.a_m = self.a.decimal & ~self.axb
        self.m_b = self.b.decimal & ~self.axb
        sum_a = sum(self.a.segments)
        sum_b = sum(self.b.segments)
        sum_am = sum(int(x) for x in format(self.a_m, '07b'))
        sum_mb = sum(int(x) for x in format(self.m_b, '07b'))
        sum_ab = sum_a + sum_b
        sum_amb = sum_am + sum_mb
        self.economy = sum_ab - sum_amb


def digit_root(a):
    return sum(int(x) for x in str(a))


t_ee = {}
end = '   '
for x in range(-1, 10):
    for y in range(-1, 10):
        p = (x, y)
        t = Transition(x, y)
        t_ee[p] = t.economy
        # print(p, '>', format(t.economy, '2d'), end=end)
    end = '    '
    # print()

# for i in range(10):
#     x = random.randint(10 ** 7, 2 * 10 ** 7)
#     print(x, digit_root(x // 100) * 100 + x % 100, end=': ')
#     n = x
#     r = digit_root(n)
#     while n > r:
#         print(n, end=' > ')
#         n = r
#         r = digit_root(n)
#     print(n)

d_ee = [0 for x in range(10)]
print(d_ee)
for x in range(10, 65):
    y = digit_root(x)
    e1 = 0
    if len(d_ee) > y:
        e1 = d_ee[y]
    x1 = x % 10 ** len(str(y))
    print(x, x1, y, e1)
