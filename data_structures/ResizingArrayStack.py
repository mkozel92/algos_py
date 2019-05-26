from typing import Any


class ResizingArrayStack(object):
    """Stack implemented using resizing array"""
    def __init__(self):
        self.stack = [None]
        self.head = 0
        self.current = 0

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current < self.head:
            data = self.stack[self.current]
            self.current += 1
            return data
        else:
            raise StopIteration

    def push(self, data: Any):
        """
        pushes data to the top of the stack and resizes the stack if needed
        complexity O(N) because of resizing
        immortalized complexity ~1

        :param data: data to push on the stack
        """
        if self.head == len(self.stack):
            self.resize(2*len(self.stack))
        self.stack[self.head] = data
        self.head += 1

    def pop(self) -> Any:
        """
        pops data from the top of the stack and resizes the stack if too empty
        complexity O(N) because of resizing
        immortalized complexity ~1
        :return: data from to top of the stack
        """
        self.head -= 1
        data = self.stack[self.head]
        self.stack[self.head] = None
        if self.head < len(self.stack) // 4:
            self.resize(len(self.stack) // 2)
        return data

    def resize(self, new_size: int):
        """
        creates new stack of the size new_size and copies data over
        :param new_size: size of the new stack
        """
        new_stack = [None] * new_size
        for i in range(min(len(self.stack), new_size)):
            new_stack[i] = self.stack[i]
        self.stack = new_stack

    def print_stack(self):
        print(self.stack)
