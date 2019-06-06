import unittest

from graphs.adjacency_list_graph import ALGraph
from graphs.depth_first_search import dfs_iterative, dfs_recursive


class TestDFS(unittest.TestCase):

    def setUp(self) -> None:
        self.g = ALGraph(10)
        self.g.add_edge(0, 1)
        self.g.add_edge(0, 5)
        self.g.add_edge(0, 7)
        self.g.add_edge(7, 9)
        self.g.add_edge(7, 8)
        self.g.add_edge(3, 2)
        self.g.add_edge(5, 3)

    def test_dfs_implementations(self):
        visited_i = [False] * 10
        visited_from_i = [-1] * 10
        dfs_iterative(self.g, 0, visited_i, visited_from_i)

        visited_r = [False] * 10
        visited_from_r = [-1] * 10
        dfs_recursive(self.g, 0, visited_r, visited_from_r, -1)

        self.assertEqual(visited_i, visited_r)
        self.assertEqual(visited_from_i, visited_from_r)
