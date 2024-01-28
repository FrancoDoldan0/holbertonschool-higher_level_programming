#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for columna in matrix:
        for fila in columna:
            print("{:d} ".format(fila), end="")
        print()
