import math

knownPrimes = []


def dividable(a, b):
    return a % b == 0


def hasDividerFromKnownPrimes(a):
    c = math.floor(a ** 0.5)
    # print('square root:', c)
    if a in knownPrimes:
        return False
    for b in knownPrimes:
        # print('next prime:', b)
        if b > c:
            return False
        if dividable(a, b):
            return b
    return False


def genPrime():
    if not len(knownPrimes):
        knownPrimes.append(2)
        yield 2
    if len(knownPrimes) == 1:
        knownPrimes.append(3)
        yield 3
    while True:
        x = knownPrimes[len(knownPrimes) - 1] + 2
        while hasDividerFromKnownPrimes(x):
            x += 2
        knownPrimes.append(x)
        yield x


primesGenerator = genPrime()


def findPrimesToLimit(L, explicit=False):
    r = L
    if not explicit:
        r = math.floor(L ** 0.5)
    m = 1
    if len(knownPrimes):
        m = knownPrimes[len(knownPrimes) - 1]
    while r >= m:
        m = primesGenerator.__next__()
    return knownPrimes[:-1]


def isPrime(a):
    if a < 2:
        return False
    findPrimesToLimit(a)
    return not hasDividerFromKnownPrimes(a)


def get_first_divider(a):
    if a < 2:
        return False
    findPrimesToLimit(a)
    return hasDividerFromKnownPrimes(a)


def find_dividers(a, f=2, distinct=False):
    d = []
    c = math.floor(a ** 0.5)
    if a < 2:
        return [a]
    pp = findPrimesToLimit(a)
    for b in pp:
        if b < f:
            continue
        if b > c:
            return [a]
        if dividable(a, b):
            d = [b]
            if a > b ** 2:
                d += find_dividers(a // b, b)
            if distinct:
                d = list(set(d))
                d.sort()
            return d
    d = [a]
    return d


def mutate(dd, prefix=''):
    l = len(dd)
    if not l:
        return []
    if l == 1:
        return [prefix + str(dd[0])]
    ss = set()
    for i in range(l):
        m = mutate(dd[0:i] + dd[i + 1:l], prefix + str(dd[i]))
        for a in m:
            ss.add(a)
    out = list(ss)
    out.sort()
    return out


def is_palindrome(a):
    b = str(a)
    return b[::-1] == b


if __name__ == '__main__':
    print(isPrime(1009))
    print(knownPrimes)