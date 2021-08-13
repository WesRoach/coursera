def optimal_summands(n: int) -> list:
    """Calculate the maximum distinct number of prizes which could be
    awarded per prize.

    Args:
        n (int): total number of prizes

    Returns:
        list: number of prizes per reward
    """
    if n == 1:
        return [1]

    summands = [1]
    _sum = 1
    for i in range(2, n + 1):
        if _sum + i <= n:
            summands.append(i)
            _sum += i
        else:
            _sum -= summands.pop()
            if _sum + i <= n:
                summands.append(i)
                _sum += i
        # print(f"i: {i}, _sum: {_sum}, summands: {summands}")

        if _sum == n:
            break

    return summands


if __name__ == "__main__":
    summands = optimal_summands(int(input()))
    print(len(summands))
    for x in summands:
        print(x, end=" ")
