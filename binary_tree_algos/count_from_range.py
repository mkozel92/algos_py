from binary_tree_algos.binary_tree import BinaryTree
from typing import Any


def tree_size(node: BinaryTree.Node) -> int:
    if node is None:
        return 0
    return node.count


def count_from_range(node: BinaryTree.Node, low: Any, hi: Any):
    """
    counts elements of a tree from given range
    complexity O(2log N)
    :param node: root of three to search
    :param low: lower limit of ot range
    :param hi: upper limit of the range
    """
    if node is None:
        return 0
    return max(0, node.count - count_lower(node, low) - count_higher(node, hi))


def count_lower(node: BinaryTree.Node, key: Any) -> int:
    """
    counts elements lower then given key
    complexity O(log N)
    :param node: root of three to count in
    :param key: key to compare
    :return: num of nodes
    """
    if node is None:
        return 0
    if key < node.key:
        return count_lower(node.left, key)
    elif key > node.key:
        return count_lower(node.right, key) + 1 + tree_size(node.left)
    else:
        return tree_size(node.left)


def count_higher(node: BinaryTree.Node, key: Any) -> int:
    """
    counts elements higher then given key
    complexity O(log N)
    :param node: root of three to count in
    :param key: key to compare
    :return: num of nodes
    """
    if node is None:
        return 0
    if key < node.key:
        return count_higher(node.left, key) + 1 + tree_size(node.right)
    elif key > node.key:
        return count_higher(node.right, key)
    else:
        return tree_size(node.right)

