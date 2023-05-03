#!/usr/bin/python3
"""
Write a method that calculates the fewest number of operations needed
to result in exactly n H characters in the file.
"""


def minOperations(n: int) -> int:
    """
    Calculates fewest no. of operations needed to result
    in exactly n H characters in the file
    Args:
        n: number of characters in the file
    Returns:
        0 if impossible, number of times if successful
    """
    if n < 1:
        return 0

    pasted = 1
    copied = 1
    count = 0

    while pasted < n:
        if n % pasted == 0:
            # copy from pasted then paste
            copied = pasted
            pasted += copied
            count += 2
        else:
            # paste from what is already copied
            pasted += copied
            count += 1

    return count if pasted == n else 0
