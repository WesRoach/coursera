def get_majority_element(a: list) -> int:
    """Returns 1 if list contains a majority element, otherwise: 0"""
    count = dict()
    for value in a:
        if value not in count:
            count[value] = 0
        count[value] = count[value] + 1

    # sorted() returns [(value, cnt), (value, cnt), (), ...]
    # with the most frequenctly counted value in the first position
    # [0][1] returns the count of the most frequency value
    max_count = sorted(count.items(), key=lambda x: x[1], reverse=True)[0][1]
    if max_count > (len(a) / 2):
        return 1
    return 0


if __name__ == "__main__":
    _ = input()
    a = list(map(int, input().split()))
    print(get_majority_element(a))
