"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""
__author__ = 'sergeyp'

import mylib

def sumPrimes(N):
    while len(mylib.knownPrimes) < N:
        print(mylib.primesGenerator.__next__())

if __name__ == '__main__':
    a = mylib.findPrimesToLimit(100, True)
    # b = 0
    # for x in a:
    #     print(x)
    #     b += x
    # print(len(a), b, mylib.isPrime(b))
    print (sum(a), a)