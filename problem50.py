__author__ = 'sergeyp'

import mylib

if __name__ == '__main__':
    a = mylib.findPrimesToLimit(200, True)
    b = 0
    for x in a:
        print(x)
        b += x
    print(len(a), b, mylib.isPrime(b))
