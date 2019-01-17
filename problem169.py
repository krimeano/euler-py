import math

n = 10
_a = '{0:b}'.format(n)

_b = '0' * len(_a)

processed_options = dict()
options = [(_a, _b)]


def split_ab(a, b):
    out = []
    print("\033[F\033[K" + "\033[F\033[K" + "\033[F\033[K", a, '\n', b)
    for i in range(len(a) - 1):

        if a[i] == '0':
            if b[i] == '1':
                raise AssertionError("0-1 pair shouldn't appear")
            continue
        if a[i + 1] == '1':
            continue
        if b[i + 1] == '1':
            raise AssertionError("0-1 pair shouldn't appear")

        c = [x for x in a]
        d = [x for x in b]
        if b[i] == '1':
            d[i] = '0'
        else:
            c[i] = '0'
        c[i + 1] = '1'
        d[i + 1] = '1'
        cd = ''.join(c), ''.join(d)
        # print(' ', cd)
        out.append(cd)
    return out


while len(options):
    ab = options[0]
    options = options[1:]
    if ab not in processed_options:
        options += split_ab(ab[0], ab[1])
        processed_options[ab] = True
        print(len(processed_options))
print(len(processed_options))
