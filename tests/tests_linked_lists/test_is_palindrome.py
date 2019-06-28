import unittest

from linked_lists.is_palindrome import is_palindrome
from linked_lists.linked_list import LinkedList


class TestIsPalindrome(unittest.TestCase):

    def setUp(self) -> None:
        self.palindrome = LinkedList()
        self.palindrome_2 = LinkedList()
        self.not_palindrome = LinkedList()

        self.palindrome.insert_many([1, 2, 3, 3, 2, 1])
        self.palindrome_2.insert_many([1, 2, 3, 2, 1])
        self.not_palindrome.insert_many([1, 5, 2, 3, 2, 1])

    def test_palindromes(self):
        self.assertTrue(is_palindrome(self.palindrome))
        self.assertTrue(is_palindrome(self.palindrome_2))
        self.assertFalse(is_palindrome(self.not_palindrome))