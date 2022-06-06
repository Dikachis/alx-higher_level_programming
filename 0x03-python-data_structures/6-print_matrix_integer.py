#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    matrix = [[input[i:i+4] for i in range(0, len(input), 4)]]
    for idx in matrix:
        print(" ".join("{:d}".format(idx)))
