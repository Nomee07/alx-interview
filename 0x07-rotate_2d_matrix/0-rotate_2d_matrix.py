#!/usr/bin/python3
"""
Rotate 2D Matrix
"""


def rotate_2d_matrix(matrix):
    """
    Rotate a 2D matrix 90 degrees clockwise.

    Args:
        matrix (list[list[int]]): The input 2D matrix to rotate.

    Returns:
        None: The matrix is edited in-place.

    Assumptions:
        - The input matrix will have 2 dimensions.
        - The input matrix will not be empty.
    """
    n = len(matrix)

    # Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to rotate clockwise
    for row in matrix:
        row.reverse()


if __name__ == "__main__":
    # Test the rotate_2d_matrix function
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    rotate_2d_matrix(matrix)
    print(matrix)
