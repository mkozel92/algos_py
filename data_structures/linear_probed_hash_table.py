from typing import Any


class LinearProbedHashTable(object):
    """Simple hash table with linear probing"""
    def __init__(self, size:int = 100):
        """
        initialize with lists for keys and values of given size
        :param size: size of table
        """
        self.keys = [None] * size
        self.values = [None] * size
        self.size = size

    def put(self, key: Any, value: Any):
        """
        insert key value pair into table
        complexity O(N)
        basically constant if table is at most half full
        :param key: key
        :param value: value
        """
        i = abs(hash(key) % self.size)
        original_i = i
        while self.keys[i] is not None and self.keys[i] != key:
            i = (i+1) % self.size
            if i == original_i:
                print("table is full")
                return
        self.keys[i] = key
        self.values[i] = value

    def get(self, key: Any) -> Any:
        """
        gets value associated with given key
        complexity O(N)
        basically constant if table is at most half full
        :param key: key
        :returns: value
        """
        i = abs(hash(key) % self.size)
        original_i = i
        while self.keys[i] is not None and self.keys[i] != key:
            i = (i + 1) % self.size
            if i == original_i:
                return
        return self.values[i]

