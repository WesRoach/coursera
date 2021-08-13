import itertools
from typing import List


def partition3(A: List[int]) -> int:
    """Determine if possible to partition A into three equal sums.

    Args:
        A (List[int]): list of ints

    Returns:
        int: 1: True; 0: False
    """
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0


def partition3_brute(A: List[int]) -> int:
    """Determine if possible to partition A into three equal sums.

    Args:
        A (List[int]): list of ints

    Returns:
        int: 1: True; 0: False
    """
    for c in itertools.product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0


if __name__ == "__main__":
    n = input()
    A = list(map(int, input().split()))
    print(partition3(A))
