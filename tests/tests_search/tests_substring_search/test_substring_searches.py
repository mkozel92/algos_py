import unittest

from search.subsrting_search.brute_force import brute_force_search
from search.subsrting_search.knuth_morris_pratt import knuth_morris_pratt


class TestSubstringSearches(unittest.TestCase):

    def setUp(self) -> None:
        self.string_to_search = "this is some long string"
        self.pattern_1 = "string"
        self.pattern_2 = "so"
        self.pattern_3 = "not"

    def test_brute_force(self):
        self.assertEqual(brute_force_search(self.string_to_search, self.pattern_1), 18)
        self.assertEqual(brute_force_search(self.string_to_search, self.pattern_2), 8)
        self.assertEqual(brute_force_search(self.string_to_search, self.pattern_3), -1)

    def test_kmp(self):
        self.assertEqual(knuth_morris_pratt(self.string_to_search, self.pattern_1), 18)
        self.assertEqual(knuth_morris_pratt(self.string_to_search, self.pattern_2), 8)
        self.assertEqual(knuth_morris_pratt(self.string_to_search, self.pattern_3), -1)
