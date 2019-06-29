from binary_tree_algos.binary_tree import BinaryTree


def recursive_is_balanced(a_node: BinaryTree.Node) -> (bool, int):
    """
    recursively check balance of both subtrees
    :param a_node: root of a subtree to check
    :return: boolean showing if a subtree is balanced and height of the subtree
    """
    if a_node is None:
        return True, 0

    left, left_height = recursive_is_balanced(a_node.left)
    right, right_height = recursive_is_balanced(a_node.right)
    balanced = abs(left_height - right_height) <= 1
    bigger_height = left_height if left_height > right_height else right_height

    return balanced and left and right, bigger_height + 1


def is_balanced(a_tree: BinaryTree) -> bool:
    """
    check if given tree is balanced
    complexity O(N)
    :param a_tree: a tree to check
    :return: true if the tree is balanced
    """
    balanced, _ = recursive_is_balanced(a_tree.root)
    return balanced
