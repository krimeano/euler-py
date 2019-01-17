import mylib, math


class Problem347:
    @staticmethod
    def test():
        return Problem347.find(10 ** 2) == 2262

    @staticmethod
    def solve():
        return Problem347.find(10 ** 7)

    @staticmethod
    def find(n):
        print(n)
        r = dict()
        for i in range(1, n + 1):
            dd = mylib.find_dividers(i, distinct=True)
            if len(dd) != 2:
                continue
            ix = 'x'.join([str(x) for x in dd])
            r[ix] = i
            print(i, ix)
        return sum([r[x] for x in r])

if __name__ == '__main__':
    if Problem347.test():
        print('*' * 79)
        print(Problem347.solve())
    else:
        print('NOT SOLVED YET')
