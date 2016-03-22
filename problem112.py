
def is_bouncy(n):
    s = ''.join(sorted(str(n)))
    return not (int(s) == n or int(s[::-1]) == n)


def find_first(p):
    b = 0
    nb = 1
    n = 1
    while b / (nb + b) < p:
        n += 1
        if is_bouncy(n):
            b += 1
        else:
            nb +=1

    return n

def test():
    test1 = [{'n':123, 'e': False}, {'n':987, 'e': False}, {'n':645, 'e': True}, {'n':546, 'e': True}]
    for x in test1:
        r = is_bouncy(x['n'])
        print (x['n'], x['e'], r)
        if r != x['e']:
            print('FAILED')
            return False
    test2 = [{'p': 0.5, 'e': 538}, {'p': 0.9, 'e': 21780}]
    for x in test2:
        r = find_first(x['p'])
        print(x['p'], x['e'], r)
        if r != x['e']:
            print('FAILED')
            return False
    return True


def solve():
    return find_first(0.99)


if __name__ == '__main__':
    if test():
        print('-'*79)
        print (solve())
    else:
        print('NOT SOLVED YET')