import unittest

from search.kth_largest import quick_find, quick_find_three


class TestKthLargest(unittest.TestCase):

    def test_kth_largest(self):
        a_list = list(range(100))
        for k in range(100):
            self.assertEqual(quick_find(a_list, k), k)

    def test_kth_largest_three(self):
        a_list = list(range(100))
        for k in range(100):
            self.assertEqual(quick_find_three(a_list, k), k)

        a_list = [1, 2, 5, 4, 5, 5, 7, 8, 5]
        self.assertEqual(quick_find_three(a_list, 3), 5)
        self.assertEqual(quick_find_three(a_list, 4), 5)
        self.assertEqual(quick_find_three(a_list, 5), 5)
        self.assertEqual(quick_find_three(a_list, 6), 5)
        self.assertEqual(quick_find_three(a_list, 7), 7)
