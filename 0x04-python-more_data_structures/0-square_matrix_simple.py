#!/usr/bin/python3

# simply return [[x**2 for x in row] for row in matrix]
# or simplly return [list(map(lambda x: x**2, row)) for row in matrix]

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_matrix.append(list(map(lambda x: x**2, row)))
    return new_matrix
