__author__ = 'sergeyp'

import mylib


def solve():
    # a = mylib.find_primes_to_limit(25, True)
    # a = mylib.find_primes_to_limit(90, True)
    a = mylib.find_primes_to_limit(3940, True)

    s = sum(a)
    print(s, len(a), a)
    print ('-' * 79)
    sum_all(a)
    return True


def sum_all(a):
    y = len(a)
    i = y
    f = False
    while i:
        x = y - i
        if i % 2:
            r = range(1, x + 1)
        else:
            r = range(1)
        for j in r:
            b = a[j:j + i]
            s = sum(b)
            if mylib.is_prime(s):
                f = True
                print(s, b, i)
        if f:
            break
        i -= 1
    return True


if __name__ == '__main__':
    print(solve())
