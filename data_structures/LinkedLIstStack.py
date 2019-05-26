from typing import Any


class LinkedListStack(object):
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

    def push(self, data: Any):
        """
        pushes data on the top of the stack
        complexity O(1)
        :param data: data to push
        """
        tmp = self.first
        self.first = self.Node(data)
        self.first.next = tmp

    def peek(self) -> Any:
        """
        return data from top of the stack without removing the top node
        :return: data from the top node
        """
        return self.first.data

    def pop(self) -> Any:
        """
        removes top node and returns its data
        complexity O(1)
        :return: data from to top node
        """
        data = self.first.data
        self.first = self.first.next
        return data

    def is_empty(self):
        """
        :return: True if the Stack is empty
        """
        return self.first is None

    def print_stack(self):
        node = self.first
        while node:
            print(node.data)
            node = node.next
