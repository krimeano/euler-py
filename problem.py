a = int(input('Введите число'))

if a % 3 == 0:
    if a % 5 == 0:
        print('Fizz Buzz')
    else:
        print('Fizz')
elif a % 5 == 0:
    print('Buzz')
else:
    print(str(a))
