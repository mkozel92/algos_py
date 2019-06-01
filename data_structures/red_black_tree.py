from typing import Any


class RedBlackTree(object):
    """implementation of red black tree that ensures balanced tree"""
    class Node(object):
        """node of the tree"""
        def __init__(self, key: Any, value: Any):
            self.left = None
            self.right = None
            self.key = key
            self.value = value
            self.is_red = True

    def __init__(self):
        """
        initialize by setting root to None
        """
        self.root = None

    @staticmethod
    def flip_colors(node: Node):
        """
        helper method for red balck tree balancing
        :param node: flip colors for this node
        """
        node.right.is_red = False
        node.left.is_red = False
        node.is_red = True

    @staticmethod
    def rotate_left(node: Node) -> Node:
        """
        helper method for red black tree balancing
        :param node: rotate this node
        :return: pointer the new root node after rotation
        """
        tmp = node.right
        node.right = tmp.left
        tmp.is_red = node.is_red
        node.is_red = True
        tmp.left = node
        return tmp

    @staticmethod
    def rotate_right(node: Node) -> Node:
        """
        helper method for red black tree balancing
        :param node: rotate this node
        :return: pointer the new root node after rotation
        """
        tmp = node.left
        node.left = tmp.right
        tmp.is_red = node.is_red
        node.is_red = True
        tmp.right = node
        return tmp

    @staticmethod
    def _is_red(node: Node) -> bool:
        """
        Checks if link leading to this node is red
        :param node: node to check
        :return: True if the link is red
        """
        if node is None:
            return False
        return node.is_red

    def put(self, k: Any, v: Any):
        """
        adds new node to the tree
        complexity 0(log N) as the tree is guaranteed to be balanced
        :param k: key to insert
        :param v: value to insert
        """
        self.root = self.recursive_put(self.root, k, v)

    def recursive_put(self, node: Node, k: Any, v: Any) -> Node:
        """
        recursive function to add new node and balance the tree
        :param node: root of the tree to add the node to
        :param k: key to add
        :param v: value to add
        :return: root of the new tree with added node
        """
        if node is None:
            return self.Node(k, v)
        if k < node.key:
            node.left = self.recursive_put(node.left, k, v)
        elif k > node.key:
            node.right = self.recursive_put(node.right, k, v)
        else:
            node.value = v

        if self._is_red(node.right) and not self._is_red(node.left):
            node = self.rotate_left(node)
        if self._is_red(node.left) and self._is_red(node.left.left):
            node = self.rotate_right(node)
        if self._is_red(node.left) and self._is_red(node.right):
            self.flip_colors(node)

        return node

    def print_preorder(self, node: Node):
        """
        print preorder to ensure that inserting sorted elements lead to balanced tree
        :param node: root of the tree to print
        """
        if node is None:
            return
        print(node.key)
        self.print_preorder(node.left)
        self.print_preorder(node.right)

