import unittest

from linear_programming.simplex import solve_simplex


class TestSimplex(unittest.TestCase):

    def test_simplex(self):
        simplex_matrix = [[5, 15, 1, 0, 0, 480],
                          [4, 4, 0, 1, 0, 160],
                          [35, 20, 0, 0, 1, 1190],
                          [13, 23, 0, 0, 0, 0]]
        solve_simplex(simplex_matrix)
        self.assertAlmostEqual(simplex_matrix[3][5], -800)
        self.assertAlmostEqual(simplex_matrix[1][5], 28)
        self.assertAlmostEqual(simplex_matrix[2][5], 12)

