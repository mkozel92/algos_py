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


def kth_last_recursion(a_node, k):
    """
    recursive routine for finding kth last element
    :param a_node: current node
    :param k: k
    :return: index of current node and found data
    """
    data = None
    if a_node.next is None:
        index = 0
    else:
        index, data = kth_last_recursion(a_node.next, k)

    if index == k:
        return index + 1, a_node.data

    if data is not None:
        return index + 1, data

    return index + 1, None


def find_kth_last_recursive(a_list: LinkedList, k: int):
    """
    recursive implementation of kth to last element
    complexity O(N) with N extra space
    :param a_list: linked list to search
    :param k: K
    :return: kth last element of None
    """
    _, data = kth_last_recursion(a_list.head, k)
    return data
