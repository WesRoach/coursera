def fibonacci_sum_squares(n):
    if n <= 1:
        return n

    r = n % 60  # 60 is the Pisano Period for modulo m=10
    previous = 0
    current = 1

    for i in range(r):
        previous, current = current, (previous + current) % 10

    return (previous * current) % 10


if __name__ == "__main__":
    n = int(input())
    print(fibonacci_sum_squares(n))
