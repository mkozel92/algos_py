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

    def recursive_put(self, node: Union[Node, None], key: str, value: Any, d: int):
        c = key[d]
        if node is None:
            node = self.Node()
            node.key = c
        if c < node.key:
            node.left = self.recursive_put(node.left, key, value, d)
        elif c > node.key:
            node.right = self.recursive_put(node.right, key, value, d)
        elif d < len(key) - 1:
            node.middle = self.recursive_put(node.middle, key, value, d + 1)
        else:
            node.value = value
        return node

    def put(self, key: str, value: Any):
        self.root = self.recursive_put(self.root, key, value, 0)

    def get(self, key: str) -> Any:
        current = self.root
        d = 0
        while current is not None:
            if current.key == key[d]:
                d += 1
                if d >= len(key):
                    return current.value
                current = current.middle
            elif key[d] < current.key:
                current = current.left
            else:
                current = current.right
        return None

