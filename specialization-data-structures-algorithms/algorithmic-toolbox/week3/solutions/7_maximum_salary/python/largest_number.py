from typing import List
from functools import cmp_to_key


def compare(s1: str, s2: str) -> int:
    """Returns orientation of strings producing a smaller integer.

    Args:
        s1 (str): first string
        s2 (str): second string

    Returns:
        int: one of: (-1, 0, 1)
            -1: s1 first produces smaller int
             0: No difference
             1: s2 first produces smaller int
    """
    s1_first = int(s1 + s2)
    s2_first = int(s2 + s1)
    if s1_first > s2_first:
        return 1
    elif s2_first > s1_first:
        return -1
    else:
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
