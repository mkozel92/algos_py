import unittest

from recursion.squashable_words import is_squashable


class TestIsSquashable(unittest.TestCase):

    def setUp(self):
        self.the_dictionary = {'hello', 'hell', 'hel', 'hl', 'l', 'a'}

    def test_squashable_words(self):
        self.assertTrue(is_squashable('hello', self.the_dictionary, {}))
        self.assertTrue(is_squashable('hel', self.the_dictionary, {}))
        self.assertTrue(is_squashable('a', self.the_dictionary, {}))

    def test_non_squashable_words(self):
        self.assertFalse(is_squashable('hellob', self.the_dictionary, {}))
        self.assertFalse(is_squashable('ghel', self.the_dictionary, {}))
        self.assertFalse(is_squashable('c', self.the_dictionary, {}))
