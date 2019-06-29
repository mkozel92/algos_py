import unittest

from data_structures.linked_list_stack import LinkedListStack
from stacks_and_queues.sort_stak import sort_stack


class TestSortStack(unittest.TestCase):

    def setUp(self) -> None:
        self.stack = LinkedListStack()
        for i in [1, 4, 5, 6, 7, 3, 4, 8, 9, 7, 2]:
            self.stack.push(i)

    def test_sort(self):
        sort_stack(self.stack)
        last = 0
        while not self.stack.is_empty():
            self.assertTrue(self.stack.peek() >= last)
            last = self.stack.pop()
