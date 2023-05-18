#!/usr/bin/python3
"""
Write a method that checks for valid utf-8 encoding
"""


def validUTF8(data):
    """
    determines if a given data set represents a valid UTF-8 encoding
    """
    subsequent_bytes = 0

    for num in data:
        # Check if the current byte is a continuation byte
        if subsequent_bytes:
            if num >> 6 != 0b10:
                return False
            subsequent_bytes -= 1
        else:
            # Check the number of bytes to follow based on the first byte
            mask = 0b10000000
            while mask & num:
                subsequent_bytes += 1
                mask >>= 1
            if not subsequent_bytes:
                continue
            if subsequent_bytes == 1 or subsequent_bytes > 4:
                return False

    # Check if there are any remaining bytes expected to follow
    return subsequent_bytes == 0
