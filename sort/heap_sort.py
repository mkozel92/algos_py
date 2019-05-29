from sort.sort_utils import swap


def sink(a_list: list, k: int, n: int):
    """
    sink operation for heap sort
    :param a_list: a list in which to perform the sink
    :param k: sink element on this index
    :param n: sink only up to this index
    """
    while (k+1)*2 <= n+1:
        left_child = 2 * (k+1) - 1
        right_child = min(2 * (k+1), n)

        if a_list[left_child] < a_list[right_child]:
            bigger_child = right_child
        else:
            bigger_child = left_child

        if a_list[bigger_child] > a_list[k]:
            swap(a_list, k, bigger_child)
            k = bigger_child
        else:
            break


def heap_sort(a_list: list):
    """
    performs in place heap sort using principles of binary heap
    complexity O(N log N)
    :param a_list: a list to sort
    """
    for i in range(len(a_list)//2, -1, -1):
        sink(a_list, i, len(a_list) - 1)
    for i in range(len(a_list)):
        swap(a_list, 0, len(a_list) - i - 1)
        sink(a_list, 0, len(a_list) - i - 2)
