import unittest

from bit_manipulation.longest_sequence import longest_sequence


class TestLongestSequence(unittest.TestCase):

    def test_longest_sequence(self):
        self.assertEqual(longest_sequence(5), 3)
        self.assertEqual(longest_sequence(7), 4)
        self.assertEqual(longest_sequence(8), 2)
        self.assertEqual(longest_sequence(0), 1)