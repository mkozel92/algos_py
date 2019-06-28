from typing import Any

from linked_lists.linked_list import LinkedList


def partition(a_list: LinkedList, a_value: Any):
    """
    Partition linked list such that all elements on the left side are lower then partitioning element
    complexity O(N)
    :param a_list: list to partition
    :param a_value: a value to partition on
    """
    processed = a_list.head
    less_then = a_list.head

    while processed:
        if processed.data < a_value:
            tmp = processed.data
            processed.data = less_then.data
            less_then.data = tmp
            less_then = less_then.next
        processed = processed.next

