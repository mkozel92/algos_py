from sort.sort_utils import swap, less


def insertion_sort(a_list: list, h: int = 1):
    """
    performs inplace insertion sort on a_list
    Goes through the whole list and moves each element to the left until its in the correct place.
    complexity 0(N^2) ...~1/4 N^2
    :param a_list: a_list to sort
    :param h length of exchanges
    """
    list_len = len(a_list)
    for i in range(list_len):
        j = i
        while j >= h and less(a_list[j], a_list[j-h]):
            swap(a_list, j, j-h)
            j -= h
