#!/usr/bin/python3
"""
Create function rotate_2d_matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise
    """
    length = len(matrix)
    for i in range(length):
        j = 0
        while j < i:
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            j += 1

    for i in range(length):
        matrix[i] = matrix[i][::-1]
