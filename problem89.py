class RomanNumeral:
    """
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000

    Numerals must be arranged in descending order of size.
    M, C, and X cannot be equalled or exceeded by smaller denominations.
    D, L, and V can each only appear once.

    - Only one I, X, and C can be used as the leading numeral in part of a subtractive pair.
    - I can only be placed before V and X.
    - X can only be placed before L and C.
    - C can only be placed before D and M.
    """
    letters = "IVXLCDM"

    def __init__(self, value):
        self.is_valid = False
        self.value = ''
        self.value_normal = ''
        self.value_number = 0
        self.value_raw = ''
        self.read(value)

    def read(self, value):
        self.value_raw = str(value)
        self.is_valid = self._is_valid()
        if not self.is_valid:
            self.value = ''
            self.value_number = 0
            self.value_normal = ''
        else:
            self.value = self.value_raw.upper()
            self.value_number = self._calculate_value()
            self.value_normal = self._number_to_roman()

    def _is_valid(self):
        return self._is_valid_symbols() and self._is_valid_row() and self._is_valid_sequence()

    def _is_valid_symbols(self):
        v = self.value_raw.upper()
        return not len(set(v) - set(RomanNumeral.letters))

    def _is_valid_row(self):
        v = self.value_raw.upper()
        for i in range(1, len(self.letters), 2):
            w = self.letters[i]
            if len(v.split(w)) > 2:
                return False
        return True

    def _is_valid_sequence(self):
        return True

    @staticmethod
    def index_to_value(ix):
        return (5 if ix % 2 else 1) * 10 ** (ix // 2)

    @staticmethod
    def letter_to_value(x):
        x = x.upper()
        if x not in RomanNumeral.letters:
            return 0
        return RomanNumeral.index_to_value(RomanNumeral.letters.index(x))

    def _calculate_value(self):
        s = 0
        for i in range(len(self.value)):
            x = self.value[i]
            y = self.value[i + 1] if i < len(self.value) - 1 else ''
            sign = 1
            if y and RomanNumeral.letters.index(y) > RomanNumeral.letters.index(x):
                sign = -1
            a = RomanNumeral.letter_to_value(x)
            # print(x, a)
            s += a * sign
        return s

    def _number_to_roman(self):
        out = ''
        n = self.value_number
        for i in range(len(self.letters), 0, -1):
            j = i - 1
            w = self.letters[j]
            a = RomanNumeral.letter_to_value(w)
            while a <= n:
                n -= a
                out += w
            # print(a, n)
            if j > 0:
                k = j - 2 + j % 2
                x = self.letters[k]
                a -= RomanNumeral.letter_to_value(x)
                if a <= n:
                    out += x + w
                    n -= a

        return out


class Problem89:
    @staticmethod
    def test():

        passed = True
        cases = [
            {"v": "MDCLXVI", "valid": True, "amount": 1666, "normal": "MDCLXVI"},
            {"v": "MDCLXVJ", "valid": False},
            {"v": "I", "valid": True, "amount": 1},
            {"v": "V", "valid": True, "amount": 5},
            {"v": "X", "valid": True, "amount": 10},
            {"v": "D", "valid": True, "amount": 500},
            {"v": "A", "valid": False},
            {"v": "II", "valid": True, "amount": 2, "normal": "II"},
            {"v": "MCMXCIV", "amount": 1994, "normal": "MCMXCIV"},
            {"v": "MMMXLVIIII", "amount": 3049, "normal": "MMMXLIX"},
            {"v": "VV", "valid": False},
        ]
        for x in cases:
            rn = RomanNumeral(x["v"])

            if "valid" in x and rn.is_valid != x["valid"]:
                print("TEST NOT PASSED:", rn.value_raw, "| valid:", rn.is_valid, "| expected: ", x["valid"])
                passed = False
            if "amount" in x and rn.value_number != x["amount"]:
                print("TEST NOT PASSED:", rn.value_raw, "| amount:", rn.value_number, "| expected: ", x["amount"])
                passed = False
            if "normal" in x and rn.value_normal != x["normal"]:
                print("TEST NOT PASSED:", rn.value_raw, "| normal:", rn.value_normal, "| expected: ", x["normal"])
                passed = False
        return passed

    @staticmethod
    def solve():
        with open('p089_roman.txt') as f:
            lines = f.read().splitlines()
        s = 0
        for x in lines:
            r = RomanNumeral(x)
            d = len(r.value) - len(r.value_normal)
            s += d
            if d:
                print(x, r.value_number, r.value_normal, d)
        return s


if __name__ == '__main__':
    if Problem89.test():
        print(Problem89.solve())
    else:
        print('NOT SOLVED YET')
