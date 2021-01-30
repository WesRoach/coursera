from typing import List


def max_dot_product(a: List[int], b: List[int]) -> int:
    a = sorted(a, reverse=True)
    b = sorted(b, reverse=True)

    return sum([x[0] * x[1] for x in zip(a, b)])


if __name__ == "__main__":
    _ = input()
    a = [*map(int, input().split())]
    b = [*map(int, input().split())]
    print(max_dot_product(a, b))
