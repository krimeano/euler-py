import math, sys

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


cache_dividers = {}
cache_dividers_distinct = {}


def find_dividers(a, f=2, distinct=False):
    cache = cache_dividers_distinct if distinct else cache_dividers
    if a in cache:
        return cache[a]
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
            if a >= b ** 2:
                d += find_dividers(a // b, b)
            if distinct:
                d = list(set(d))
                d.sort()
            cache[a] = d
            return d
    d = [a]
    cache[a] = d
    return d


def gather_dividers(a):
    dividers = find_dividers(a)
    out = []
    for x in dividers:
        is_found = False
        for xx in out:
            if x in xx:
                xx.append(x)
                is_found = True
        if not is_found:
            out.append([x])
    return out


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


gcd_cache = {}


def find_gcd(a, b):
    """
    Returns the Greatest common divisor
    :param a:
    :param b:
    :return:
    """
    if a == b:
        return a
    x = max(a, b)
    y = min(a, b)
    cache_key = '-'.join([str(x), str(y)])
    if cache_key in gcd_cache:
        # print('   ', cache_key, 'found cache!')
        return gcd_cache[cache_key]
    gcd_cache[cache_key] = find_gcd(y, x - y)
    return gcd_cache[cache_key]


def find_relaitvely_primes(n):
    r = []
    if n < 2:
        return r
    r.append(1)
    for x in range(2, n):
        # print(x)
        if find_gcd(n, x) == 1:
            r.append(x)

    return r


def hcf(x, y):
    """This function implements the Euclidian algorithm
    to find H.C.F. of two numbers"""

    while (y):
        x, y = y, x % y

    return x


def mult(l):
    out = 1
    for x in l:
        if not x:
            return 0
        out *= x
    return out


if __name__ == '__main__':
    # print(find_relaitvely_primes(1000))
    # print(find_relaitvely_primes(10000))
    findPrimesToLimit(10)
