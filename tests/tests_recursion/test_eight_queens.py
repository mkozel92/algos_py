import unittest

from recursion.eight_queens import eight_queens


class TestEightQueens(unittest.TestCase):

    def test_eight_queens(self):
        mem = {}
        self.assertEqual(eight_queens(8, set(range(64)), mem), 92)