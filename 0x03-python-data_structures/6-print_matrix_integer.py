#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ligne in range(len(matrix)):
        for colonne in range(len(matrix[ligne])):
            print("{:d}".format(matrix[ligne][colonne]), end="")
            if colonne < (len(matrix[ligne]) - 1):
                print(" ", end="")
        print()
