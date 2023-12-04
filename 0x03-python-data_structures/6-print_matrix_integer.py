#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
        return
    for ind in range(len(matrix)):
        for index in range(len(matrix[ind])):
            print("{:d}".format(matrix[ind][index]), end=" ")
        print()
