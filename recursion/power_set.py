def power_set_recursive(a_list: list, index: int) -> list:
    """
    get power set
    complexity O(2^N)
    :param a_list: a list of elements
    :param index: currently processed index
    :return: all possible subsets
    """
    if index == len(a_list) - 1:
        return [{a_list[-1]}, set([])]

    sub_sets = []
    for sub_set in power_set_recursive(a_list, index + 1):
        sub_sets.append({a_list[index]}.union(sub_set))
        sub_sets.append(sub_set)

    return sub_sets


def convert_to_set(i: int, a_list: list):
    """
    use integer as a binary mask to select from given list
    :param i: mask
    :param a_list: a list
    :return: set with selected list elements
    """
    result = set([])
    index = 0
    while i != 0 and index < len(a_list):
        if 1 & i:
            result.add(a_list[index])
        index += 1
        i >>= 1

    return result


def power_set(a_list: list):
    """
    iterative implementation of power set
    complexity O(2^n)
    :param a_list: a list to process
    :return: power set
    """
    count = 2**len(a_list)
    result = []
    for i in range(count):
        result.append(convert_to_set(i, a_list))

    return result
