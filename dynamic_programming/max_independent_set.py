

def max_independent_set(a_list: list) -> int:
    """
    get subset of given elements such that it does not contain any consecutive elements
    and the sum of the subset is maximized
    complexity O(N)
    :param a_list: list of elements
    :return: sum of max independent subset
    """
    result = [0] * len(a_list)

    result[0] = a_list[0]
    result[1] = max(a_list[0], a_list[1])

    for i in range(2, len(a_list)):
        result[i] = max(a_list[i] + result[i - 2], result[i - 1])

    return result[-1]


def max_independent_set_recursive(a_list: list, i: int, mem: dict) -> int:
    """
    get subset of given elements such that it does not contain any consecutive elements
    and the sum of the subset is maximized
    complexity O(N)
    :param a_list: list of elements
    :param i: currently processed index
    :param mem: memoized results
    :return: sum of max independent subset
    """

    if i < 0:
        return 0

    if i in mem:
        return mem[i]

    mem[i] = max(max_independent_set_recursive(a_list, i - 2, mem) + a_list[i],
                 max_independent_set_recursive(a_list, i - 1, mem))

    return mem[i]
