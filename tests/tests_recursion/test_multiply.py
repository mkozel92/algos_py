import unittest

from recursion.recursive_multiply import multiply


class TestMultiply(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(multiply(5, 10), 50)
        self.assertEqual(multiply(5, 11), 55)
        self.assertEqual(multiply(5, 12), 60)
        self.assertEqual(multiply(7, 7), 49)
