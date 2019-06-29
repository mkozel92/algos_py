from typing import Any

from data_structures.linked_list_stack import LinkedListStack


class MinStack(object):
    """
    stack implementing a constant access time to the min element
    """
    def __init__(self):
        self.min_stack = LinkedListStack()
        self.stack = LinkedListStack()

    def push(self, value: Any):
        """
        push value into stack and update currently min value if necessary
        :param value: value to push
        """
        self.stack.push(value)
        if not self.min_stack.peek():
            self.min_stack.push(value)
        elif self.min_stack.peek() > value:
            self.min_stack.push(value)

    def min(self) -> Any:
        """
        :return: current min value in the stack that is kept on the top of the min_stack
        """
        return self.min_stack.peek()

    def pop(self) -> Any:
        """
        pop value from the stack and update current min stack if necessary
        :return: top of the stack
        """
        value = self.stack.pop()
        if value == self.min_stack.peek():
            self.min_stack.pop()
        return value
