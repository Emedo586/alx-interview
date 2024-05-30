#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise.
    """
    n = len(matrix)
    for i in range(int(n / 2)):
        # Outer loop iterates through the row of matrix upto half its length
        for j in range(i, (n - i - 1)):
            # Inner loop iterates through the column within the current row
            x = (n - 1 - j)
            # Retrive elements in current group and swap them.
            p = matrix[i][j]
            matrix[i][j] = matrix[x][i]
            matrix[x][i] = matrix[(n - i - 1)][x]
            matrix[(n - i - 1)][x] = matrix[j][(n - i - 1)]
            matrix[j][(n - i - 1)] = p
