def get_fibonacci_last_digit_fast(n: int):
    if n <= 1:
        return n
    prev, current = 0, 1
    for i in range(1, n):
        current, prev = (current + prev) % 10, current

    return current


n = int(input())
print(get_fibonacci_last_digit_fast(n))
