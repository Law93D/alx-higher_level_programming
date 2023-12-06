#!/usr//bin/python3
def square_matrix_simple(matrix=[]):
    sq_matrix = matrix.copy()

    for num in range(len(matrix)):
        sq_matrix[num] = list(map(lambda x: x**2, matrix[num]))

    return sq_matrix
