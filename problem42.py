import csv

zeroChar = ord('A') - 1


def getInput():
    with open('words.txt', 'r') as csvfile:
        r = csv.reader(csvfile, delimiter=',', quotechar='"')
        return r.__next__()


def countWord(word):
    s = 0
    for x in word:
        s += ord(x) - zeroChar
    return s


def getTriangle(to):
    a = 0
    n = 0
    out = []
    while a < to:
        n += 1
        a = int(n * (n + 1) / 2)
        out.append(a)
    return out


if __name__ == '__main__':
    tt = getTriangle(200)
    s = 0
    for w in getInput():
        if countWord(w) in tt:
            s += 1
    print(s)
