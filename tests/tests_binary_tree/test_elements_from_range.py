import unittest
from random import shuffle

from binary_tree_algos.binary_tree import BinaryTree
from binary_tree_algos.elements_from_range import get_elements_from_range
from data_structures.linked_list_queue import LinkedListQueue


class TestElemntsFromRange(unittest.TestCase):

    def setUp(self) -> None:
        self.bst = BinaryTree()
        a_list = list(range(100))
        shuffle(a_list)
        for x in a_list:
            self.bst.put(x, "sample_data")

    def test_ranges(self):
        q = LinkedListQueue()
        get_elements_from_range(self.bst.root, q, 40, 50)
        i = 40
        for e in q:
            self.assertEqual(e[0], i)
            self.assertEqual(e[1], 'sample_data')
            i += 1

    def test_empty_ranges(self):
        q = LinkedListQueue()
        get_elements_from_range(self.bst.root, q, 50, 40)
        self.assertTrue(q.is_empty())
