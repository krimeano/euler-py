__author__ = 'sergeyp'

coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200

def findWays(fromSum, toSum, maxCoin):
    s = 0
    w = 0
    for c in coins:
        if c > maxCoin:
            continue
        s = fromSum + c
        if s > toSum:
            continue
        elif s == toSum:
            w += 1
        else:
            w += findWays(s, toSum, c)
    return w

if __name__ == '__main__':
    print(findWays(0, target, coins[len(coins) - 1]))
