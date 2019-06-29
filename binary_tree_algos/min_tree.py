from binary_tree_algos.binary_tree import BinaryTree


def add_to_tree(a_list: list, from_: int, to_: int):
    """
    recursively build tree
    keep the tree balanced by adding elements from the middle of given lists
    :param a_list: a list to build the tree from
    :param from_: from index in a list
    :param to_: to index in a list
    :param a_tree: tree to build
    """
    if from_ > to_:
        return None

    mid = (from_ + to_) // 2
    a_node = BinaryTree.Node(a_list[mid], "")

    a_node.left = add_to_tree(a_list, from_, mid - 1)
    a_node.right = add_to_tree(a_list, mid + 1, to_)
    return a_node


def min_tree(a_list: list) -> BinaryTree:
    """
    build tree of minimal height given a list of elements
    complexity O(N)
    :param a_list: a list to build tree from
    :return: binary tree
    """
    a_list.sort()
    bt = BinaryTree()
    bt.root = add_to_tree(a_list, 0, len(a_list) - 1)
    return bt

