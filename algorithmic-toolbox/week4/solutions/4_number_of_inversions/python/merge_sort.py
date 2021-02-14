def _merge(array, left_starts, left_ends, right_starts, right_ends):
    """Swaps values in array depending on order

    Starts with array[left] up to array[right] until array[end]
    """
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


def merge_sort(array: list, left: int = 0, right: int = None):
    """Sort array"""
    if right is None:
        right = len(array) - 1

    if right == left:
        return

    m = (right + left) // 2
    merge_sort(array, left, m)
    merge_sort(array, m + 1, right)
    _merge(array, left, m, m + 1, right)
