"""
problem 92
"""
__author__ = 'sergeyp'

my_numbers = dict()
loop_numbers = [1, 89]


def square_sum(a):
    return sum([int(x) ** 2 for x in str(a)])


def make_chain(a):
    print(a)
    while a not in loop_numbers:
        a = square_sum(a)
        print(a)
    return a


def jump_chain(a):
    if a in loop_numbers:
        return a
    if a in my_numbers:
        return my_numbers[a]
    b = jump_chain(square_sum(a))
    if not a % 10 ** 5:
        print(a, b, len(my_numbers))
    my_numbers[a] = b
    return b


def solve():
    d = [jump_chain(x) == 89 for x in range(1, 10 ** 7)]
    # print(my_numbers)
    print('-' * 79)
    return sum(d)


if __name__ == '__main__':
    print(solve())
