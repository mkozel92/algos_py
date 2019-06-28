from linked_lists.linked_list import LinkedList
from typing import Any


def find_kth_last(a_list: LinkedList, k: int) -> Any:
    """
    return Kth last element from a linked list
    :param a_list: linked list to search
    :param k: k
    :return: kth last element or None
    """
    current = a_list.head
    runner = a_list.head
    for _ in range(k):
        runner = runner.next
        if runner is None:
            return None

    while runner.next:
        current = current.next
        runner = runner.next

    return current.data
