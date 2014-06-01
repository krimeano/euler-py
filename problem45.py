__author__ = 'sergeyp'


for i in range(1, 100000, 1):
    pentNumber = int(i * (3 * i - 1) / 2)
    D = 1 + 8 * pentNumber
    r = D ** 0.5
    if r % 1:
        continue
    n = (r + 1) / 4
    if n % 1:
        continue
    hexNumber = n * (2 * n - 1)
    print (i, pentNumber, D, r, n, hexNumber)
