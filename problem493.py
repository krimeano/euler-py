"""
70 colored balls are placed in an urn, 10 for each of the seven rainbow colors.

What is the expected number of distinct colors in 20 randomly picked balls?

Give your answer with nine digits after the decimal point (a.bcdefghij).
"""
import mylib

s = 0
t = 0
for i in range(2, 8):
    x = mylib.prob_c(i, 7)  # outcome to get i distinct colors of i
    # 20 - i: number of balls to take to fill 20
    # 9 * i: number of balls of needed colors
    # 70 - i: total number of balls
    y = mylib.prob_c(20 - i, 9 * i)
    z = mylib.prob_c(20 - i, 70 - i)
    w = x * z // y
    s += i * w
    t += w
    print(i, w)
a = mylib.prob_c(20, 70)
print(a)
print(a / t)
print(s / t)
