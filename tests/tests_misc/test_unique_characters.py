import unittest

from misc.unique_characters import has_unique_chars, has_unique_inplace


class TestUniqueChars(unittest.TestCase):

    def setUp(self) -> None:
        self.u_string = "abcdef"
        self.n_string = "abcda"

    def test_unique_chars(self):
        self.assertTrue(has_unique_chars(self.u_string))
        self.assertTrue(has_unique_inplace(self.u_string))

        self.assertFalse(has_unique_chars(self.n_string))
        self.assertFalse(has_unique_inplace(self.n_string))
