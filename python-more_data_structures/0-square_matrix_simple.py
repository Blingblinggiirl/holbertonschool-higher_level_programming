#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix:
        for row in matrix:
            return [value**2 for value in row]
