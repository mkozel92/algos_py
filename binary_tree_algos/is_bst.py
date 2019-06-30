from binary_tree_algos.binary_tree import BinaryTree
from data_structures.linked_list_stack import LinkedListStack


def is_bst_recursive(a_node: BinaryTree.Node, a_stack: LinkedListStack) -> bool:
    """
    use inorder traversal to verify that given tree is BST
    :param a_node: root of a subtree to verify
    :param a_stack: stack that keeps ordered tree elements
    :return: True if given subtree is BST
    """
    if a_node is None:
        return True

    left = is_bst_recursive(a_node.left, a_stack)
    if not a_stack.is_empty() and a_node.data < a_stack.peek():
        return False
    a_stack.push(a_node.data)
    right = is_bst_recursive(a_node.right, a_stack)

    return left and right


def is_bst_no_stack(min_, max_, a_node) -> bool:
    """
    check if given tree is BST using range comparisons
    :param min_: min of range
    :param max_: max of range
    :param a_node: root of subtree to check
    :return: True if given subtree is bst
    """
    if a_node is None:
        return True

    if (min_ is not None and a_node.data < min_) \
            or (max_ is not None and a_node.data > max_):
        return False

    if not is_bst_no_stack(min_, a_node.data, a_node.left) \
            or not is_bst_no_stack(a_node.data, max_, a_node.right):
        return False

    return True


def is_bst(a_tree: BinaryTree) -> bool:
    """
    checks if given tree is BST
    complexity O(N)
    :param a_tree: a tree to check
    :return: True if tree is BST
    """
    a_stack = LinkedListStack()
    return is_bst_recursive(a_tree.root, a_stack)
