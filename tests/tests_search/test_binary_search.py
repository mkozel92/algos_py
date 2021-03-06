import unittest

from search.binary_search import binary_search, recursive_binary_search


class TestBinarySearch(unittest.TestCase):

    def setUp(self) -> None:
        pass

    def test_empty_list(self):
        self.assertEqual(-1, binary_search([], 5))

    def test_present_elements(self):
        a_list = list(range(100))
        self.assertEqual(10, binary_search(a_list, 10))
        self.assertEqual(0, binary_search(a_list, 0))
        self.assertEqual(99, binary_search(a_list, 99))

    def test_missing_elements(self):
        a_list = list(range(100))
        self.assertEqual(-1, binary_search(a_list, 100))
        self.assertEqual(-1, binary_search(a_list, -1))
        self.assertEqual(-1, binary_search(a_list, 150))

    def test_empty_list_recursive(self):
        self.assertEqual(-1, recursive_binary_search([], 5, 0, len([]) - 1))

    def test_present_elements_recursive(self):
        a_list = list(range(100))
        self.assertEqual(10, recursive_binary_search(a_list, 10, 0, len(a_list) - 1))
        self.assertEqual(0, recursive_binary_search(a_list, 0, 0, len(a_list) - 1))
        self.assertEqual(99, recursive_binary_search(a_list, 99, 0, len(a_list) - 1))

    def test_missing_elements_recursive(self):
        a_list = list(range(100))
        self.assertEqual(-1, recursive_binary_search(a_list, 100, 0, len(a_list) - 1))
        self.assertEqual(-1, recursive_binary_search(a_list, -1, 0, len(a_list) - 1))
        self.assertEqual(-1, recursive_binary_search(a_list, 150, 0, len(a_list) - 1))
