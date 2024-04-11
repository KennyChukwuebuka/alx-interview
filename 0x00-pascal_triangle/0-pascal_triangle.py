#!/usr/bin/python3
"""create a function def pascal_triangle(n): that returns a list of lists
of integers representing the Pascal’s triangle of n:
Returns an empty list if n <= 0
You can assume that n is always an integer
"""


def pascal_triangle(n):
    """create a function def pascal_triangle(n): that returns a list of lists
    of integers representing the Pascal’s triangle of n:
    Returns an empty list if n <= 0
    You can assume that n is always an integer
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle
