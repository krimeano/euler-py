class MatrixPath:
    def __init__(self, txt_matrix, paths=2):
        self.paths = paths
        self.matrix = [[int(y) for y in x.strip().split(",") if len(y)] for x in txt_matrix.strip().split("\n")]
        self.assert_matrix()
        self.rows = len(self.matrix)
        self.cols = self.rows and len(self.matrix[0])

    def assert_matrix(self):
        s = -1
        for x in self.matrix:
            if s < 0:
                s = len(x)
            assert s == len(x)

    def next_neighbours(self, i=-1, j=-1):
        if self.paths == 2:
            return self.next_neighbours_2(i, j)

        if self.paths == 3:
            return self.next_neighbours_3(i, j)

        if self.paths == 4:
            return self.next_neighbours_4(i, j)

    def next_neighbours_2(self, i=-1, j=-1):
        if i < 0 or j < 0:
            return (0, 0),
        if i == 255 or j == 255:
            return tuple()
        if i == self.rows - 1 and j == self.cols - 1:
            return (255, 255),
        out = []
        if i < self.rows - 1:
            out.append((i + 1, j))
        if j < self.cols - 1:
            out.append((i, j + 1))
        return tuple(out)

    def next_neighbours_3(self, i=-1, j=-1):
        if i == 255 or j == 255:
            return tuple()
        if j < 0:
            return tuple((x, 0) for x in range(self.rows))
        if j == self.cols - 1:
            return tuple([(x, j) for x in range(self.rows)] + [(255, 255)])
        out = []
        if i > 0:
            out.append((i - 1, j))
        if i < self.rows - 1:
            out.append((i + 1, j))
        if j < self.cols - 1:
            out.append((i, j + 1))
        return tuple(out)

    def next_neighbours_4(self, i=-1, j=-1):
        if i < 0 or j < 0:
            return (0, 0),
        if i == 255 or j == 255:
            return tuple()
        out = []

        if 255 > i > 0:
            out.append((i - 1, j))
        if i < self.rows - 1:
            out.append((i + 1, j))
        if 255 > j > 0:
            out.append((i, j - 1))
        if j < self.cols - 1:
            out.append((i, j + 1))

        if i == self.rows - 1 and j == self.cols - 1:
            out.append((255, 255))
        return tuple(out)


class Node:
    def __init__(self, i, j, m_path):
        self.i = i
        self.j = j
        self.m_path = m_path
        self.value = 0
        if -1 < i < m_path.rows and -1 < j < m_path.cols:
            self.value = m_path.matrix[i][j]
        self.path = []
        self.path_has_changed = False

    def get_next(self):
        return self.m_path.next_neighbours(self.i, self.j)

    def get_previous(self):
        return self.m_path.previous_neighbours(self.i, self.j)

    def __str__(self):
        return '%d, %d, %d' % (self.i, self.j, self.value)


class Graph:
    def __init__(self, txt_matrix, paths=2):
        self.m_path = MatrixPath(txt_matrix, paths)
        self.nodes = dict()
        self.nodes[(-1, -1)] = Node(-1, -1, self.m_path)
        self.nodes[(255, 255)] = Node(255, 255, self.m_path)
        for x in range(self.m_path.cols):
            for y in range(self.m_path.rows):
                self.nodes[(x, y)] = Node(x, y, self.m_path)

    @staticmethod
    def calc_path_length(n_path):
        if not len(n_path):
            return -1
        return sum(x.value for x in n_path)

    @staticmethod
    def print_path(n_path):
        return tuple((x.i, x.j, x.value) for x in n_path)

    def make_path(self):
        self.nodes[(-1, -1)].path_has_changed = True
        # self.iterate_path()
        # self.iterate_path()
        # self.iterate_path()
        while len([self.nodes[x] for x in self.nodes if self.nodes[x].path_has_changed]):
            self.iterate_path()
        return self.nodes[(255, 255)].path + [self.nodes[(255, 255)]]

    def iterate_path(self):
        print('----- iteration -----')
        nn = [self.nodes[x] for x in self.nodes if self.nodes[x].path_has_changed]
        change_path_after_iteration = []
        for n in nn:
            n.path_has_changed = False
            n_path = n.path + [n]
            p = self.calc_path_length(n_path)
            print(n, p, self.print_path(n.path))
            for x in n.get_next():
                k = self.nodes[x]
                q = self.calc_path_length(k.path)
                if q < 0 or p < q:
                    k.path = n_path
                    change_path_after_iteration.append(k)
        for k in change_path_after_iteration:
            k.path_has_changed = True
        return self
