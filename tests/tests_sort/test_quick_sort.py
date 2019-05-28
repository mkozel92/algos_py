import unittest

from random import shuffle
from sort.quick_sort import quick_sort


class TestQuickSort(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_integer_sort_recursive(self):
        a_list = list(range(100))
        shuffle(a_list)
        quick_sort(a_list, 'basic')
        self.assertEqual(a_list, list(range(100)))

    def test_string_sort_recursive(self):
        a_list = ["this", "is", "some", "sample", "data", "for", "sorting", "test"]
        b_list = a_list.copy()
        quick_sort(a_list, 'basic')
        b_list.sort()
        self.assertEqual(a_list, b_list)

    def test_integer_sort_iterative(self):
        a_list = list(range(100))
        shuffle(a_list)
        quick_sort(a_list, 'three_way')
        self.assertEqual(a_list, list(range(100)))

    def test_string_sort_iterative(self):
        a_list = ["this", "is", "some", "sample", "data", "for", "sorting", "test"]
        b_list = a_list.copy()
        quick_sort(a_list, 'three_way')
        b_list.sort()
        self.assertEqual(a_list, b_list)
