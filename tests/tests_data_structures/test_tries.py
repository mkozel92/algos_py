import unittest

from data_structures.r_way_trie import RWayTrie
from data_structures.ternary_search_trie import TernarySearchTrie


class TestTries(unittest.TestCase):

    def setUp(self) -> None:
        self.trie = RWayTrie(256)
        self.tst = TernarySearchTrie()
        self.data_list = ["hello", "hell", "hellos", "hallow", "something", "else"]

    def test_r_way_trie(self):
        for i, e in enumerate(self.data_list):
            self.trie.put(e, i)

        for i, e in enumerate(self.data_list):
            self.assertEqual(self.trie.get(e), i)

        self.assertIsNone(self.trie.get("notThere"))

    def test_ternary_search_trie(self):
        for i, e in enumerate(self.data_list):
            self.tst.put(e, i)

        for i, e in enumerate(self.data_list):
            self.assertEqual(self.tst.get(e), i)

        self.assertIsNone(self.tst.get("notThere"))
