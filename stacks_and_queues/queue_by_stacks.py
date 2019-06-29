from typing import Any

from data_structures.linked_list_stack import LinkedListStack


class QueueByStacks(object):
    """
    Queue implemented by two stacks
    """

    def __init__(self):
        self.first_stack = LinkedListStack()
        self.second_stack = LinkedListStack()

    def enqueue(self, value: Any):
        """
        enqueue and element in o(1) time
        :param value: value to enqueue
        """
        self.first_stack.push(value)

    def dequeue(self) -> Any:
        """
        dequeue and element in O(N) time
        :return: value
        """
        if self.second_stack.is_empty():
            while not self.first_stack.is_empty():
                self.second_stack.push(self.first_stack.pop())

        return self.second_stack.pop()

