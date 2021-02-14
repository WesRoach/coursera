from typing import List, Tuple


def fast_count_segments(segments: List[Tuple[int, int]], points: List[int]):
    starts = sorted([x for x, y in segments])
    ends = sorted([y + 1 for x, y in segments])
    s = e = 0

    # can't assume points are sorted
    # capture original index of point
    points = sorted(
        [(idx, point) for idx, point in enumerate(points)], key=lambda x: x[1]
    )

    segment_count = 0
    point_counts = []

    for orig_idx, point in points:
        while s < len(starts) and starts[s] <= point:
            segment_count += 1
            s += 1
        while e < len(ends) and ends[e] <= point:
            segment_count += -1
            e += 1
        point_counts.append((orig_idx, segment_count))

    return [cnt for idx, cnt in sorted(point_counts, key=lambda x: x[0])]


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt


if __name__ == "__main__":
    n_segments, n_points = tuple(map(int, input().split()))

    segments = []
    for segment in range(0, n_segments):
        segments.append(tuple(map(int, input().split())))

    starts = [x for x, y in segments]
    ends = [y for x, y in segments]

    points = list(map(int, input().split()))

    # cnt = naive_count_segments(starts, ends, points)
    for x in fast_count_segments(segments, points):
        print(x, end=" ")
