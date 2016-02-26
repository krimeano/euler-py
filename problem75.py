"""
(3, 4, 5)
(5, 12, 13)
(8, 15, 17)
(7, 24, 25)
(20, 21, 29)
(12, 35, 37)
(9, 40, 41)
(28, 45, 53)
(11, 60, 61)
(16, 63, 65)
(33, 56, 65)
(48, 55, 73)
(13, 84, 85)
(36, 77, 85)
(39, 80, 89)
(65, 72, 97)



(20, 99, 101)
(60, 91, 109)
(15, 112, 113)
(44, 117, 125)
(88, 105, 137)
(17, 144, 145)
(24, 143, 145)
(51, 140, 149)
(85, 132, 157)
(119, 120, 169)
(52, 165, 173)
(19, 180, 181)
(57, 176, 185)
(104, 153, 185)
(95, 168, 193)
(28, 195, 197)
(84, 187, 205)
(133, 156, 205)
(21, 220, 221)
(140, 171, 221)
(60, 221, 229)
(105, 208, 233)
(120, 209, 241)
(32, 255, 257)
(23, 264, 265)
(96, 247, 265)
(69, 260, 269)
(115, 252, 277)
(160, 231, 281)
(161, 240, 289)
(68, 285, 293)
"""
import mylib

known_triples_300 = (
    (3, 4, 5),
    (5, 12, 13),
    (8, 15, 17),
    (7, 24, 25),
    (20, 21, 29),
    (12, 35, 37),
    (9, 40, 41),
    (28, 45, 53),
    (11, 60, 61),
    (16, 63, 65),
    (33, 56, 65),
    (48, 55, 73),
    (13, 84, 85),
    (36, 77, 85),
    (39, 80, 89),
    (65, 72, 97),
    (20, 99, 101),
    (60, 91, 109),
    (15, 112, 113),
    (44, 117, 125),
    (88, 105, 137),
    (17, 144, 145),
    (24, 143, 145),
    (51, 140, 149),
    (85, 132, 157),
    (119, 120, 169),
    (52, 165, 173),
    (19, 180, 181),
    (57, 176, 185),
    (104, 153, 185),
    (95, 168, 193),
    (28, 195, 197),
    (84, 187, 205),
    (133, 156, 205),
    (21, 220, 221),
    (140, 171, 221),
    (60, 221, 229),
    (105, 208, 233),
    (120, 209, 241),
    (32, 255, 257),
    (23, 264, 265),
    (96, 247, 265),
    (69, 260, 269),
    (115, 252, 277),
    (160, 231, 281),
    (161, 240, 289),
    (68, 285, 293),
)


def make_simple_pythagorean_triples(s_max):
    m_max = int(((2 * s_max + 1) ** 0.5 - 1) // 2)
    print(m_max)
    kk = [x for x in known_triples_300]
    out = []
    for m in range(2, m_max + 1):
        n_max_1 = int(s_max / m // 2) - m
        print(m, m % 2 + 1, n_max_1, 2 * m * (m + n_max_1))
        n_max = min(n_max_1, m - 1)
        for n in range(m % 2 + 1, n_max + 1, 2):
            if n > 1 and mylib.find_gcd(m,n) > 1:
                continue
            if n >= m:
                break
            # print(m, 'x', n, '/', m_max, 'x', n_max)
            x = m * m - n * n
            y = 2 * m * n
            z = m * m + n * n
            t = (min(x, y, ), max(x, y, ),z )

            if z <= 300:
                if t not in known_triples_300:
                    raise AssertionError('WTF', t)
                kk.remove(t)
            s = 2 * m * (m + n)
            out.append(s)
            print(m, n, t, s)
    if len(kk):
        raise AssertionError('WTF2', kk)
    return out


if __name__ == '__main__':
    limit = 1500
    ss = make_simple_pythagorean_triples(limit)
    print(ss)
    xx = {}
    for s in ss:
        for x in range(s, limit + 1, s):
            if x in xx:
                xx[x] += 1
            else:
                xx[x] = 1
    print(xx)
    yy = [x for x in xx if xx[x] == 1]
    print(yy)
    print(len(yy))
    print('ololo')
