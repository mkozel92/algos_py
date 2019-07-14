import unittest

from search.search_matrix import search_matrix, search_matrix_parallel


class TestSearchMatrix(unittest.TestCase):

    def setUp(self) -> None:
        self.matrix = [[1, 2, 3, 4, 5],
                       [6, 7, 8, 9, 10],
                       [11, 12, 13, 14, 15],
                       [16, 17, 18, 19, 22],
                       [25, 28, 31, 55, 70],
                       [27, 29, 44, 71, 100]]

    def test_search_matrix(self):
        for i in range(101):
            self.assertEqual(search_matrix(i, self.matrix),
                             search_matrix_parallel(i, self.matrix))