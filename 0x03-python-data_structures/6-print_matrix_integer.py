#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
        return
    for ind in matrix:
        for index in range(len(ind)):
            if index == len(ind) - 1:
                print("{}".format(ind[index]), end="")
            else:
                print("{}".format(ind[index]), end=" ")
        print()
