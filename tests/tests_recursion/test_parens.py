import unittest

from recursion.parens import parens


class TestParens(unittest.TestCase):

    def test_parens(self):
        res = []
        cur = [None] * 6
        parens(6 - 1, 0, res, cur)
        self.assertEqual(len(res), 5)
