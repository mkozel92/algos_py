import unittest

from recursion.inversions import count_inversions


class TestInversions(unittest.TestCase):

    def setUp(self) -> None:
        self.a_list_0 = [1, 3, 5, 2, 4, 6]
        self.a_list_1 = [6, 5, 4, 3, 2, 1]

    def test_inversions(self):
        self.assertEqual(count_inversions(self.a_list_0), 3)
        self.assertEqual(count_inversions(self.a_list_1), 15)
