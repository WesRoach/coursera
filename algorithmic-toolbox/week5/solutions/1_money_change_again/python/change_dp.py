def get_change(m):
    """minimum number coins with denominators 1, 3, 4 which changes m

    Args:
        m (int): money

    Returns:
        int: minimum number of coins to reach m
    """
    # write your code here
    return m // 4


if __name__ == "__main__":
    print(get_change(int(input())))
