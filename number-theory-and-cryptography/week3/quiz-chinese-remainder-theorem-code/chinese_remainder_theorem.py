def ExtendedEuclid(a, b):
    if b == 0:
        x, y = 1, 0
    else:
        (p, q) = ExtendedEuclid(b, a % b)
        x = q
        y = p - q * (a // b)

    return (x, y)


def ChineseRemainderTheorem(n1, r1, n2, r2):
    (x, y) = ExtendedEuclid(n1, n2)
    n = r1 * n2 * y + r2 * n1 * x
    return n % (n1 * n2)
