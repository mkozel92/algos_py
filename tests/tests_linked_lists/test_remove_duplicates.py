import unittest
from copy import deepcopy

from linked_lists.linked_list import LinkedList
from linked_lists.remove_duplicates import remove_duplicates_no_buffer, remove_duplicates


class TestRemoveDuplicates(unittest.TestCase):

    def setUp(self) -> None:
        self.original_list = LinkedList()
        self.original_list.insert_many([2, 4, 5, 7, 6, 5, 4, 3, 3, 3, 3, 2, 9])
        self.processed_list = [2, 4, 5, 7, 6, 3, 9]

    def test_remove_duplicates(self):
        list_copy = deepcopy(self.original_list)
        remove_duplicates(list_copy)
        self.assertEqual(list_copy.get_as_list(), self.processed_list)

        list_copy = deepcopy(self.original_list)
        remove_duplicates_no_buffer(list_copy)
        self.assertEqual(list_copy.get_as_list(), self.processed_list)
