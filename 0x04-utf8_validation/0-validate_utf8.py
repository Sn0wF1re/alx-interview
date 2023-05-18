#!/usr/bin/python3
"""
Write a method that checks for valid utf-8 encoding
"""


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding
    """
    byte_count = 0

    for num in data:
        if byte_count > 0:
            if num >> 6 == 2:
                byte_count -= 1
            else:
                return False

        else:
            mask = 1 << 7
            while mask & num:
                byte_count += 1
                mask >>= 1
            if byte_count > 4 or byte_count == 1:
                return False

    return byte_count == 0
