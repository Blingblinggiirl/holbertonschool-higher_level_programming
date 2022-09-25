#!/usr/bin/python3
"""
        matrix
"""


def matrix_divided(matrix, div):
    """matrix dividir"""
    matrix_len = len(matrix[0])
    for row in matrix:
        if matrix_len =! len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for x in row:
            if not isinstance(x, int):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            return None
       if not isinstance(matrix, list) or not matrix[0]:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if (not isinstance(div, int) and (not isinstance(div, float))):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero") 
    matriz_dividida= matrix.copy()
    matriz_dividida = [list(map(lambda x: round(x / div, 2), roow)) for roow in matrix]
    return matriz_dividida
