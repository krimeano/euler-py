import math

knownPrimes = []


def dividable(a, b):
    return a % b == 0


def hasDividerFromKnownPrimes(a):
    c = math.floor(a ** 0.5)
    #print('square root:', c)
    if a in knownPrimes:
        return False
    for b in knownPrimes:
        #print('next prime:', b)
        if b > c:
            return False
        if dividable(a, b):
            return True
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

if __name__ == '__main__':
    print(isPrime(1009))
    print(knownPrimes)