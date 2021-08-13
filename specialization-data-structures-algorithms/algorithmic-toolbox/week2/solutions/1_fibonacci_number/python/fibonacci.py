def fibonacci(n: int):
    if n <= 1:
        return n
    prev, current = 0, 1
    for i in range(1, n):
        current, prev = current + prev, current

    return current


n = int(input())
print(fibonacci(n))
