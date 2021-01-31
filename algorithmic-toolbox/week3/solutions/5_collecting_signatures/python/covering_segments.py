from typing import List
from collections import namedtuple

Segment = namedtuple("Segment", "start end")


def optimal_points(segments: List[Segment]) -> list:
    points = []

    # Sort segments ascending by start of segment
    segments = sorted(segments, key=lambda x: x.start)
    for idx, segment in enumerate(segments):
        if idx == 0:
            prev = segment
            point = segment.end
        elif segment.start <= prev.end:
            point = min(point, segment.end)
            if point < segment.start:
                points.append(point)
                point = segment.end
            prev = segment
        elif segment.start > prev.end:
            points.append(point)
            point = segment.end
            prev = segment
    points.append(point)

    return points


if __name__ == "__main__":
    n = int(input())
    data = []
    for _ in range(0, n):
        data.append([*map(int, input().split())])
    segments = [Segment(x, y) for x, y in data]
    points = optimal_points(segments)
    # print(f"n: {n}")
    # print(f"data: {data}")
    # print(f"segments: {segments}")
    print(len(points))
    print(*points)
