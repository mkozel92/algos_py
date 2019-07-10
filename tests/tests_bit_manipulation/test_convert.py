import unittest

from bit_manipulation.conversion import convert


class TestConvert(unittest.TestCase):

    def test_convert(self):
        self.assertEqual(convert(8, 7), 4)
        self.assertEqual(convert(8, 4), 2)
        self.assertEqual(convert(8, 8), 0)
