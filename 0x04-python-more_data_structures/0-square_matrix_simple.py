#!/usr/bin/python3
def square_matrix_simple(matrix=[]):

    new_matrix = []
    for line in range(len(matrix)):
        temp = []
        for c in range(len(matrix[line])):
            temp.append(matrix[line][c] ** 2)
        new_matrix.append(temp)
    return (new_matrix)
