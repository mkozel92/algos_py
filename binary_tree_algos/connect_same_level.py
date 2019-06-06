from binary_tree_algos.binary_tree import BinaryTree
from data_structures.linked_list_queue import LinkedListQueue


def connect_same_level(root: BinaryTree.Node):
    """
    connects elements of a binary tree that are on the same level
    complexity O(N)
    :param root: root of the tree to connect
    """
    q = LinkedListQueue()
    q.enqueue((root, 0))
    while not q.is_empty():
        current, level = q.dequeue()
        if current.left is not None:
            q.enqueue((current.left, level + 1))
        if current.right is not None:
            q.enqueue((current.right, level + 1))
        data = q.peek()
        if data[1] == level:
            current.next = data[0]
