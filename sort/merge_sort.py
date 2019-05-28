from sort.sort_utils import less


def merge(a_list: list, aux_list: list, low: int, mid: int, hi: int):
    """
    merges two sorted sub-arrays to one sorted array
    :param a_list: a list to sort
    :param aux_list: aux_list used to store copy of the list
    :param low: index where the first sub-array starts
    :param mid: index separating the sub-arrays
    :param hi: index where the second sub-array ends
    """
    for k in range(low, hi + 1):
        aux_list[k] = a_list[k]

    i = low
    j = mid + 1
    k = low

    while k <= hi:
        if i > mid or (j <= hi and less(aux_list[j], aux_list[i])):
            a_list[k] = aux_list[j]
            j += 1
        elif j > hi or (i <= mid and not less(aux_list[j], aux_list[i])):
            a_list[k] = aux_list[i]
            i += 1
        k += 1


def recursive_sort(a_list: list, aux_list: list, low: int, hi: int):
    """
    recursive function for merge sort
    :param a_list: pointer to array to sort
    :param aux_list: pointer to aux_array
    :param low: index from which to sort
    :param hi: index to which to sort
    """
    if hi <= low:
        return

    mid = (low + hi) // 2
    recursive_sort(a_list, aux_list, low, mid)
    recursive_sort(a_list, aux_list, mid + 1, hi)
    if not less(a_list[mid + 1], a_list[mid]):
        return
    merge(a_list, aux_list, low, mid, hi)


def iterative_sort(a_list: list, aux_list: list, low: int, hi: int):
    """
    iterative function for merge sort
    :param a_list: pointer to array to sort
    :param aux_list: pointer to aux_array
    :param low: index from which to sort
    :param hi: index to which to sort
    """
    if hi <= low:
        return

    stride = 1
    while stride <= len(a_list):
        for i in range(0, len(a_list), 2*stride):
            merge(a_list, aux_list, i, i + stride - 1, min(i+2*stride-1, hi))
        stride *= 2


def merge_sort(a_list: list, implementation: str = 'recursive'):
    """
    perform merge sort to to a_list using aux_list
    complexity O(N log N)
    space complexity extra N for aux_list
    :param a_list: a list to sort
    :param implementation: use either recursive or iterative version of the sort
    """
    aux_list = [None] * len(a_list)
    if implementation == 'recursive':
        recursive_sort(a_list, aux_list, 0, len(a_list) - 1)
    elif implementation == 'iterative':
        iterative_sort(a_list, aux_list, 0, len(a_list) - 1)
    else:
        raise RuntimeError("unrecognized implementation of merge sort %s" % implementation)
