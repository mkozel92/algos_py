import unittest

from recursion.power_set import power_set_recursive


class TestPowerSet(unittest.TestCase):

    def test_power_set(self):
        self.assertEqual(len(power_set_recursive([1, 2, 3], 0)), 8)
        self.assertEqual(len(power_set_recursive([1, 2, 3, 4], 0)), 16)
        self.assertEqual(len(power_set_recursive([1, 2, 3, 4, 5], 0)), 32)
