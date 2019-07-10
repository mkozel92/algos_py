import unittest

from dynamic_programming.coins import coins


class TestCoins(unittest.TestCase):

    def test_coins(self):
        self.assertEqual(coins([1], 10), 1)
        self.assertEqual(coins([1, 5], 10), 3)
        self.assertEqual(coins([1, 4, 5], 10), 6)