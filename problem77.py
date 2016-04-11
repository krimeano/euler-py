"""
It is possible to write ten as the sum of primes in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written as the sum of primes in over five thousand different ways?
"""
import mylib

pp = sorted(mylib.primes_from_file(100))


def find_ways(number, max_a=0):
    ways = []
    for a in pp:
        if a > number:
            break
        if max_a and a > max_a:
            break
        if number == a:
            ways.append([a])
            continue
        append_ways = find_ways(number - a, a)
        for w in append_ways:
            ways.append([a] + w)

    return ways


print(pp)
for x in range(2, 20):
    print(x, find_ways(x))
print(len(find_ways(71)))
