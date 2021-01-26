def fibonacci_partial_sum(start: int, end: int):
    prev, current, _sum = 0, 1, 0
    for i in range(2, end + 1):
        current, prev = (current + prev) % 10, current
        if i >= start:
            _sum += current
    return _sum % 10


if __name__ == "__main__":
    start, end = map(int, input().split())
    print(fibonacci_partial_sum(start, end))
