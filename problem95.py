import mylib

bb = {}
cc = {}
m = 10 ** 6 + 1
longest = (0,)
for a in range(m):
    if a in cc:
        continue

    b = sum(mylib.find_composite_dividers(a)[:-1])
    if a == b:
        cc[a] = (), (b,)
        continue
    c = [a]

    x = a
    y = sum(mylib.find_composite_dividers(x)[:-1])
    c_prefix = None
    c_amicable = None
    while y not in c:
        # print(y)
        if y in cc:
            c_prefix = tuple(c) + cc[y][0]
            c_amicable = cc[y][1]
            break
        c.append(y)
        if y > m:
            break
        x = y
        y = sum(mylib.find_composite_dividers(x)[:-1])
    if c_prefix and c_amicable:
        # print(' ', a, c_prefix, c_amicable)
        cc[a] = c_prefix, c_amicable
        continue

    if c[-1] > m:
        for i in range(len(c) - 1):
            z = c[i]
            if z in cc:
                continue
            cc[z] = tuple(c[i:-1]), (c[-1],)
            # print('   ', z, cc[z])
        continue
    i = c.index(y)
    c_prefix = tuple(c[:i])
    c_amicable = tuple(c[i:])
    cc[a] = c_prefix, c_amicable
    print(a, c_prefix, c_amicable)
    for j in range(i, len(c)):
        z = c[j]
        if z in cc:
            continue
        cc[z] = (), c_amicable
        # print(z, cc[z])
        # print('not processed', a, c, y, i, c_prefix, c_amicable)
    if len(c_amicable) > len(longest):
        longest = c_amicable
print(min(longest), longest)
# for x in cc:
#     print(x, cc[x])
