import math


def find_for_power(digits, power):
    out = []
    min_x = math.ceil(10 ** ((digits - 1) / power))
    max_x = min(math.floor(10 ** (digits / power)), 9 * digits)
    print(digits, power, min_x, max_x)
    if max_x < min_x:
        return []
    for x in range(min_x, max_x):
        xp = x ** power
        s = sum(int(d) for d in str(xp))
        # print('   ', x, xp, s)
        if x == s:
            out.append((xp, x, power,))
    return out


def find_for(digits):
    out = []
    max_pow = digits
    min_pow = 2
    for p in range(min_pow, max_pow + 1):
        out += find_for_power(digits, p)
    return out


result = []
for n in range(2, 16):
    result += find_for(n)
print(len(result))
for r in result:
    print(r)
print(sorted(x[0] for x in result))
