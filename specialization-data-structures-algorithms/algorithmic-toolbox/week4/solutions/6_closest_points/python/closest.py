from typing import Union, List, Tuple
import math


def euclidean_distance(a: Tuple[int, int], b: Tuple[int, int]) -> float:
    """Caluclates Euclidean distance between two points.

    Args:
        a (List[int, int]): x, y coordinates of first point
        b (List[int, int]): x, y coordinates of second point

    Returns:
        float: Euclidean distance between point a & b
    """
    return math.sqrt(((a[0] - b[0]) ** 2) + ((a[1] - b[1]) ** 2))


def _min_distance(coordinates: List[Tuple[int, int]], left: int, right: int) -> float:
    # if 3 or less points - just use brute force approach
    if right - left + 1 <= 3:
        i = left
        min_distance = math.inf
        while i < right:
            j = i + 1
            while j <= right:
                dist = euclidean_distance(coordinates[i], coordinates[j])
                if dist < min_distance:
                    min_distance = dist
                j += 1
            i += 1
        return min_distance
    m = (right + left) // 2
    l_min_distance = _min_distance(coordinates, left, m)
    r_min_distance = _min_distance(coordinates, m + 1, right)
    d = min(l_min_distance, r_min_distance)

    # l_x_coord bisects the point sets into left and right
    #       .       |       .
    #       .   .   |   .       .
    # N coordinates on left <== l ==> N coordinates on right
    l_x_coord = (coordinates[m][0] + coordinates[m + 1][0]) / 2

    # filter to coordinates with an `x-distance to l` < d
    x_less_d = [
        coord
        for coord in coordinates[left : right + 1]
        if abs(coord[0] - l_x_coord) <= d
    ]
    x_less_d.sort(key=lambda x: x[1])

    # compute min distance between each point in x_less_d and 7 next points
    d_prime = math.inf
    i = 0
    while i < len(x_less_d):
        j = i + 1
        while j <= len(x_less_d) - 1 and (j - i) <= 8:
            dist = euclidean_distance(x_less_d[i], x_less_d[j])
            if dist < d_prime:
                d_prime = dist
            j += 1
        i += 1

    return min(d, d_prime)


def minimum_distance(coordinates: List[Tuple[int, int]]) -> float:
    """Computes the minimum distance between any point.

    Improvements could be made by being more considerate with sorting.
    - Consider sorting in place
    - Consdier pre-sorting y-axis rather than sorting on each d&c

    Args:
        coordinates (List[Tuple[int, int]]): list of (x, y) coordinates.

    Returns:
        float: minimum distance between any two points in coordinates
    """

    # sort coordinates by their x position
    # d&c: split into n/2 halves by x-coordinate
    # d&c until returning the min distance b/t coordinates
    x_sorted_coords = sorted(coordinates, key=lambda coord: coord[0])
    # y_sorted_coords = sorted(coordinates, key=lambda coord: coord[1])

    smallest_x_distance = _min_distance(x_sorted_coords, 0, len(coordinates) - 1)

    return smallest_x_distance


def brute_minimum_distance(coordinates: List[Tuple[int, int]]) -> float:

    min_dist = math.inf
    for i in range(0, len(coordinates) - 1):
        for j in range(i + 1, len(coordinates)):
            dist = euclidean_distance(coordinates[i], coordinates[j])
            if dist < min_dist:
                min_dist = dist
    return min_dist


if __name__ == "__main__":
    n = int(input())
    coordinates = []
    for coordinate in range(0, n):
        coordinates.append(list(map(int, input().split())))

    # x = [x for x, y in coordinates]
    # y = [y for x, y in coordinates]
    print("{0:.9f}".format(minimum_distance(coordinates)))


# import pdb
# from closest import minimum_distance, euclidean_distance, _min_distance
# pdb.run('minimum_distance([(7, 7), (1, 100), (4, 8), (7, 7)])')
# pdb.run('_min_distance([(0, 0), (3, 4)], 0, 1)')
