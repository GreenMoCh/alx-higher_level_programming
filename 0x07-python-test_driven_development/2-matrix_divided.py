#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divide all elements  of a matrix by a number

    Args:
        matrix: the matrix to be divided
        div: the divisor

    Returns:
        list of lists: new matrix with all elements divided by div

    Raises:
        TypeError: if the matrix is not a list of lists of ints or floats, or div is not a number
        ZeroDivisionError: if the div is 0
        TypeError: If each row of the matrix does not have the same size
    """
    if not all(isinstance(row, list) and all(isinstance(num, (int, float)) for num in row) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if len(set(len(row) for row in matrix)) != 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise typeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = [round(num / div, 2) for num in row]
        new_matrix.append(new_row)

    return (new_matrix)
