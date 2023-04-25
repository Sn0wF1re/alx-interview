#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened
    Return True if possible, False otherwise
    """
    if not boxes or not isinstance(boxes, list):
        return False

    keys = [0]
    length = len(boxes)

    for i in keys:
        for k in boxes[i]:
            if k not in keys and k < length:
                keys.append(k)
    return len(keys) == length
