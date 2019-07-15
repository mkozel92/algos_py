def pivot(simplex_matrix: list, pivot_row: int, pivot_column: int):
    """
    perform pivot operation
    1. divide pivot row by value of coefficient in pivot column and pivot row.
       variable on this place will then have coefficient 1
    2. express this variable by moving all other variables to the right side of equation
       represented by pivot row and substitute this variable to other rows.
       -> this will zero out pivot column and rescales other coefficients
    :param simplex_matrix: simplex matrix
    :param pivot_row: pivot raw
    :param pivot_column: pivot column
    """
    rows = len(simplex_matrix)
    cols = len(simplex_matrix[0])
    # scale all entries
    for i in range(rows):
        for j in range(cols):
            if i != pivot_row and j != pivot_column:
                simplex_matrix[i][j] -= simplex_matrix[pivot_row][j] * \
                                        simplex_matrix[i][pivot_column] / \
                                        simplex_matrix[pivot_row][pivot_column]

    # zero out pivot column
    for i in range(rows):
        if i != pivot_row:
            simplex_matrix[i][pivot_column] = 0.0

    # scale pivot row
    for j in range(cols):
        if j != pivot_column:
            simplex_matrix[pivot_row][j] /= simplex_matrix[pivot_row][pivot_column]
    simplex_matrix[pivot_row][pivot_column] = 1


def min_ratio_row(simplex_matrix: list, pivot_column: int) -> int:
    """
    find a row with min ration of right_side_value and pivot column coefficient
    :param simplex_matrix: simplex matrix
    :param pivot_column: pivot column computed by bland rule
    :return: index of a row with min ratio
    """
    rows = len(simplex_matrix)
    cols = len(simplex_matrix[0])
    min_ratio = -1
    min_ratio_index = 0
    for i in range(rows - 1):
        if simplex_matrix[i][pivot_column] <= 0:
            continue
        ratio = simplex_matrix[i][cols - 1] / simplex_matrix[i][pivot_column]
        if min_ratio == -1 or ratio < min_ratio:
            min_ratio = ratio
            min_ratio_index = i
    return min_ratio_index


def bland(simplex_matrix: list) -> int:
    """
    Find columns where objective function coefficient is positive and return this column
    pivoting on such columns will increase value of objective function
    :param simplex_matrix: simplex matrix
    :return: column to pivot on or -1 if the matrix is optimal
    """
    rows = len(simplex_matrix)
    cols = len(simplex_matrix[0])
    for i in range(cols):
        if simplex_matrix[rows - 1][i] > 0:
            return i
    return -1


def solve_simplex(simplex_matrix: list):
    """
    use simplex algo to solve linear programming problem
    :param simplex_matrix: matrix representing given problem
    example:
    maximize 13A + 23B
    under constraints that
    5A + 15B <= 480
    4A + 4B <= 160
    35A + 23B <= 1190
    can be expressed as:
    simplex_matrix = [[5, 15, 1, 0, 0, 480],
                     [4,  4,  0, 1, 0, 160],
                     [35, 20, 0, 0, 1, 1190],
                     [13, 23, 0, 0, 0, 0]]

    results in:
    [0.0, 0.0, 1.5, -10.625, 1, 210]
    [0.0, 1.0, 0.1, -0.125, 0.0, 28.0] -> B = 28
    [1.0, 0.0, -0.1, 0.375, 0.0, 12] -> A = 12
    [0.0, 0.0, -1.0, -2.0, 0.0, -800.0] -> objective 800

    """
    while True:
        pivot_column = bland(simplex_matrix)
        if pivot_column == -1:
            break
        pivot_row = min_ratio_row(simplex_matrix, pivot_column)
        pivot(simplex_matrix, pivot_row, pivot_column)
