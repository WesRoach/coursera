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


def fibonacci_partial_sum(start: int, end: int):
    pisano_period = fib_pisano_period(10)
    if start == end:
        return pisano_period[start % 60]

    start_fib = fibonacci_sum(start - 1)
    end_fib = fibonacci_sum(end)
    return (end_fib - start_fib) % 10


if __name__ == "__main__":
    start, end = map(int, input().split())
    print(fibonacci_partial_sum(start, end))
