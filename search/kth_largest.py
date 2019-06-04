from sort.knuth_shuffle import knuth_shuffle
from sort.quick_sort import partition
from typing import Any


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


a_list = list(range(100))
for k in range(100):
    quick_find(a_list, k)
