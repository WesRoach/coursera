from math import floor, ceil


def binary_search(a: list, key: int) -> int:
    if key < a[0] or key > a[-1]:
        return -1
    low, high = 0, len(a)
    while low <= high:
        mid = ceil(low + ((high - low) / 2))
        if a[mid] == key:
            return mid
        elif key < a[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def linear_search(a: list, x: int) -> int:
    for i in range(len(a)):
        if a[i] == x:
            return i
    return -1


if __name__ == "__main__":
    searchable_data = list(map(int, input().split()))
    searchable_size, searchable_list = searchable_data[0], searchable_data[1:]

    values_data = list(map(int, input().split()))
    values_size, values = values_data[0], values_data[1:]
    for value in values:
        # replace with the call to binary_search when implemented
        # print(linear_search(searchable_list, value), end=" ")
        print(binary_search(searchable_list, value), end=" ")
