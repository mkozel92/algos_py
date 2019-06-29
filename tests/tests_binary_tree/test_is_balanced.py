import unittest

from binary_tree_algos.binary_tree import BinaryTree
from binary_tree_algos.is_balanced import is_balanced


class TestIsBalnced(unittest.TestCase):

    def setUp(self) -> None:
        self.balanced_tree = BinaryTree()
        self.unbalanced_tree = BinaryTree()

        self.balanced_tree.put(5, 1)
        self.balanced_tree.put(3, 1)
        self.balanced_tree.put(7, 1)
        self.balanced_tree.put(4, 1)
        self.balanced_tree.put(2, 1)
        self.balanced_tree.put(6, 1)
        self.balanced_tree.put(8, 1)

        self.unbalanced_tree.put(5, 1)
        self.unbalanced_tree.put(3, 1)
        self.unbalanced_tree.put(7, 1)
        self.unbalanced_tree.put(6, 1)
        self.unbalanced_tree.put(7, 1)
        self.unbalanced_tree.put(8, 1)
        self.unbalanced_tree.put(9, 1)

    def test_is_balanced(self):
        self.assertTrue(is_balanced(self.balanced_tree))
        self.assertFalse(is_balanced(self.unbalanced_tree))

