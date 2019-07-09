import unittest

from recursion.power_set import power_set_recursive, power_set


class TestPowerSet(unittest.TestCase):

    def test_power_set(self):
        self.assertEqual(len(power_set_recursive([1, 2, 3], 0)), 8)
        self.assertEqual(len(power_set_recursive([1, 2, 3, 4], 0)), 16)
        self.assertEqual(len(power_set_recursive([1, 2, 3, 4, 5], 0)), 32)

        self.assertEqual(len(power_set([1, 2, 3])), 8)
        self.assertEqual(len(power_set([1, 2, 3, 4])), 16)
        self.assertEqual(len(power_set([1, 2, 3, 4, 5])), 32)

    def test_compare(self):
        self.assertEqual(power_set([1, 2, 3, 4, 5]).sort(), power_set_recursive([1, 2, 3, 4, 5], 0).sort())
