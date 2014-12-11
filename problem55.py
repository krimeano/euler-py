__author__ = 'sergeyp'


def revert_number(a):
    return int(str(a)[::-1])


def is_lychrel (a):
    r = revert_number(a)
    for c in range(50):
        if a == r and c:
            break
        a += r
        r = revert_number(a)
    else:
        return True
    return False


def solve():
    return sum([is_lychrel(x) for x in range(10000)])


if __name__ == '__main__':
    print(solve())
