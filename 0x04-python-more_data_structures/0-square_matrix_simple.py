#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """Computes the square value of a matrix

    Args:
        matrix: Matrix for computation

    Returns:
        A list of square'd matrix
    """

    square = [[0] * len(matrix[0]) for i in range(len(matrix))]
    for i in range(len(matrix)):
        square[i] = list(map(lambda x: x ** 2, matrix[i]))

    return square
