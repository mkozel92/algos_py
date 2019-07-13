import unittest

from dynamic_programming.max_independent_set import max_independent_set, max_independent_set_recursive


class TestMaxIndependentSet(unittest.TestCase):

    def test_max_independent_sets(self):
        first = [1, 2, 3, 4]
        mem = {}

        self.assertEqual(max_independent_set(first), max_independent_set_recursive(first, len(first) - 1, mem))
        self.assertEqual(max_independent_set(first), 6)
        self.assertEqual(max_independent_set_recursive(first, len(first) - 1, mem), 6)

        second = [1, 2, 3, 4, 9, 8, 8, 8, 9, 10, 11, 40, 67]
        mem = {}
        self.assertEqual(max_independent_set(second), max_independent_set_recursive(second, len(second) - 1, mem))
