import unittest

from recursion.stack_boxes import stack_boxes, Box


class TestStackBoxes(unittest.TestCase):

    def test_stack_boxes(self):
        self.assertEqual(stack_boxes([Box(1, 5, 6), Box(2, 7, 8), Box(3, 6, 7)]), 4)
        self.assertEqual(stack_boxes([Box(1, 5, 6), Box(2, 7, 8), Box(1, 6, 7)]), 3)
        self.assertEqual(stack_boxes([Box(1, 5, 6)]), 1)
