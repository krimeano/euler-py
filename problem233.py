def f(z):
    m_max = int((z - 1) ** 0.5 // 1)
    m_min = int((z / 2) ** 0.5 // 1)
    print(z, m_max)
    out = 0
    for m in range(m_min, m_max + 1):
        m2 = m ** 2
        n = round((z - m2) ** 0.5)
        if m2 + n ** 2 == z:
            print(m2, n ** 2)
            out += 1
    return out


if __name__ == '__main__':
    print(f(100))
