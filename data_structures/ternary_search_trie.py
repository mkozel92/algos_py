from typing import Any, Union


class TernarySearchTrie(object):

    class Node(object):

        def __init__(self):
            self.left = None
            self.middle = None
            self.right = None
            self.value = None
            self.key = None

    def __init__(self):
        self.root = None

    def recursive_put(self, node: Union[Node, None], key: str, value: Any):
        if node is None:
            node = self.Node()
            node.key = key[0]
            if len(key) == 1:
                node.value = value
                return node
            else:
                node.middle = self.recursive_put(None, key[1:], value)
                return node
        elif key[0] == node.key:
            key = key[1:]
            if not key:
                node.value = value
                return node

        if node.middle and node.middle.key == key[0]:
            node.middle = self.recursive_put(node.middle, key, value)
        elif key[0] < node.key:
            node.left = self.recursive_put(node.left, key, value)
        else:
            node.right = self.recursive_put(node.right, key, value)
        return node

    def put(self, key: str, value: Any):
        self.root = self.recursive_put(self.root, key, value)

    def get(self, key: str) -> Any:
        current = self.root
        while current is not None:
            if current.key == key[0]:
                key = key[1:]
            if not key:
                return current.value
            if current.middle and current.middle.key == key[0]:
                current = current.middle
            elif key[0] < current.key:
                current = current.left
            else:
                current = current.right
        return None

