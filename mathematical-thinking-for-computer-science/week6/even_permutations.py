# def is_permutation(p):
#     return set(p) == set(range(len(p)))


# print(is_permutation([0]))
# print(is_permutation([0, 2, 1]))
# print(is_permutation([1, 2, 3]))


def selection_sort(arr: list):
    if len(arr) == 1:
        return 0, arr

    swaps = 0
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[min_idx], arr[i] = arr[i], arr[min_idx]
        swaps += 1
        print(f"Swap {swaps}: {arr}")

    return swaps, arr


def is_even(arr: list):
    if selection_sort(arr)[0] % 2 != 0:
        return False
    else:
        return True


print(selection_sort([3, 2, 1]))
print(selection_sort([0, 3, 2, 4, 5, 6, 7, 1, 9, 8]))
# print(selection_sort([3, 2, 1]), is_even([3, 2, 1]))
# print(
#     selection_sort([0, 3, 2, 4, 5, 6, 7, 1, 9, 8]),
#     is_even([0, 3, 2, 4, 5, 6, 7, 1, 9, 8]),
# )
