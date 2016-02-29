def is_right(x1, y1, x2, y2):
    if y1 in (0, y2) and x2 in (0, x1):
        return True
    a_sq = (x2 - x1) ** 2 + (y2 - y1) ** 2
    p_sq = x1 ** 2 + y1 ** 2
    q_sq = x2 ** 2 + y2 ** 2
    b_sq = min(p_sq, q_sq)
    c_sq = max(p_sq, q_sq)
    return c_sq == a_sq + b_sq


def find_right_triangles(a):
    print(a)
    n = 0
    for y1 in range(a + 1):
        for x1 in range(a + 1):
            if x1 == y1 == 0:
                continue
            for y2 in range(y1, a + 1):
                for x2 in range(a + 1):
                    if x1 == x2 and y1 == y2:
                        continue
                    if x1 == x2 == 0:
                        continue
                    if y1 == y2 == 0:
                        continue
                    if y1 == y2 and x2:
                        break
                    r = is_right(x1, y1, x2, y2)
                    n += r
                    if r:
                        print((x1, y1), (x2, y2), r)
    print(n)
    return n


if __name__ == '__main__':
    if find_right_triangles(2) == 14:
        print(find_right_triangles(50))
    else:
        print('NOT SOLVED YET')
