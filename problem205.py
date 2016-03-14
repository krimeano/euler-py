"""
                  0   1   1   1   1   0
            0   1   2   3   4   3   2   1   0
      0   1   3   6  10  12  12  10   6   3   1   0
0   1   4  10  20  31  40  44  40  31  20  10   4   3   1   0

"""


def calc_outs(dice, outs=(1,)):
    affix = (0,) * (dice - 1)
    old_outs = (0,) + affix + outs + affix
    new_outs = tuple()
    for i in range(len(old_outs) - dice + 1):
        out = 0
        for j in range(dice):
            out += old_outs[i + j]
        new_outs = new_outs + (out,)
    # print(dice, old_outs, new_outs)
    return new_outs


def get_outs(dice, dices):
    outs = (1,)
    for i in range(dices):
        outs = calc_outs(dice, outs)
    return outs


outs49 = get_outs(4, 9)
sum49 = sum(outs49)
print(sum49, outs49)
outs66 = get_outs(6, 6)
sum66 = sum(outs66)
print(sum66, outs66)
"""
calc wins for outs
"""
s = 0
for x in range(len(outs49)):
    s += outs49[x] * sum(outs66[:x])
print(s / sum66 / sum49)
