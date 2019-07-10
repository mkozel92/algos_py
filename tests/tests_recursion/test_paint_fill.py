import unittest

from recursion.paint_fill import paint_fill


class TestPaintFill(unittest.TestCase):

    def setUp(self) -> None:
        self.area = [[0, 0, 1, 0, 0, 0],
                     [0, 0, 1, 0, 0, 0],
                     [0, 0, 1, 0, 0, 0],
                     [0, 0, 1, 0, 0, 0],
                     [0, 0, 1, 0, 0, 0]]

    def test_paint_fill(self):
        paint_fill(self.area, 0, 0, 5)
        self.assertEqual(self.area, [[5, 5, 1, 0, 0, 0],
                                     [5, 5, 1, 0, 0, 0],
                                     [5, 5, 1, 0, 0, 0],
                                     [5, 5, 1, 0, 0, 0],
                                     [5, 5, 1, 0, 0, 0]])

        paint_fill(self.area, 0, 2, 0)
        self.assertEqual(self.area, [[5, 5, 0, 0, 0, 0],
                                     [5, 5, 0, 0, 0, 0],
                                     [5, 5, 0, 0, 0, 0],
                                     [5, 5, 0, 0, 0, 0],
                                     [5, 5, 0, 0, 0, 0]])

        paint_fill(self.area, 0, 2, 6)
        self.assertEqual(self.area, [[5, 5, 6, 6, 6, 6],
                                     [5, 5, 6, 6, 6, 6],
                                     [5, 5, 6, 6, 6, 6],
                                     [5, 5, 6, 6, 6, 6],
                                     [5, 5, 6, 6, 6, 6]])
