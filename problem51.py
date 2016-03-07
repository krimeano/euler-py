__author__ = 'sergeyp'

import mylib




def find_chains(p):
    # mylib.is_prime()
    out = []
    sp = str(p)
    search_digits = ['0', '1', '2']
    replace_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in range(len(search_digits)):
        sub_out = []
        if search_digits[i] in sp and i != p % 10:
            # print(i, 'found in', p)
            for j in range(len(replace_digits)):
                x = int(replace_digits[j].join(sp.split(search_digits[i])))
                if mylib.is_prime(x):
                    sub_out.append(x)
        if len(sub_out):
            out.append(sub_out)
    return out


def solve():
    a = mylib.find_primes_to_limit(100000000)
    for x in a:
        cc = find_chains(x)
        if len(cc):
            print(x, cc)

    return True


if __name__ == '__main__':
    print(solve())
