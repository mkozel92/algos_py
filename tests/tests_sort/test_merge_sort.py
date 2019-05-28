import unittest

from random import shuffle
from sort.merge_sort import merge_sort


class TestMergeSort(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_integer_sort_recursive(self):
        a_list = list(range(100))
        shuffle(a_list)
        merge_sort(a_list, 'recursive')
        self.assertEqual(a_list, list(range(100)))

    def test_string_sort_recursive(self):
        a_list = ["this", "is", "some", "sample", "data", "for", "sorting", "test"]
        b_list = a_list.copy()
        merge_sort(a_list, 'recursive')
        b_list.sort()
        self.assertEqual(a_list, b_list)

    def test_integer_sort_iterative(self):
        a_list = list(range(100))
        shuffle(a_list)
        merge_sort(a_list, 'iterative')
        self.assertEqual(a_list, list(range(100)))

    def test_string_sort_iterative(self):
        a_list = ["this", "is", "some", "sample", "data", "for", "sorting", "test"]
        b_list = a_list.copy()
        merge_sort(a_list, 'iterative')
        b_list.sort()
        self.assertEqual(a_list, b_list)
