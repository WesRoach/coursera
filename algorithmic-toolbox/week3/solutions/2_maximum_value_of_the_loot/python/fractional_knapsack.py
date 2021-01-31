# Uses python3
from typing import List


def get_optimal_value(capacity: int, weights: List[int], values: List[int]) -> float:
    """Returns highest value for a fixed weight of items.

    Args:
        capacity (int): max weight knapsack can hold
        weights (List[int]): weights of potential items
        values (List[int]): values of potential items

    Returns:
        float: maximum value of items in knapsack
    """

    value = 0.0
    sorted_value_weight_ratio = sorted(
        [
            (value / weight, idx)
            for (idx, (value, weight)) in enumerate(zip(values, weights))
        ],
        reverse=True,
    )
    # print(f"sorted_value_weight_ratio: {sorted_value_weight_ratio}")

    for value_weight_ratio, idx in sorted_value_weight_ratio:
        # item = (value: float, idx: int)
        if capacity > 0:
            item_weight = weights[idx]
            usable_capacity = min(item_weight, capacity)
            value += usable_capacity * value_weight_ratio
            capacity -= usable_capacity
            # print(f"item_weight: {item_weight}")
            # print(f"usable_capacity: {usable_capacity}")
            # print(f"value: {value}")
            # print(f"capacity: {capacity}")

    return value


if __name__ == "__main__":
    n, capacity = map(int, input().split())
    weights = []
    values = []
    for _ in range(0, n):
        value, weight = map(int, input().split())
        weights.append(weight)
        values.append(value)
    # print(f"n: {n}")
    # print(f"capacity: {capacity}")
    # print(f"weights: {weights}")
    # print(f"values: {values}")
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
