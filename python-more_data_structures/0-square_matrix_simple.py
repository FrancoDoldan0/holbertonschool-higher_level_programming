def square_matrix_simple(matrix=[]):

    newlist = [list(map(lambda x: x**2, row)) for row in matrix]
    return (newlist)