import unittest

from search.subsrting_search.brute_force import brute_force_search


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
