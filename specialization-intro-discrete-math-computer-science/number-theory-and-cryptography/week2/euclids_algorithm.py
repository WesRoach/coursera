def gcd_naive(a, b):
    assert a >= 0 and b >= 0 and a + b > 0

    if a == 0 or b == 0:
        return max(a, b)

    for d in range(min(a, b), 0, -1):
        if a % d == 0 and b % d == 0:
            return d

    return 1


# print(gcd_naive(0, 1))
# print(gcd_naive(24, 16))
# The following call would take too long
# print(gcd_naive(790933790547, 1849639579327))


def gcd_improved(a, b):
    assert a >= 0 and b >= 0 and a + b > 0

    while a > 0 and b > 0:
        if a >= b:
            a = a - b
        else:
            b = b - a

    return max(a, b)


# print(gcd_improved(24, 16))
# print(gcd_improved(790933790547, 1849639579327))
# The following call would take too long
# print(gcd_improved(790933790548, 2))


def gcd_euclids(a, b):
    assert a >= 0 and b >= 0 and a + b > 0

    while a > 0 and b > 0:
        if a >= b:
            a = a % b
        else:
            b = b % a

    return max(a, b)


# print("Euclid's GCD")
# print(gcd_euclids(24, 16))
# print(gcd_euclids(790933790547, 1849639579327))
# print(gcd_euclids(790933790548, 2))


def extended_gcd(a, b):
    assert a >= b and b >= 0 and a + b > 0

    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)

    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y
    return (d, x, y)


# print("Extended Euclid's")
# print(extended_gcd(10, 6))
# print(extended_gcd(7, 5))
# print(extended_gcd(391, 299))
# print(extended_gcd(239, 201))

# Quiz Tile a Rectangle with Squares
def squares(n, m):
    if n >= m:
        res = extended_gcd(n, m)
    else:
        res = extended_gcd(m, n)
    return (n * m) // (res[0] ** 2)


# print(squares(10, 6))
# print(squares(2, 2))

# Quiz: Least Common Multiple: Code
def lcm(a, b):
    assert a > 0 and b > 0

    # Write your code here
    if a > b:
        return (a * b) / extended_gcd(a, b)[0]
    else:
        return (a * b) / extended_gcd(b, a)[0]
