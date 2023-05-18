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
        binary = bin(num)[2:].zfill(8)
        if subsequent_bytes == 0:
            if binary.startswith('0'):
                continue
            elif binary.startswith('110'):
                subsequent_bytes = 1
            elif binary.startswith('1110'):
                subsequent_bytes = 2
            elif binary.startswith('11110'):
                subsequent_bytes = 3
            else:
                return False

        else:
            if not binary.startswith('10'):
                return False
            subsequent_bytes -= 1
        if subsequent_bytes < 0:
            return False

    return subsequent_bytes == 0
