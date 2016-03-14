if __name__ == '__main__':
    r = 0
    for n in range(2, 10 ** 1 + 11):
        if not n % 10 ** 3:
            print(n)
        s_max = 0
        ss = [(x * x) % n for x in range(1, n // 2 + 1)]
        tt = [((x * n) ** 0.5 // 1) ** 2 % n for x in range(1, ((n // 2) ** 2) // n + 1)]
        s_max = max(ss)
        t_max = max(tt or [1])
        r += s_max
        print(n, s_max, ss)
        print(n, t_max, tt)
    print(r)
