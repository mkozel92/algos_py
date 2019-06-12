from typing import Any, Union


class RWayTrie(object):

    class Node(object):

        def __init__(self, radix: int):
            self.next = [None] * radix
            self.value = None

    def __init__(self, radix: int):
        self.radix = radix
        self.root = self.Node(radix)

    def recursive_put(self, node: Union[Node, None], key: str, value: Any):
        if node is None:
            node = self.Node(self.radix)
        if not key:
            node.value = value
            return node
        node.next[ord(key[0])] = self.recursive_put(node.next[ord(key[0])], key[1:], value)
        return node

    def put(self, key: str, value: Any):
        self.recursive_put(self.root, key, value)

    def get(self, key: str) -> Any:
        current = self.root
        while current is not None:
            if not key:
                return current.value
            current = current.next[ord(key[0])]
            key = key[1:]
        return None
