def eliminate_from_left(xx):
    return tuple(xx[i] for i in range(1, len(xx), 2))


def eliminate_from_right(xx):
    return tuple(eliminate_from_left(xx[::-1])[::-1])


def full_eliminate(xx):
    d = True
    print(xx, end=' ')
    n = 0
    while len(xx) > 1:
        n += 1
        if n > 10:
            break
        xx = (eliminate_from_left if d else eliminate_from_right)(xx)
        print('=>', xx, end=' ')
        d = not d
    print()
    return xx[0]


for b in range(1, 100):
    aa = tuple(x + 1 for x in range(b))
    print(b, full_eliminate(aa))
