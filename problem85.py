__author__ = "krimeano"


def solve():
    r = (0, 0, -1)
    m = 2 * 10 ** 6
    for y in range(1, round(((8 * (m ** .5) - 1) ** 0.5 - 1) / 2)):
        x = round(((16 * m / y / (y + 1) + 1) ** .5 - 1) / 2)
        d = abs(m - x * (x + 1) * y * (y + 1) / 4)
        if r[2] < 0 or d < r[2]:
            r = (x, y, d)
            print(r)
    return r[0] * r[1]


if __name__ == '__main__':
    print(solve())
