

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
