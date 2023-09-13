#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []

    for l in range(len(matrix)):
        temp = []
        for c in range(len(matrix[l])):
            temp.append(matrix[l][c] ** 2)
        new_matrix.append(temp)
    return (new_matrix)
