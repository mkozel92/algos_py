import unittest

from misc.is_permutation import is_permutation


class TestPermutation(unittest.TestCase):

    def setUp(self) -> None:
        self.a_string = 'this is some string'
        self.permutation_string = 'this some is trsing'
        self.non_permutation_string = 'thix is some string'

    def test_permutation(self):
        self.assertTrue(is_permutation(self.a_string, self.permutation_string))
        self.assertFalse(is_permutation(self.a_string, self.non_permutation_string))
