import fractions

if __name__ == '__main__':
    k = 0
    for x in range(1, 10001):
        q = fractions.SquareRootFraction(x)
        if len(q.r[1]) % 2:
            print(q.n, q.r)
            k += 1
    print(k)
