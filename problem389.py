"""
An unbiased single 4-sided die is thrown and its value, T, is noted.
T unbiased 6-sided dice are thrown and their scores are added together. The sum, C, is noted.
C unbiased 8-sided dice are thrown and their scores are added together. The sum, O, is noted.
O unbiased 12-sided dice are thrown and their scores are added together. The sum, D, is noted.
D unbiased 20-sided dice are thrown and their scores are added together. The sum, I, is noted.
Find the variance of I, and give your answer rounded to 4 decimal places.
"""

import mylib

def sum_outs(outs, outs_outs):
    print("calc sum outs")
    res = [0, ] * len(outs[len(outs) - 1])
    for dices in range(1, len(outs) + 1):
        xx = outs[dices - 1]
        y = outs_outs[dices - 1]
        for i in range(len(xx)):
            res[i] += y * xx[i]
    return tuple(res[1:-len(outs_outs)])


outs4 = (mylib.Dices.get_outs(4, 1),)
sum4 = sum_outs(outs4, (1,))
print(len(sum4),"\n")

outs6 = tuple(mylib.Dices.get_outs(6, x) for x in range(1, 4 + 1))
sum6 = sum_outs(outs6, sum4)
print(len(sum6), "\n")

outs8 = tuple(mylib.Dices.get_outs(8, x) for x in range(1, 4 * 6 + 1))
sum8 = sum_outs(outs8, sum6)
print(len(sum8), "\n")

outs12 = tuple(mylib.Dices.get_outs(12, x) for x in range(1, 4 * 6 * 8 + 1))
sum12 = sum_outs(outs12, sum8)
print(len(sum12), "\n")

outs20 = tuple(mylib.Dices.get_outs(20, x) for x in range(1, 4 * 6 * 8 * 12 + 1))
sum20 = sum_outs(outs20, sum12)
print(len(sum20), "\n")

outs = sum20
total = sum(outs)

mx = sum((i+1) * outs[i] for i in range(len(outs)))
mx2 = sum((i+1)*(i+1) * outs[i] for i in range(len(outs)))
print(total)
variance = mx2 - mx ** 2
print(mx, mx ** 2, mx2, variance)

print('%.4f' % variance)

