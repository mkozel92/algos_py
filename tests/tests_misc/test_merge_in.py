import unittest

from misc.merge_in import merge_in


class TestMergeIn(unittest.TestCase):

    def test_merge_in(self):
        b = [1, 3, 5, 7]
        a = [2, 4, 6, 8, 9, None, None, None, None]
        merge_in(a, b)
        self.assertEqual(a, list(range(1, 10)))
