import unittest
from random import shuffle

from binary_tree_algos.binary_tree import BinaryTree
from binary_tree_algos.count_from_range import count_from_range, count_lower, count_higher


class TestCounts(unittest.TestCase):

    def setUp(self) -> None:
        self.bst = BinaryTree()
        a_list = list(range(100))
        shuffle(a_list)
        for x in a_list:
            self.bst.put(x, "sample_data")

    def test_ranges(self):
        self.assertEqual(count_from_range(self.bst.root, 40, 50), 11)
        self.assertEqual(count_from_range(self.bst.root, 50, 40), 0)

    def test_lower(self):
        self.assertEqual(count_lower(self.bst.root, 40,), 40)
        self.assertEqual(count_lower(self.bst.root, -5), 0)

    def test_higher(self):
        self.assertEqual(count_higher(self.bst.root, 40,), 59)
        self.assertEqual(count_higher(self.bst.root, 100), 0)

