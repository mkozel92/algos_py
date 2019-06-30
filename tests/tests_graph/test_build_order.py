import unittest

from graphs.build_order import build_order


class TestBuildOrder(unittest.TestCase):

    def setUp(self) -> None:
        self.projects = [0, 1, 2, 3, 4, 5]
        self.dependencies = [(0, 3), (5, 1), (1, 3), (5, 0), (3, 2), (1, 0), (3, 2)]
        self.correct_order = [5, 4, 1, 0, 3, 2]

    def test_build_order(self):
        stack = build_order(self.projects, self.dependencies)
        i = 0
        while stack.is_empty():
            self.assertEqual(stack.pop(), self.correct_order[i])
