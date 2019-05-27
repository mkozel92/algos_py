from sort.insertion_sort import insertion_sort


def shell_sort(a_list: list, h_tuple: tuple = (13, 5, 1)):
    """
    performs inplace shell sort on the given array.
    This is done by calling many insertions sorts with decreasing exchange length
    which is efficient because complexity of insertion sort on partially sorted array is basically linear
    complexity O(N^(3/2)) in practise much faster
    :param a_list: a list to sort
    :param h_tuple: tuple of exchange lengths for insertion sort
    """
    for h in h_tuple:
        insertion_sort(a_list, h)

