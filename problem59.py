__author__ = 'palutser'


def solve():
    result = 0
    for x in [' ', ',', '.', 'A', 'Z', 'a', 'z']:
        print(x, '{0:b}'.format(ord(x)), ord(x))
    print('-' * 79)
    with open('p059_cipher.txt') as f:
        raw_data = f.read()

    data = [int(x) for x in raw_data.split(',')]
    print(data)
    code = 'god'
    for i in range(len(data)):
        _e = '\n'
        current_x = ord(code[i % 3])
        # print(current_x, ' ')
        decoded_x = data[i] ^ current_x
        print(chr(decoded_x), end='')
        result += decoded_x
        if not (i + 1) % 3:
            # print('')
            _e = ' '

            # print(chr(data[i]), end='')
            # print('{0:b}'.format(data[i]), end=_e)
    print('\n' + '-' * 79)
    return result


if __name__ == '__main__':
    print(solve())
