"""
problem 97
"""
__author__ = 'sergeyp'


def solve():
    n = 7830457
    k = 32
    m = 2 ** k
    a = 28433
    b = 10 ** 10
    print(n // k, 'iterations')
    x = 1
    while n > k:
        x = (x * m) % b
        n -= k
    x = (x * (2 ** n)) % b
    x = (a * x + 1) % b
    return x


if __name__ == '__main__':
    print(solve())
