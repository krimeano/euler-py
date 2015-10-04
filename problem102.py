__author__ = 'krimeano'


def mult_v(ax, ay, bx, by):
    return ax * by - ay * bx


def solve():
    r = 0
    with open("p102_triangles.txt", "r") as f:
        tt = [[int(y) for y in x.split(',')] for x in f.readlines()]

    for t in tt:
        a = mult_v(t[0], t[1], t[2], t[3])
        b = mult_v(t[2], t[3], t[4], t[5])
        c = mult_v(t[4], t[5], t[0], t[1])
        ii = (a < 0 and b < 0 and c < 0) or (a > 0 and b > 0 and c > 0)
        r += ii
        # print(t, (a, b, c), ii)
    return r


if __name__ == '__main__':
    print(solve())
