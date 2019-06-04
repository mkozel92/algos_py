from sort.knuth_shuffle import knuth_shuffle
from sort.quick_sort import partition
from typing import Any, Tuple

from sort.sort_utils import swap


def quick_find(a_list: list, k: int) -> Any:
    """
    function to find kth largest element in a list.
    quick select is based on quick sort partitioning and stops when we
    partitioned the list on k-th element
    complexity worst case O(N^2)
               guaranteed by shuffle O(N log N)
               in practice run ~N

    :param a_list: a list to search in
    :param k: k specifying what to search for
    :return: k-th largest element
    """
    knuth_shuffle(a_list)
    low = 0
    hi = len(a_list) - 1

    while low <= hi:
        j = partition(a_list, low, hi)
        if j > k:
            hi = j-1
        elif j < k:
            low = j+1
        else:
            return a_list[k]
    return a_list[k]


def three_way_partition(a_list: list, from_: int, to_: int) -> Tuple[int, int]:
    """
    tree way partition that split the array to the tree parts
    lesser, equal and greater than the partitioning element
    :param a_list: list to partition
    :param from_: partition from here
    :param to_: partition to here
    :return: lt and gt separators
    """
    v = a_list[from_]
    i = from_
    lt = from_
    gt = to_

    while i <= gt:
        if a_list[i] < v:
            swap(a_list, i, lt)
            i += 1
            lt += 1
        elif a_list[i] > v:
            swap(a_list, i, gt)
            gt -= 1
        else:
            i += 1

    return lt, gt


def quick_find_three(a_list: list, k: int) -> Any:
    """
    function to find kth largest element in a list.
    quick find is based on quick sort partitioning and stops when we
    partitioned the list on k-th element
    complexity worst case O(N^2)
               guaranteed by shuffle O(N log N)
               in practice run ~N

    :param a_list: a list to search in
    :param k: k specifying what to search for
    :return: k-th largest element
    """
    knuth_shuffle(a_list)
    low = 0
    hi = len(a_list) - 1

    while low <= hi:
        lt, gt = three_way_partition(a_list, low, hi)
        if lt > k:
            hi = lt - 1
        elif gt < k:
            low = gt + 1
        else:
            return a_list[lt]
    return a_list[low]
