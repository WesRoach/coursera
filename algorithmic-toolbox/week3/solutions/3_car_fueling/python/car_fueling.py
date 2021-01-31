from typing import List


def compute_min_refills(distance: int, tank: int, stops: List[int]) -> int:
    """Calculates minimum number of stops required.

    Args:
        distance (int): total trip distance
        tank (int): max fuel range of car
        stops (List[int]): total trip distance of each stop on route

    Returns:
        int: minimum number refills
    """

    num_refills = 0
    current_refill = 0
    n_stops = len(stops)
    stops = [0, *stops, distance]
    while current_refill <= n_stops:
        last_refill = current_refill
        while (
            current_refill <= n_stops
            and stops[current_refill + 1] - stops[last_refill] <= tank
        ):
            current_refill += 1
        if current_refill == last_refill:
            return -1
        if current_refill <= n_stops:
            num_refills += 1
    return num_refills


if __name__ == "__main__":
    d = int(input())
    m = int(input())
    n = int(input())  # not need for python implementation
    stops = [x for x in map(int, input().split())]
    # print(f"d: {d}")
    # print(f"d: {m}")
    # print(f"stops: {stops}")
    print(compute_min_refills(d, m, stops))
