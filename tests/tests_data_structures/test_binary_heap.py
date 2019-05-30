import unittest
from random import shuffle

from data_structures.binary_heap import MinHeap


class TestBinaryHeap(unittest.TestCase):

    def setUp(self) -> None:
        self.bh = MinHeap()
        a_list = list(range(50))
        shuffle(a_list)
        for i in a_list:
            self.bh.insert(i)

    def test_heap_order(self):
        last = self.bh.remove()
        while not self.bh.is_empty():
            current = self.bh.remove()
            self.assertTrue(current >= last)
            last = current

