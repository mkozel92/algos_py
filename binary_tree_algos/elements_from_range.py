from binary_tree_algos.binary_tree import BinaryTree
from data_structures.linked_list_queue import LinkedListQueue
from typing import Any


def get_elements_from_range(node: BinaryTree.Node, q: LinkedListQueue, low: Any, hi: Any):
    """
    enqueues elements of a tree from given range
    complexity O(M + log N)
    :param node: root of three to search
    :param low: lower limit of ot range
    :param hi: upper limit of the range
    :param  q: queue to store elements from the range
    """
    if node is None:
        return
    if node.key < low:
        get_elements_from_range(node.right, q, low, hi)
    elif node.key > hi:
        get_elements_from_range(node.left, q, low, hi)
    else:
        get_elements_from_range(node.left, q, low, hi)
        q.enqueue((node.key, node.data))
        get_elements_from_range(node.right, q, low, hi)
