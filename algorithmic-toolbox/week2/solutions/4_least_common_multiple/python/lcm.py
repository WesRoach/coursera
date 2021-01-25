def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def lcm_naive(a, b):
    for l in range(1, a * b + 1):
        if l % a == 0 and l % b == 0:
            return l

    return a * b


def lcm_fast(a, b):
    return (a * b) // gcd(a, b)


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(lcm_fast(a, b))
