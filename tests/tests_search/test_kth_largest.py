import unittest

from search.kth_largest import quick_find


class TestKthLargest(unittest.TestCase):

    def test_kth_largest(self):
        a_list = list(range(100))
        for k in range(100):
            self.assertEqual(quick_find(a_list, k), k)
