from sort.sort_utils import swap, less


def selection_sort(a_list: list):
    """
    performs inplace selection sort on a_list.
    The function searches for the smallest element in the list and moves it the the beginning of the list.
    Then it searches for the smallest element in the reminder of the list (excluding the first element)
    and moves it to the second position in the list and so on.
    complexity O(N^2) ...~1/2 N^2

    :param a_list: list to sort
    """
    list_length = len(a_list)
    for i in range(list_length):
        min_index = i
        for j in range(i, list_length):
            if less(a_list[j], a_list[min_index]):
                min_index = j
        swap(a_list, i, min_index)
