from binary_tree_algos.binary_tree import BinaryTree


def common_ancestor(a_node: BinaryTree.Node, b_node: BinaryTree.Node, root: BinaryTree.Node):
    """
    recursively finds common ancestor in a binary tree
    complexity O(N)
    :param a_node: first node
    :param b_node: second node
    :param root: root of the tree
    :return: bools if given nodes are in a subtree and first common ancestor
    """
    if root is None:
        return False, False, None

    has_a = root is a_node
    has_b = root is b_node

    left_has_a, left_has_b, ancestor_node = common_ancestor(a_node, b_node, root.left)
    if ancestor_node is not None:
        return True, True, ancestor_node

    right_has_a, right_has_b, ancestor_node = common_ancestor(a_node, b_node, root.right)
    if ancestor_node is not None:
        return True, True, ancestor_node

    has_a = left_has_a or has_a or right_has_a
    has_b = left_has_b or has_b or right_has_b

    if has_a and has_b:
        return True, True, root

    return has_a, has_b, None
