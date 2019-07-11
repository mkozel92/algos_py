def search_rotated(a_list: list, element: int):
    """
    search element in sorted rotated array
    :param a_list: list to search
    :param element: element to search
    :return: index of the element
    """
    low = 0
    high = len(a_list) - 1

    while low <= high:
        mid = (low + high) // 2
        if a_list[mid] == element:
            return mid
        elif a_list[low] < a_list[mid] and a_list[low] <= element < a_list[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1


