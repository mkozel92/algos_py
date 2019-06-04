

def binary_search(a: list, to_search: int) -> int:
    """
    Binary search algo that looks for and element in a given sorted array
    complexity O(log N)

    :param a: a sorted list to search in
    :param to_search: element to search
    :return: index of the element in given array or -1 if the element is not present
    """
    hi = len(a) - 1
    low = 0
    while hi >= low:
        mid = (hi + low) // 2
        if a[mid] > to_search:
            hi = mid - 1
        elif a[mid] < to_search:
            low = mid + 1
        else:
            return mid
    return -1


def recursive_binary_search(a_list: list, to_search: int, from_: int, to_: int) -> int:
    """
    recursive implementation of binary search
    complexity O(log N)
    :param a_list: list to search
    :param to_search: element to search for
    :param from_: index to search from
    :param to_:  index to search to
    :return: index of the element of -1
    """

    if from_ > to_:
        return -1

    mid = from_ + (to_ - from_) // 2
    if a_list[mid] < to_search:
        return recursive_binary_search(a_list, to_search, mid + 1, to_)
    elif a_list[mid] > to_search:
        return recursive_binary_search(a_list, to_search, from_, mid - 1)
    else:
        return mid
