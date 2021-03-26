import math
import pprint


def get_change(m, coins: list = [1, 3, 4]):
    """minimum number coins with denominators 1, 3, 4 which changes m

    Args:
        m (int): money
        coins (List[int]): coin denominations

    Returns:
        int: minimum number of coins to reach m
    """
    min_num_coins = {0: 0}
    for m in range(1, m + 1):
        min_num_coins[m] = math.inf
        for coin in coins:
            if m >= coin:
                num_coins = min_num_coins[m - coin] + 1
                if num_coins < min_num_coins[m]:
                    min_num_coins[m] = num_coins

    return min_num_coins[m]


if __name__ == "__main__":
    print(get_change(int(input())))
