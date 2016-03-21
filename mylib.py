import math, sys

known_primes = dict()


def dividable(a, b):
    return a % b == 0


def has_divider_from_known_primes(a):
    c = math.floor(a ** 0.5)
    # print('square root:', c)
    if a in known_primes:
        return False
    for b in sorted(known_primes):
        # print('next prime:', b)
        if b > c:
            return False
        if not a % b:
            return b
    return False


def gen_prime():
    if not len(known_primes):
        known_primes[2] = True
        yield 2
    if len(known_primes) == 1:
        known_primes[3] = True
        yield 3
    while True:
        x = max(known_primes.keys()) + 2
        # print(x)
        while has_divider_from_known_primes(x):
            x += 2
        known_primes[x] = True
        yield x


primes_generator = gen_prime()


def find_primes_to_limit(L, explicit=False):
    r = L
    if not explicit:
        r = math.floor(L ** 0.5)
    m = 1
    if len(known_primes):
        m = max(known_primes.keys())
    while r >= m:
        m = primes_generator.__next__()
        # print(m, 'prime')
    return dict((x, True) for x in known_primes if x <= r)


def is_prime(a):
    if a < 2:
        return False
    find_primes_to_limit(a)
    return not has_divider_from_known_primes(a)


def get_first_divider(a):
    if a < 2:
        return False
    find_primes_to_limit(a)
    return has_divider_from_known_primes(a)


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
    pp = find_primes_to_limit(a)
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
    # print(a, b)
    if a == b:
        return a
    x = max(a, b)
    y = min(a, b)
    r = x % y
    cache_key = '-'.join([str(x), str(y)])
    if cache_key in gcd_cache:
        # print('   ', cache_key, 'found cache!')
        return gcd_cache[cache_key]
    if r:
        gcd_cache[cache_key] = find_gcd(y, r)
    else:
        gcd_cache[cache_key] = y
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
    # if is_prime(n):
    #     return n -1
    dd = find_dividers(n, distinct=True)
    phi = n
    for d in dd:
        phi *= (d - 1) / d
    return int(phi)


def make_primes_sieve_atkin(limit):
    """
    https://ru.wikipedia.org/wiki/%D0%A0%D0%B5%D1%88%D0%B5%D1%82%D0%BE_%D0%90%D1%82%D0%BA%D0%B8%D0%BD%D0%B0
    :param limit:
    :return:
    """
    out = {}
    out[2] = True
    out[3] = True
    r = int(limit ** 0.5 // 1) + 1

    x2 = 0
    for i in range(1, r):
        x2 += 2 * i - 1
        y2 = 0
        for j in range(1, r):
            y2 += 2 * j - 1
            n = 4 * x2 + y2
            if (n <= limit) and (n % 12 == 1 or n % 12 == 5):
                print("\033[F\033[K", i, j, n, 'invert')
                out[n] = not out[n] if n in out else True

            # n = 3 * x2 + y2
            n -= x2  # Optimization
            if (n <= limit) and (n % 12 == 7):
                print("\033[F\033[K", i, j, n, 'invert')
                out[n] = not out[n] if n in out else True

            # n = 3 * x2 - y2;
            n -= 2 * y2  # Optimization
            if (i > j) and (n <= limit) and (n % 12 == 11):
                print("\033[F\033[K", i, j, n, 'invert')
                out[n] = not out[n] if n in out else True

    for i in range(1, r):
        if i in out and out[i]:
            n = i * i
            print("\033[F\033[K", n, 'is square')
        for j in range(n, limit + 1, n):
            out[j] = False

    for i in range(9, limit + 1, 3):
        out[i] = False

    for i in range(25, limit + 1, 5):
        out[i] = False

    return dict((x, True) for x in out if out[x])


def prob_c(k, n):
    r = 1
    k1 = min(k, n - k)
    if k1 < 0:
        return 0
    for i in range(0, k1):
        r *= n - i
        r //= i + 1
    return r


cache_factorial = dict()


def factorial(n):
    if n <= 0:
        return 1
    if n not in cache_factorial:
        cache_factorial[n] = n * factorial(n - 1)
    return cache_factorial[n]


def factorial_mod(n, p):
    if n < 2:
        return 1
    out = 2
    for x in range(3, n + 1):
        out = (out * x) % p
    return out


class Fraction:
    def __init__(self, n, d):
        self.n = n
        self.d = d

    def get_period(self):
        # print(self.n / self.d, "\n")
        p = ''
        n = self.n % self.d
        d = self.d
        nn = set()
        while n not in nn:
            # print("\033[F\033[K" + str(len(p)), p[-5:], n, d)
            nn.add(n)
            p += str((n * 10) // d)
            n = (n * 10) % d
        return p


if __name__ == '__main__':

    for n in range(2, 11):
        for k in range(1, n // 2 + 1):
            print(k, n, prob_c(k, n))
