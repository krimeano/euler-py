"""
problem 76
"""
__author__ = 'sergeyp'

cached = {}


def find_ways(to_amount, limit):
    # print(to_amount, limit)
    if to_amount == 1:
        return 1
    if limit == 1:
        return 1
    r = 0
    cached_key = '-'.join((str(to_amount), str(limit)))
    if cached_key in cached:
        # print('found', cached_key)
        return cached[cached_key]
    for x in range(1, limit + 1):
        d = to_amount - x
        if d == 0:
            r += 1
        elif d > 0:
            r += find_ways(d, x)
    # d = to_amount - limit
    # for y in range(1, limit):
    #     r += find_ways(to_amount - limit, x)
    cached[cached_key] = r
    return r


def solve():
    result = 0
    x = 100
    result = find_ways(x, x) - 1
    return result


if __name__ == '__main__':
    print(solve())
