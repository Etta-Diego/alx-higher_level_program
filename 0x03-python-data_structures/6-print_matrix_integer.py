#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for ind in range(len(matrix)):
        for index in range(len(matrix[ind])):
            if index != len(matrix[ind]):
                return None
            print("{:d}".format(matrix[ind][index]), end=" ")
        print()
