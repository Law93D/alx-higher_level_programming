#!/usr//bin/python3
def square_matrix_simple(matrix=[]):
    sq_matrix = []
    for row in matrix:
        sq_row = []

        for num in row:
            sq_num = num ** 2
            sq_row.append(sq_num)
        sq_matrix.append(sq_row)
    return sq_matrix
