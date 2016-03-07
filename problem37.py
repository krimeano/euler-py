import mylib

myDigits = [1, 3, 5, 7, 9]

i = 0
complexPrimes = [
    [2, 3, 5, 7]
]
while len(complexPrimes[i]):
    newComplexPrimes = []

    for j in complexPrimes[i]:
        for k in myDigits:
            p = 10 * j + k
            if mylib.is_prime(p):
                newComplexPrimes.append(p)
    complexPrimes.append(newComplexPrimes)
    #print(newComplexPrimes)
    i+=1
s = 0
for pp in complexPrimes:
    for p in pp:
        if p < 10:
            continue
        q = int(str(p)[1:])
        while q:
            if not mylib.is_prime(q):
                break
            if q > 10:
                q = int(str(q)[1:])
            else:
                q = 0
        else:
            s += p
            print (p)

print(s)