from sort.knuth_shuffle import knuth_shuffle
from sort.sort_utils import less, swap


def partition(a_list: list, low: int, hi: int) -> int:
    """
    function to partition a list on the first element in such a way that
    all elements on the left of the array are lower then the partitioning element
    and everything to the right is higher
    :param a_list: a list to partition
    :param low: partition from this index
    :param hi: partition to this index
    :return: final position of the partitioning element
    """
    i = low + 1
    j = hi

    while i <= j:

        while less(a_list[low], a_list[j]):
            j -= 1
            if j <= low:
                break

        while less(a_list[i], a_list[low]):
            i += 1
            if i >= hi:
                break

        if i >= j:
            break
        swap(a_list, i, j)

    swap(a_list, low, j)
    return j


def recursive_sort(a_list: list, low, hi):
    """
    recursive version of the basic implementation of the quick sort
    :param a_list: a list to sort
    :param low: sort from this index
    :param hi: sort to this index
    """
    if low >= hi:
        return
    mid = partition(a_list, low, hi)
    recursive_sort(a_list, low, mid - 1)
    recursive_sort(a_list, mid + 1, hi)


def three_way_sort(a_list, low, hi):
    """
    recursive implementation of quick sort with three way partitioning
    :param a_list: a list to sort
    :param low: sort from this index
    :param hi: sort to this index
    """
    if hi <= low:
        return
    lt = low
    gt = hi
    v = a_list[low]
    i = low
    while i <= gt:

        if a_list[i] < v:
            swap(a_list, lt, i)
            lt += 1
            i += 1
        elif a_list[i] > v:
            swap(a_list, i, gt)
            gt -= 1
        else:
            i += 1

    three_way_sort(a_list, low, lt -1)
    three_way_sort(a_list, gt + 1, hi)


def quick_sort(a_list: list, implementation: str = "basic"):
    """
    implementation of inplace quick sort
    complexity o(N^2) but random shuffle basically ensures O(N log N)
    three way sort needed to ensure O(N log N) with duplicate keys
    :param a_list: list to sort
    :param implementation: either basic or three way implementation
    """
    knuth_shuffle(a_list)
    if implementation == 'basic':
        recursive_sort(a_list, 0, len(a_list) - 1)
    elif implementation == 'three_way':
        three_way_sort(a_list, 0, len(a_list) - 1)
    else:
        raise RuntimeError("Unknown implementation for quick sort: %s" % implementation)
