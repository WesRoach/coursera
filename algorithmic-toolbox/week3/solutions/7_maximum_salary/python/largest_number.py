from typing import List
from functools import cmp_to_key


def compare(s1: str, s2: str) -> int:
    """Compares two strings character by character. Strings of different
    length but otherwise matching on equal indices use each string's
    str[-1] character to determine which is smaller.

    Examples:
        >>> compare("1", "2")
        -1

        >>> compare("55", "55")
        0

        >>> compare("55", "556")
        -1

        >>> compare("55", "554")
        1

    Args:
        s1 (str): first string
        s2 (str): second string

    Returns:
        int: indicates which string is smaller (ascending)
            -1: first string is smaller
             1: second string is smaller
             0: matching
    """
    s1_len, s2_len = len(s1), len(s2)
    max_len = max(s1_len, s2_len)
    min_len = min(s1_len, s2_len)
    for i in range(0, max_len):
        if i == min_len:
            if i == s1_len and s2_len > s1_len:
                if s1[i - 1] < s2[i]:
                    return -1
                elif s1[i - 1] > s2[i]:
                    return 1
                else:
                    return 0
            elif i == s2_len and s1_len > s2_len:
                if s1[i] > s2[i - 1]:
                    return 1
                elif s1[i] < s2[i - 1]:
                    return -1
                else:
                    return 0

        if s1[i] < s2[i]:
            return -1
        elif s1[i] > s2[i]:
            return 1

    return 0


def largest_number(a: List[str]) -> str:
    """Compose the largest number out of a set of integers.

    Args:
        a (List[str]): list of integers

    Returns:
        str: largest number that can be composed of `a`
    """
    return "".join(sorted(a, reverse=True, key=cmp_to_key(compare)))


if __name__ == "__main__":
    _ = input()
    print(largest_number(input().split()))
