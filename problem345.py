def print_matrix(mx):
    w = len(str(max([max(x) for x in mx])))
    print('[[' + ']\n ['.join([', '.join([' ' * (w - len(str(y))) + str(y) for y in x]) for x in mx]) + ']]\n')


def transpone(mx):
    return [[mx[j][i] for j in range(len(mx[i]))] for i in range(len(mx))]


class Matrix:
    def __init__(self, txt):
        self.raw = txt
        self.data = []
        self.data_r = []
        self.data_n = []
        self._process_raw()

    def _process_raw(self):
        data = [[int(y) for y in x.strip().split(' ') if len(y)] for x in self.raw.split('\n') if len(x)]
        a = len(data)
        for x in data:
            if a != len(x):
                raise AssertionError('can not parse the matrix')
        self.data = data

    def _revert(self):
        m = max(max(x) for x in self.data)
        self.data_r = [[m - y for y in x] for x in self.data]

    def _reduce_rows(self):
        for i in range(len(self.data_r)):
            x = self.data_r[i]
            m = min(x)
            self.data_r[i] = [y - m for y in x]

    def _reduce_columns(self):
        self.data_r = transpone(self.data_r)
        self._reduce_rows()
        self.data_r = transpone(self.data_r)

    def _find_nulls(self):
        self.data_n = [[1 - (y and 1 or 0) for y in x] for x in self.data_r]

    def sum(self):
        print_matrix(self.data)

        print('revert values to find minimum')
        self._revert()
        print_matrix(self.data_r)

        print('reduce rows')
        self._reduce_rows()
        print_matrix(self.data_r)

        print('reduce columns')
        self._reduce_columns()
        print_matrix(self.data_r)

        print('find nulls')
        self._find_nulls()
        print_matrix(self.data_n)

        print('get graph')
        graph = Graph(self.data_r)
        print('edges:', graph.edges)
        return 0


class Graph:
    def __init__(self, mx):
        self._matrix = mx
        self.edges = tuple()
        self._find_edges()

    def _find_edges(self):
        for i in range(len(self._matrix)):
            for j in range(len(self._matrix[i])):
                if not self._matrix[i][j]:
                    self.edges = self.edges + ((i, j),)


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

"""
[0, 4), [1, 4), [2, 4), [3, 2), [3, 3), [4, 0), [4, 1)
(0, 4], [1, 4), [2, 4), (3, 2], [3, 3), (4, 0], [4, 1)

"""
