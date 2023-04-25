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

    keys = set((0,))

    for i in range(len(boxes)):
        for k in boxes[i]:
            if k < len(boxes):
                keys.add(k)

    for x in range(len(boxes)):
        if x not in keys:
            return False
    return True
