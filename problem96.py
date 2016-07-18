a_input = """
Grid 01
003020600
900305001
001806400
008102900
700000008
006708200
002609500
800203009
005010300
"""


class SudokuCell:
    def __init__(self, n):
        n = int(n)
        self.n = n

        self.possible = [n]

        if not n:
            self.possible = [x + 1 for x in range(9)]

    def __str__(self):
        if self.n:
            return str(self.n)

        return '[' + ''.join([str(x) for x in self.possible]) + ']'


class Sudoku:
    def __init__(self, a):
        self.raw = a
        self.data = []
        self.read_input(a)

    def read_input(self, a):
        self.raw = a
        # data = [[int(y) for y in x] ]
        #
        self.data = []
        for x in a.strip().split('\n')[1:]:
            self.data += [SudokuCell(y) for y in x]
        return self

    def __str__(self):
        # out = [str(x) for x in self.data]
        # for i in range(len(self.data)):
        #     out_row = ''
        #     if not i % 3:
        #         out.append('')
        #     row = self.data[i]
        #     for j in range(len(row)):
        #         if not j % 3:
        #             out_row += ' '
        #         out_row += str(row[j])
        #     out.append(out_row)
        out = []
        for i in range(0, len(self.data), 9):
            out_row = [str(x).center(11) for x in self.data[i:i + 9]]

            out.append(' '.join(out_row))
        return '\n'.join(out)


def solve():
    s = Sudoku(a_input)
    print(s)
    return True


if __name__ == "__main__":
    print(solve())
