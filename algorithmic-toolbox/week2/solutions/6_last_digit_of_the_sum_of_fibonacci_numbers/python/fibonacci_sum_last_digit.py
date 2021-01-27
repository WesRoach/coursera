def fib_pisano_period(m):
    pisano_period = [0, 1]
    prev, current = 0, 1
    while True:
        current, prev = (current + prev) % m, current
        if current == 1 and prev == 0:
            return pisano_period[:-1]
        pisano_period.append(current)


def fibonacci_sum(n):
    pisano_period = fib_pisano_period(10)
    pisano_period_sum = sum(pisano_period)
    return ((pisano_period_sum * (n // 60)) + sum(pisano_period[: (n % 60) + 1])) % 10


if __name__ == "__main__":
    n = int(input())
    print(fibonacci_sum(n))
