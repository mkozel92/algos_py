import unittest
from binary_tree_algos.binary_tree import BinaryTree
from binary_tree_algos.bst_sequences import bst_sequences


class TestBstSequence(unittest.TestCase):

    def setUp(self) -> None:
        self.bt = BinaryTree()
        self.bt.put(2, "")
        self.bt.put(1, "")
        self.bt.put(3, "")
        self.bt.put(4, "")
        self.bt.put(5, "")

    def test_bst_sequence(self):
        possible_next = [self.bt.root]
        seq = bst_sequences(possible_next)
        self.assertEqual(seq, [[2, 1, 3, 4, 5], [2, 3, 1, 4, 5], [2, 3, 4, 1, 5], [2, 3, 4, 5, 1]])
