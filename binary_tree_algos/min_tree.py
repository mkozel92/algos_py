from binary_tree_algos.binary_tree import BinaryTree


def add_to_tree(a_list: list, from_: int, to_: int, a_tree: BinaryTree):
    """
    recursively build tree
    keep the tree balanced by adding elements from the middle of given lists
    :param a_list: a list to build the tree from
    :param from_: from index in a list
    :param to_: to index in a list
    :param a_tree: tree to build
    """
    if from_ > to_:
        return

    mid = (from_ + to_) // 2
    a_tree.put(a_list[mid], '')

    add_to_tree(a_list, from_, mid - 1, a_tree)
    add_to_tree(a_list, mid + 1, to_, a_tree)


def min_tree(a_list: list) -> BinaryTree:
    """
    build tree of minimal height given a list of elements
    :param a_list: a list to build tree from
    :return: binary tree
    """
    a_list.sort()
    bt = BinaryTree()
    add_to_tree(a_list, 0, len(a_list) - 1, bt)
    return bt

