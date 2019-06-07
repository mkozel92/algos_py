from typing import Any, Union

from data_structures.data_structure_interfaces import Queue
from data_structures.linked_list_queue import LinkedListQueue


class BSTSymbolTable(object):
    """symbol table implemented using binary search tree"""

    class Node(object):
        """Node for tree structure that holds key, value pair.
           count specifies size of this subtree
           and left and right point to the respective subtrees
        """
        def __init__(self, key: Any, data: Any):
            """
            initializes a Node
            :param key: key of the node
            :param data: data to hold
            """
            self.key = key
            self.data = data
            self.count = 1
            self.left = None
            self.right = None

    def __init__(self):
        """
        initializes tree by setting root to None
        """
        self.root = None

    def get(self, key: Any) -> Union[Any, None]:
        """
        returns value associated with given key
        complexity O(log N) in a balanced tree
        :param key: key to search for
        :return:
        """
        current = self.root
        while current:
            if current.key == key:
                return current.value
            elif key == current.key:
                current = current.left
            else:
                current = current.right
        return None

    def put(self, key: Any, value: Any):
        """
        adds new key value pair to the tree
        complexity O(log N) in a balanced tree
        :param key: the key
        :param value: the value
        """
        self.root = self.recursive_put(self.root, key, value)

    def recursive_put(self, node: Node, key: Any, value: Any) -> Node:
        """
        helper recursive function for adding new nodes
        :param node: root of a subtree where to add new node
        :param key: key for the new node
        :param value: value for the new node
        :return: pointer to a subtree or newly added node
        """
        if node is None:
            return self.Node(key, value)
        if node.key > key:
            node.left = self.recursive_put(node.left, key, value)
        elif node.key < key:
            node.right = self.recursive_put(node.right, key, value)
        else:
            node.data = value
        node.count = 1 + self._size(node.left) + self._size(node.right)
        return node

    @staticmethod
    def _size(node: Node) -> int:
        """
        gets size of a subtree
        complexity O(1)
        :param node: root of a subtree
        :return: size of a subtree
        """
        if node is None:
            return 0
        return node.count

    def __iter__(self):
        """
        returns iterable queie of inorder sorted tree
        :return: queue iterator with inorder sorted tree nodes
        """
        queue = LinkedListQueue()
        self.recursive_inorder(self.root, queue)
        return queue.__iter__()

    def recursive_inorder(self, node: Node, queue: Queue):
        """
        recursive implementation of inorder traversal
        complexity O(N) + N extra space for the queue
        :param node: root of a subtree to travers
        :param queue: queue to hold sorted tree Nodes
        :return: queue of inorder sorted tree Nodes
        """
        if node is None:
            return
        self.recursive_inorder(node.left, queue)
        queue.enqueue((node.key, node.data))
        self.recursive_inorder(node.right, queue)

    def delete(self, key: Any):
        """
        deletes a Node with a given key using Hibbard deletion
        complexity O(log N) in a balanced tree
        :param key: key of a node to delete
        """
        self.root = self._delete(self.root, key)

    def _delete(self, node: Node, key: Any) -> Union[Node, None]:
        """
        recursive helper function for Hibbard deletion
        :param node: root of a subtree to delete from
        :param key: key of the node to delete
        :return: pointer to the new subtree with deleted Node
        """
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.right is None:
                return node.left
            elif node.left is None:
                return node.right

            t = node
            node = self._min(t.right)
            node.right = self._delete_min(t.right)
            node.left = t.left
        node.count = 1 + self._size(node.left) + self._size(node.right)
        return node

    def _delete_min(self, node: Node) -> Node:
        """
        deletes the node with the minimal key
        complexity O(log N) in a balanced tree
        :param node: root of the subtree to delete from
        :return: pointer to the new subtree with deleted node
        """
        if node.left is None:
            return node.right
        node.left = self._delete_min(node.left)
        node.count = 1 + self._size(node.left) + self._size(node.right)
        return node

    @staticmethod
    def _min(node: Node) -> Union[None, Node]:
        """
        returns pointer the the Node with a min key
        complexity O(log N) in a balanced tree
        :param node: root of the subtree to search
        :return: Node with a minimal key
        """
        if node is None:
            return None
        current = node
        while current.left is not None:
            current = current.left
        return current
