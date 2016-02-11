class Matrix:
    def __init__(self, txt):
        self.it = 0
        self.raw = txt
        self.data = []
        self._process_raw()

    def sum(self):
        self.it = 0
        s = self.compare(self.data)
        return s

    def compare(self, m):
        self.it += 1
        print('compare #' + str(self.it), m, )

        if len(m) == 1:
            return m[0][0]
        ss = []
        for i in range(len(m)):
            ss.append(m[i][0] + self.compare(self.cut(i, m)))
        print('max from', ss, max(ss))
        return max(ss)

    def cut(self, x, m):
        return [m[i][1:] for i in range(len(m)) if i != x]

    def _process_raw(self):
        data = [[int(y) for y in x.strip().split(' ') if len(y)] for x in self.raw.split('\n') if len(x)]
        a = len(data)
        for x in data:
            if a != len(x):
                raise AssertionError('can not parse the matrix')
        print(data)
        self.data = data


class Problem345:
    m0 = """
  7  53 183 439 863
497 383 563  79 973
287  63 343 169 583
627 343 773 959 943
767 473 103 699 303
"""
    m1 = """
  7  53 183 439 863 497 383 563  79 973 287  63 343 169 583
627 343 773 959 943 767 473 103 699 303 957 703 583 639 913
447 283 463  29  23 487 463 993 119 883 327 493 423 159 743
217 623   3 399 853 407 103 983  89 463 290 516 212 462 350
960 376 682 962 300 780 486 502 912 800 250 346 172 812 350
870 456 192 162 593 473 915  45 989 873 823 965 425 329 803
973 965 905 919 133 673 665 235 509 613 673 815 165 992 326
322 148 972 962 286 255 941 541 265 323 925 281 601  95 973
445 721  11 525 473  65 511 164 138 672  18 428 154 448 848
414 456 310 312 798 104 566 520 302 248 694 976 430 392 198
184 829 373 181 631 101 969 613 840 740 778 458 284 760 390
821 461 843 513  17 901 711 993 293 157 274  94 192 156 574
 34 124   4 878 450 476 712 914 838 669 875 299 823 329 699
815 559 813 459 522 788 168 586 966 232 308 833 251 631 107
813 883 451 509 615  77 281 613 459 205 380 274 302  35 805
"""

    @staticmethod
    def test():
        m = Matrix(Problem345.m0)
        return m.sum() == 33151

    @staticmethod
    def solve():
        m = Matrix(Problem345.m1)
        return m.sum()


if __name__ == '__main__':
    if Problem345.test():
        print('*' * 79)
        print(Problem345.solve())
    else:
        print('NOT SOLVED YET')
