import unittest

from misc.path_in_grid import path_in_grid


class TestPathInGrid(unittest.TestCase):

    def setUp(self) -> None:
        self.impossible = [[0, 0, 0, -1, 0],
                           [0, -1, 0, -1, 0],
                           [0, 0, 0, -1, 0],
                           [0, 0, 0, -1, 0],
                           [0, 0, 0, -1, 0]]

        self.possible = [[0, 0, 0, -1, 0],
                         [0, -1, 0, 0, 0],
                         [0, 0, 0, -1, 0],
                         [0, 0, 0, -1, 0],
                         [0, 0, 0, -1, 0]]

    def test_path_in_grid(self):
        self.assertEqual(path_in_grid(self.impossible), [])
        self.assertEqual(len(path_in_grid(self.possible)), 8)
