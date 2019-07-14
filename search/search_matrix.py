from multiprocessing import Pool

from search.binary_search import binary_search


def search_matrix(to_search: int, a_matrix: list) -> (int, int):
    """
    search for element in sorted matrix
    complexity O(MN)
    :param to_search: element to search
    :param a_matrix: matrix to search in
    :return: indices of element
    """
    row = 0
    column = len(a_matrix[0]) - 1
    while row < len(a_matrix) and column >= 0:
        if to_search < a_matrix[row][column]:
            column -= 1
        elif to_search > a_matrix[row][column]:
            row += 1
        else:
            return row, column
    return -1, -1


def search_matrix_parallel(to_search: int, a_matrix) -> (int, int):
    """
    parallel search in sorted matrix
    complexity O(M + log N)
    :param a_matrix: matrix to search
    :param to_search: element to search
    :return: index of searched element
    """
    pool_size = len(a_matrix)

    with Pool(pool_size) as p:
        res = p.starmap(binary_search, [(a_matrix[i], to_search) for i in range(len(a_matrix))])

    for i, r in enumerate(res):
        if r != -1:
            return i, r

    return -1, -1

