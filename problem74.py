"""
The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
"""

ff = []
for i in range(10):
    if i == 0:
        ff.append(1)
    else:
        ff.append(ff[i - 1] * i)
print(ff)


def next_n(n):
    return sum([ff[int(d)] for d in str(n)])


loop_nn = dict()
lengths = dict()
# xx = [145, 169, 871, 872, 69, 78, 540]
xx = range(1, 1000000)
rr = 0
for x in xx:
    ch = []
    next_x = 0
    while next_x not in ch and next_x not in loop_nn and next_x not in lengths:
        ch.append(next_x or x)
        next_x = next_n(next_x or x)

    i = len(ch)
    if next_x in lengths:
        s = len(ch) + lengths[next_x]
    else:

        if next_x not in loop_nn:
            i = ch.index(next_x)
            for y in ch[i:]:
                loop_nn[y] = len(ch) - i
                lengths[y] = len(ch) - i
        s = i + loop_nn[next_x]
    lengths[x] = s
    for j in range(i):
        lengths[ch[j]] = s - j
    if s == 60:
        rr += 1
        print(x, s, next_x, ch)
print(loop_nn)
# print(lengths)
print(rr)
