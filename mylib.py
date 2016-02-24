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
        if not a % b:
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
        print(m, 'prime')
    return [x for x in knownPrimes if x <= r]


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
        if not a % b:
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


def product_lists(aa, bb, c_max=0):
    cc = []
    for a in aa:
        for b in bb:
            c = a * b
            if not c_max or c <= c_max:
                cc.append(c)
    return sorted(cc)


def find_composite_dividers(a, c_max=0):
    if a == 1:
        return [1]
    gathered = gather_dividers(a)
    vvv = []
    cc = [1]
    for dd in gathered:
        vv = []
        d = dd[0]
        for i in range(len(dd) + 1):
            vv.append(d ** i)
        vvv.append(vv)
    for vv in vvv:
        cc = product_lists(cc, vv, c_max)
    return cc


def find_rational_dividers(a, c_max=0):
    if a == 1:
        return [1]
    gathered = gather_dividers(a)
    vvv = []
    cc = [1]
    for dd in gathered:
        vv = []
        d = dd[0]
        for i in range(-len(dd), len(dd) + 1):
            vv.append(d ** i)
        vvv.append(vv)
    for vv in vvv:
        cc = product_lists(cc, vv, c_max)
    return cc


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


def totient(n):
    if n < 2:
        return 1
    # if isPrime(n):
    #     return n -1
    dd = find_dividers(n, distinct=True)
    phi = n
    for d in dd:
        phi *= (d - 1) / d
    return int(phi)


def make_primes_sieve(limit):
    r = math.floor(limit ** 0.5)
    known_primes = make_primes_sieve_init(r)
    p_max = max(known_primes)
    print(limit, r, known_primes[-10:], "\n")
    modulo = 1
    p_min = 1
    pp = set()
    for x in known_primes:
        if modulo * x > r:
            break
        modulo *= x
        p_min = x
        pp.add(x)
    for p in [1] + [x for x in known_primes if (x > p_min) and (x < modulo)]:
        print("\033[F\033[K", p, modulo)
        pp |= set(range(p, limit, modulo))
    # print(sorted(pp))
    if 1 in pp:
        pp.remove(1)
    for p in [x for x in known_primes if x > p_min]:
        print("\033[F\033[K", p, '/', p_max, end=' ')
        ss = set(range(p ** 2, limit + 1, p))
        print('-', len(ss), 'items')
        pp -= ss
    return sorted(pp)


def make_primes_sieve_init(L):
    r = int(L ** 0.5 // 1)
    pp = set(range(5, L + 1, 6)) | set(range(7, L + 1, 6))
    dd = set(range(5, r + 1, 6)) | set(range(7, r + 1, 6))
    pp.add(2)
    pp.add(3)
    print("\033[F\033[K", 1, ', len = ', len(dd))
    while len(dd):
        d = min(dd)
        pp -= set(range(d * 2, L + 1, d))
        dd -= set(range(d, r + 1, d))
        print("\033[F\033[K", d, ', len =', len(dd))
    return sorted(pp)


if __name__ == '__main__':
    print(find_rational_dividers(20))  # 1, 2, 4, 5, 10, 20, 1/2, 1/4, 1/5, 1/10, 1/20, 2/5, 4/5
