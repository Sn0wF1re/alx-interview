#!/usr/bin/python3
"""
Pascal triangle
"""
def pascal_triangle(n):
    """
    Creates a pascal triangle
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for row in range(1, n):
        newRow = [1]
        for col in range(1, row):
            newRow.append(triangle[row-1][col-1] + triangle[row-1][col])
        newRow.append(1)
        triangle.append(newRow)
    return triangle
