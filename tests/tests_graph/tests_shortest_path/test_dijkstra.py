import unittest

from graphs.adjacency_list_weighted_digraph import ALWDigraph
from graphs.shortest_path.dijkstra import dijkstra


class TestDijkstra(unittest.TestCase):

    def setUp(self) -> None:
        self.g = ALWDigraph(10)
        self.g.add_edge(0, 1, 10)
        self.g.add_edge(0, 2, 10)
        self.g.add_edge(2, 3, 5)
        self.g.add_edge(0, 5, 10)
        self.g.add_edge(5, 3, 1)
        self.g.add_edge(3, 9, 1)
        self.g.add_edge(0, 9, 13)

    def test_dijkstr(self):
        dists = [0.0] + [float('Inf')] * 9
        e_from = [-1] * 10

        dijkstra(self.g, dists, e_from)
        self.assertEqual(dists, [0, 10, 10, 11, float('Inf'), 10, float('Inf'), float('Inf'), float('Inf'), 12])
