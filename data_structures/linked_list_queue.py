from typing import Any


class LinkedListQueue(object):
    """
    A Stack implemented using a Linked list
    """

    class Node(object):
        """"Node for a Linked list"""
        def __init__(self, data):
            self.next = None
            self.data = data

    def __init__(self):
        self.first = None
        self.last = None
        self.current = None

    def __iter__(self):
        self.current = self.first
        return self

    def __next__(self):
        if self.current:
            data = self.current.data
            self.current = self.current.next
            return data
        else:
            raise StopIteration

    def enqueue(self, data: Any):
        """
        enqueue data to the beginning of the queue
        complexity O(1)
        :param data: data to enqueue
        """
        new_node = self.Node(data)
        if self.is_empty():
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = self.last.next

    def dequeue(self) -> Any:
        """
        removes first node and returns its data
        complexity O(1)
        :return: data from to top node
        """
        if not self.is_empty():
            data = self.first.data
            self.first = self.first.next
            return data
        return None

    def peek(self) -> Any:
        """
        returns data from top node
        complexity O(1)
        :return: data from to top node
        """
        if not self.is_empty():
            data = self.first.data
            return data
        return None

    def is_empty(self):
        """
        :return: True if the Queue is empty
        """
        return self.first is None

    def print_queue(self):
        node = self.first
        while node:
            print(node.data)
            node = node.next
