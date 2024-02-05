#!/usr/bin/python3
def matrix_divided(matrix, div):
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list):
        raise TypeError(error)

    if all(not isinstance(row, list) for row in matrix):
        raise TypeError(error)

    row_length = len(matrix[0])  # Obtener la longitud de la primera fila
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    newmat = len(matrix)

    matrix1 = []
    for row in matrix:
        new_row = [round(element / div, 2) for element in row]
        matrix1.append(new_row)

    return matrix1
