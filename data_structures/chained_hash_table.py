from typing import Any


class ChainedHashTable(object):
    """hash table using separate chaining"""
    class Node(object):
        """node for linked list in the hash table"""
        def __init__(self, k: Any, v: Any):
            self.key = k
            self.value = v
            self.next = None

    def __init__(self, size: int = 100):
        """
        initialize hash table with a size for the list of pointer to the LLs
        :param size: size of the list for pointers
        """
        self.data = [None] * size
        self.size = size

    def put(self, k: Any, v: Any):
        """
        add key value pair to the hash table
        Complexity O(log N) for uniformly random hash function
        on average constant time
        :param k: key
        :param v: value
        """
        i = abs(hash(k)) % self.size
        current = self.data[i]
        while current is not None:
            if current.key == k:
                current.value = v
                return
            current = current.next
        new_node = self.Node(k, v)
        new_node.next = self.data[i]
        self.data[i] = new_node

    def get(self, k: Any) -> Any:
        """
        get value associated with given key
        Complexity O(log N) for uniformly random hash function
        on average constant time
        :param k: key
        :returns: value
        """
        i = abs(hash(k)) % self.size
        current = self.data[i]
        while current is not None:
            if current.key == k:
                return current.value
            current = current.next
        return None

    def delete(self, k: Any) -> Any:
        """
        delete node with given key
        Complexity O(log N) for uniformly random hash function
        on average constant time
        :param k: key
        """
        i = abs(hash(k)) % self.size
        current = self.data[i]
        last = None
        while current is not None:
            if current.key == k:
                if last is not None:
                    last.next = current.next
                else:
                    self.data[i] = None
            last = current
            current = current.next
