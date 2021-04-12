from typing import List
from pprint import pprint


def optimal_weight(knapsack_weight: int, items: List[int]):
    """Maximum weight of gold that fits into knapsack.

    Args:
        knapsack_weight (int): capacity of knapsack
        items (List[int]): weight of gold bars

    Returns:
        int: maximum weight of given gold bars which fit into knapsack
    """
    # create 2-dimensional array of size W x len(w) filled w/0
    value = [
        [0 for x in range(0, knapsack_weight + 1)] for y in range(0, len(items) + 1)
    ]

    for i in range(1, len(items) + 1):
        for w in range(1, knapsack_weight + 1):
            value[i][w] = value[i - 1][w]
            if items[i - 1] <= w:
                val = value[i - 1][w - items[i - 1]] + items[i - 1]
                if value[i][w] < val:
                    value[i][w] = val

    return value[len(items)][knapsack_weight]


if __name__ == "__main__":
    W, _ = map(int, input().split())
    w = list(map(int, input().split()))
    print(optimal_weight(W, w))
