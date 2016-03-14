"""
                  0   1   1   1   1   0
            0   1   2   3   4   3   2   1   0
      0   1   3   6  10  12  12  10   6   3   1   0
0   1   4  10  20  31  40  44  40  31  20  10   4   3   1   0

"""


def calc_outs_next_dice(dice, outs=(1,)):
    affix = (0,) * dice
    outs = affix + outs + affix
    new_outs = tuple(sum(outs[i + j] for j in range(dice)) for i in range(len(outs) - dice + 1))
    return new_outs


def get_outs(dice, dices):
    outs = (1,)
    for i in range(dices):
        outs = calc_outs_next_dice(dice, outs)
    return outs


outs4x9, outs6x6 = get_outs(4, 9), get_outs(6, 6)
print('%.7f' % (sum(outs4x9[x] * sum(outs6x6[:x]) for x in range(len(outs4x9))) / sum(outs6x6) / sum(outs4x9)))
