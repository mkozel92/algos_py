from typing import Any
from sort.sort_utils import swap

CAPACITY = 100


class MinHeap(object):
    """ implementation of min Binary heap with fixed capacity"""

    def __init__(self):
        """
        initialize heap with a list of Nones and set current size to 0
        """
        self.data = [None] * CAPACITY
        self.current_size = 0

    def swim(self, index: int):
        """
        swim element at the given index to fix heap order
        :param index: index of element to swim
        """
        while index > 1 and self.data[index] < self.data[index//2]:
            swap(self.data, index, index // 2)
            index //= 2

    def sink(self, index: int):
        """
        sink element at the given index to fix heap order
        :param index: index of element to sink
        """
        while 2*index <= self.current_size:
            if self.current_size < 2*index + 1:
                smaller_child = 2 * index
            elif self.data[2*index] < self.data[2*index+1]:
                smaller_child = 2 * index
            else:
                smaller_child = 2 * index + 1

            if self.data[smaller_child] < self.data[index]:
                swap(self.data, smaller_child, index)
                index = smaller_child
            else:
                break

    def insert(self, data: Any):
        """
        insert element to the heap
        complexity O(log N)
        :param data: data to insert
        """
        self.current_size += 1
        self.data[self.current_size] = data
        self.swim(self.current_size)

    def remove(self) -> Any:
        """
        remove smallest element from the heap
        complexity O(log N)
        :return: smallest element
        """
        data = self.data[1]
        swap(self.data, 1, self.current_size)
        self.data[self.current_size] = None
        self.current_size -= 1
        self.sink(1)
        return data

    def is_empty(self) -> bool:
        """
        :return: True if the heap is empty
        """
        return self.current_size == 0
