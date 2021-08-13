# Uses python3
import sys


def _merge(array, left_starts, left_ends, right_starts, right_ends):
    """Swaps values in array depending on order

    Starts with array[left] up to array[right] until array[end]
    """
    number_of_inversions = 0

    A = array[left_starts : left_ends + 1]
    B = array[right_starts : right_ends + 1]
    l, r = 0, 0

    i = left_starts
    while l < len(A) and r < len(B):
        if A[l] <= B[r]:
            array[i] = A[l]
            l += 1
        else:
            array[i] = B[r]
            number_of_inversions = number_of_inversions + (len(A) - l)
            r += 1
        i += 1
    if l < len(A):
        # add remaining of A
        for l in range(l, len(A)):
            array[i] = A[l]
            i += 1
    else:
        # add remaining of B
        for r in range(r, len(B)):
            array[i] = B[r]
            i += 1

    return number_of_inversions


def get_number_of_inversions(array: list, left: int = 0, right: int = None):
    """Sort array"""
    number_of_inversions = 0

    if right is None:
        right = len(array) - 1

    if right == left:
        return 0

    m = (right + left) // 2
    number_of_inversions += get_number_of_inversions(array, left, m)
    number_of_inversions += get_number_of_inversions(array, m + 1, right)
    number_of_inversions += _merge(array, left, m, m + 1, right)

    return number_of_inversions


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    b = n * [0]
    print(get_number_of_inversions(a))
