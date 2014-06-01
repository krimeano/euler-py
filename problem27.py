import mylib


def findLongestAForB(b):
    low = - b
    aa = [x for x in range( low, 1000, 2)]
    d = 0
    n = 0
    c = 0
    aaaa = []
    while len(aa):
        aaa = []
        for a in aa:
            c = n * (n + a) + b
            #print(n, a, b, c)
            if c > 1 and mylib.isPrime(c):
                aaa.append(a)
        if len(aaa):
            aaaa = aaa
        aa = aaa
        n += 1
    return [n-1, aaaa]

if __name__ == '__main__':

    bb = mylib.findPrimesToLimit(1000, True)
    r = {}
    for b in bb:
        r[b] = findLongestAForB(b)
        print(b, r[b][0], r[b][1])

    maxC = 0
    maxB = 0
    maxA = 0
    for b in r:
        if r[b][0] > maxC:
            maxC = r[b][0]
            maxB = b
            maxA = r[b][1]
    print(maxC, maxA, maxB, maxA[0] * maxB)
