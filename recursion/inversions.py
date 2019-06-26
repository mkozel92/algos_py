

def merge(a_list: list, aux_list: list, low: int, mid: int, high: int) -> int:
    """
    Merge subroutine similar to merger sort but keeping track of num of inversions.
    Every time we select an element from the right sub-array it means we found mid - i inversions
    that is number of element in the left sub-array we jump over by taking element from the right sub-array
    :param a_list: a list to merge
    :param aux_list: helper list
    :param low: merge from here
    :param mid: division point for merge
    :param high: merge to here
    :return: num of inversions found during merging
    """
    for i in range(low, high + 1):
        aux_list[i] = a_list[i]

    i = low
    j = mid + 1
    k = low

    inversions = 0

    while k <= high:

        if i > mid:
            a_list[k] = aux_list[j]
            j += 1
        elif j > high or aux_list[i] <= aux_list[j]:
            a_list[k] = aux_list[i]
            i += 1
        else:
            a_list[k] = aux_list[j]
            inversions += mid + 1 - i
            j += 1
        k += 1
    return inversions


def recursive_count_inversions(a_list: list, aux_list: list, low: int, high: int) -> int:
    """
    recursive function to count inversions in a list
    :param a_list: a list to count inversions in
    :param aux_list: aux list for merge subroutine
    :param low: count from this index
    :param high: count to this index
    :return: number of inversions between high and low
    """
    if low >= high:
        return 0
    mid = (low + high) // 2
    count = recursive_count_inversions(a_list, aux_list, low, mid)
    count += recursive_count_inversions(a_list, aux_list, mid + 1, high)
    count += merge(a_list, aux_list, low, mid, high)
    return count


def count_inversions(a_list: list) -> int:
    """
    count inversions in a list
    inversion is every pair i,j such that j > i and a_list[i] > a_list[j]
    basically all out of order pairs
    complexity O(N log N)
    :param a_list: list to count
    :return: number of inversions
    """
    aux_list = [0] * len(a_list)
    return recursive_count_inversions(a_list, aux_list, 0, len(a_list) - 1)

