import unittest

from stacks_and_queues.min_stack import MinStack


class TestMinStack(unittest.TestCase):

    def setUp(self) -> None:
        self.min_stack = MinStack()

    def test_min_stack(self):

        self.min_stack.push(10)
        self.assertTrue(self.min_stack.min(), 10)

        self.min_stack.push(20)
        self.assertTrue(self.min_stack.min(), 10)

        self.min_stack.push(5)
        self.assertTrue(self.min_stack.min(), 5)

        self.min_stack.push(5)
        self.assertTrue(self.min_stack.min(), 7)

        self.min_stack.push(5)
        self.assertTrue(self.min_stack.min(), 8)

        self.min_stack.pop()
        self.assertTrue(self.min_stack.min(), 5)

        self.min_stack.pop()
        self.assertTrue(self.min_stack.min(), 5)

        self.min_stack.pop()
        self.assertTrue(self.min_stack.min(), 10)
