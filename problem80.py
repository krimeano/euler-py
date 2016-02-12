import mylib

if __name__ == '__main__':
    m = 2
    for n in range(2, 10 ** 7 + 1):
        phi = mylib.totient(n)
        if sorted(str(n)) == sorted(str(phi)):
            r = n / phi
            if r < m:
                m = r
                print(n, phi, n / phi)
