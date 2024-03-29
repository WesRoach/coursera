def extended_gcd(a, b):
    assert a >= 0 and b >= 0 and a + b > 0

    if b == 0:
        d, x, y = a, 1, 0
    else:
        (d, p, q) = extended_gcd(b, a % b)
        x = q
        y = p - q * (a // b)

    assert a % d == 0 and b % d == 0
    assert d == a * x + b * y
    return (d, x, y)


extended_gcd(9, 2)


def diophantine(a, b, c):
    if a >= b:
        gcd = extended_gcd(a, b)
    else:
        gcd = extended_gcd(b, a)
    
    div = c / gcd[0]
    assert c % gcd[0] == 0
    
    if a >= b:
        x = int(div * gcd[1])
        y = int(div * gcd[2])
    else:
        x = int(div * gcd[2])
        y = int(div * gcd[1])
    
    # return (x, y) such that a * x + b * y = c
    return (x, y)


diophantine(9, 2, 1)


def divide(a, b, n):
    gcd = extended_gcd(a, n)
    assert n > 1 and a > 0 and extended_gcd(a, n)[0] == 1
    
    (s, t) = diophantine(n, a, 1)
        
    # return the number x s.t. x = b / a (mod n) and 0 <= x <= n-1.
    return (b * t) % n


divide(7, 2, 9)

-8 % 9



(2 * 5) % 9

2 % 9

7 * 5 % 9

16 % 9
