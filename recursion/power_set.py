def power_set_recursive(a_list: list, index: int) -> list:
    """
    get power set
    complexity O(2^N)
    :param a_list: a list of elements
    :param index: currently processed index
    :return: all possible subsets
    """
    if index == len(a_list) - 1:
        return [{a_list[-1]}, {}]

    sub_sets = []
    for sub_set in power_set_recursive(a_list, index + 1):
        sub_sets.append({a_list[index]}.union(sub_set))
        sub_sets.append(sub_set)

    return sub_sets
