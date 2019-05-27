import unittest

from random import shuffle
from sort.insertion_sort import insertion_sort


class TestInsertionSort(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_integer_sort(self):
        a_list = list(range(100))
        shuffle(a_list)
        insertion_sort(a_list)
        self.assertEqual(a_list, list(range(100)))

    def test_string_sort(self):
        a_list = ["this", "is", "some", "sample", "data", "for", "sorting", "test"]
        b_list = a_list.copy()
        insertion_sort(a_list)
        b_list.sort()
        self.assertEqual(a_list, b_list)
