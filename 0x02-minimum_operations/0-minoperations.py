#!/usr/bin/env python3
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
    pasted = 1
    copied = 0
    count = 0

    while pasted < n:
        if copied == 0:
            # copy from pasted
            copied = pasted
            count += 1

        if pasted == 1:
            # paste from copied
            pasted += copied
            count += 1
            # continue with loop
            continue

        # check for remainder
        rem = n - pasted

        # check whether copied has more than needed
        if rem < copied:
            return 0

        if rem % pasted == 0:
            # copy and paste then increment counter by 2
            copied = pasted
            pasted += copied
            count += 2
        else:
            # paste from what's already copied
            pasted += copied
            count += 1

    return count if pasted == n else 0
