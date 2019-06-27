import unittest

from misc.palindrome_permutation import is_palindrome_permutation


class TestPalindromePermutation(unittest.TestCase):

    def setUp(self) -> None:

        self.is_pp = 'tactcoa'
        self.not_pp = 'tactcoaq'

    def test_palindrome_permutation(self):
        self.assertTrue(is_palindrome_permutation(self.is_pp))
        self.assertFalse(is_palindrome_permutation(self.not_pp))
