import unittest

from itertools import permutations
from recursion.permutations import get_permutations


class TestPermutations(unittest.TestCase):

    def setUp(self) -> None:
        self.string_1 = 'hello'
        self.string_2 = 'something'
        self.perms_1 = set([''.join(x) for x in permutations(self.string_1)])
        self.perms_2 = set([''.join(x) for x in permutations(self.string_2)])

    def test_permutations(self):
        perms_1 = get_permutations(self.string_1)
        perms_2 = get_permutations(self.string_2)
        self.assertEqual(len(perms_1), len(self.perms_1))
        self.assertEqual(len(perms_2), len(self.perms_2))
        self.assertEqual(perms_1, self.perms_1)
        self.assertEqual(perms_2, perms_2)
