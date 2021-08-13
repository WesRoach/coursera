# 1) Find Pisano Period Length of modulo m; pisano_length
# 2) r = n % pisano_length
# 3) F(r) % m


def get_fibonacci_period_length(m):
    """
    Given modulo `m`, return the Pisano Period length.

    The Pisano period is the sequence of remainers r returned from taking
    modulo m of Fibonacci(0)...Fibonacci(n).
    """
    assert m >= 2
    pisano_length = 0
    prev, current = 0, 1
    while True:
        current, prev = (current + prev) % m, current
        pisano_length += 1
        if current == 1 and prev == 0:
            return pisano_length


def fibonacci(n: int):
    if n <= 1:
        return n
    prev, current = 0, 1
    for i in range(1, n):
        current, prev = current + prev, current

    return current


def fibonacci_mod(n: int, m: int):
    if n <= 1:
        return n
    prev, current = 0, 1
    for i in range(1, n):
        current, prev = (current + prev) % m, current

    return current


def fibonacci_mod_m(n, m):
    pisano_length = get_fibonacci_period_length(m)
    remainder = n % pisano_length
    # return fibonacci(remainder)
    return fibonacci_mod(remainder, m)


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(fibonacci_mod_m(n, m))
