import unittest

from search.search_rotated import search_rotated


class TestSearchRotated(unittest.TestCase):

    def test_search_rotated(self):
        for i in range(1, 9):
            self.assertEqual(search_rotated([5, 6, 7, 8, 9, 1, 2, 3, 4], i), (i + 4) % 9)
