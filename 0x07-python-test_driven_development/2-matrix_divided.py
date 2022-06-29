#!/usr/bin/python3
"""
    2-matrix_divided Module
"""


def matrix_divided(matrix, div):
    """
        Divides all elements of a matrix

        Args:
            matrix: intial 2D list
            div: integer which is the divisor

        Returns:
            New matrix containing the divided elements
            rounded to 2 decimal places
    """
    prev_len = 0
    error_mess = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(error_mess)

    for block in matrix:    # matrix is a list
        if type(block) is not list:
            raise TypeError(error_mess)

        for element in block:
            if type(element) is not int and type(element) is not float:
                raise TypeError(error_mess)

        if len(block) != prev_len and prev_len != 0:
            raise TypeError("Each row of the matrix must have the same size")
        prev_len = len(block)

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
