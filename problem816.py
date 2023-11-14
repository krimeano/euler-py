import time


def next_s(s0: int, mod: int):
    s = s0
    while True:
        yield s
        s = s * s % mod


def next_p(s0: int, mod: int, limit: int):
    g = next_s(s0, mod)
    c = 0
    while c < limit:
        yield next(g), next(g)
        c += 1


def distance_sq(p: tuple[int, int], q: tuple[int, int]) -> int:
    return (p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2


def min_dist_sq_brute(pp: list[tuple[int, int]]) -> int:
    size = len(pp)
    min_d = 0

    for ix in range(size - 1):
        for jy in range(ix + 1, size):
            d = distance_sq(pp[ix], pp[jy])
            if not min_d or d < min_d:
                min_d = d

    return min_d


def min_dist_sq(pp: list[tuple[int, int]]) -> int:
    size = len(pp)
    if size < 4:
        return min_dist_sq_brute(pp)
    m = size // 2
    pp_left, pp_right = pp[:m], pp[m:]
    delta_sq = min([min_dist_sq(pp_left), min_dist_sq(pp_right)])
    delta = delta_sq ** .5
    for p in pp_left:
        for q in pp_right:
            if q[0] - p[0] > delta:
                break
            if q[1] < p[1] - delta or q[1] > p[1] + delta:
                continue
            box_delta_qs = distance_sq(p, q)
            if box_delta_qs < delta_sq:
                delta_sq = box_delta_qs
                delta = delta_sq ** .5
    return delta_sq


def solve(s0: int, mod: int, limit: int) -> int:
    pp = sorted([x for x in next_p(s0, mod, limit)])
    return min_dist_sq(pp) ** 0.5


if __name__ == '__main__':
    st = time.time()
    a = 290797
    b = 50515093
    print(solve(a, b, 2000000))
    print('elapsed time:', time.time() - st, 'seconds')
