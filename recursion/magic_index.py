

def magic_index(a_list: list, from_index: int, to_index: int) -> int:
    """
    return index such that index == a_list[index] in
    sorted array of distinct elements
    :param a_list: list ot search
    :param from_index: search from this index
    :param to_index: search to this index
    :return: magic index
    """
    if from_index > to_index:
        return -1

    mid = (from_index + to_index) // 2

    if a_list[mid] < mid:
        return magic_index(a_list, mid + 1, to_index)
    elif a_list[mid] > mid:
        return magic_index(a_list, from_index, mid - 1)
    else:
        return mid

