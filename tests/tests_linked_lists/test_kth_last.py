import unittest

from linked_lists.find_kth_last import find_kth_last, find_kth_last_recursive
from linked_lists.linked_list import LinkedList


class TestKthLast(unittest.TestCase):

    def setUp(self) -> None:
        self.original_list = LinkedList()
        self.original_list.insert_many([1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_remove_duplicates(self):
        self.assertEqual(find_kth_last(self.original_list, 0), 9)
        self.assertEqual(find_kth_last(self.original_list, 1), 8)
        self.assertEqual(find_kth_last(self.original_list, 2), 7)
        self.assertEqual(find_kth_last(self.original_list, 3), 6)
        self.assertEqual(find_kth_last(self.original_list, 20), None)

    def test_remove_duplicates_recursive(self):
        self.assertEqual(find_kth_last_recursive(self.original_list, 0), 9)
        self.assertEqual(find_kth_last_recursive(self.original_list, 1), 8)
        self.assertEqual(find_kth_last_recursive(self.original_list, 2), 7)
        self.assertEqual(find_kth_last_recursive(self.original_list, 3), 6)
        self.assertEqual(find_kth_last_recursive(self.original_list, 20), None)
