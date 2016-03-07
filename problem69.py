__author__ = 'palutser'
import mylib, sys


def get_totient(n):
    dd = mylib.find_dividers(n, distinct=True)
    phi = n - 1
    print(dd)
    for d in dd:
        if d == n:
            continue
        phi -= n / d - 1
    print(n, phi)
    return n / phi
    # return n / (len(mylib.find_relaitvely_primes(n)) or 1)


def solve():
    result = 0

    max_t = 1
    for x in range(59, 61):
        # if mylib.is_prime(x):
        #     continue
        t = get_totient(x)
        max_t = max(t, max_t)
        # if max_t == t:
        print(x, t)
    return result


if __name__ == '__main__':
    print(solve())
    # sys.stdout.write("\033[F")
    # sys.stdout.write("\033[K")
