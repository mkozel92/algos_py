import unittest

from linked_lists.linked_list import LinkedList
from linked_lists.partition import partition


class TestPartition(unittest.TestCase):

    def test_partition(self):
        a_list = LinkedList()
        a_list.insert_many([9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 40, 6])
        partition_element = 5
        partition(a_list, partition_element)

        less = True
        for element in a_list.get_as_list():
            if element >= partition_element:
                less = False
            if less:
                self.assertTrue(element < partition_element)
            else:
                self.assertTrue(element >= partition_element)
