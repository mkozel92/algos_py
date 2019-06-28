from copy import deepcopy


def rotate_matrix(a_matrix: list):
    """
    rotate given matrix by 90 degrees
    complexity O(N)
    :param a_matrix: matrix to rotate
    :return: rotated matrix
    """
    rotated_matrix = deepcopy(a_matrix)

    for i in range(len(a_matrix)):
        for j in range(len(a_matrix[0])):
            rotated_matrix[len(a_matrix) - j - 1][i] = a_matrix[i][j]
    return rotated_matrix


def rotate_in_place(a_matrix: list):
    """
    rotate matrix by 90 degrees in place
    :param a_matrix: matrix to rotate
    """
    length = len(a_matrix)
    for i in range(length // 2):
        first = i
        last = length - 1 - i
        for j in range(first, last):

            offset = j - first
            top = a_matrix[first][j]
            a_matrix[first][j] = a_matrix[last - offset][first]
            a_matrix[last - offset][first] = a_matrix[last][last - offset]
            a_matrix[last][last - offset] = a_matrix[j][last]
            a_matrix[j][last] = top
