import unittest

from graphs.adjacency_list_weighted_graph import ALWGraph
from graphs.prim_algorithm import prim


class TestPrim(unittest.TestCase):

    def setUp(self) -> None:
        self.g = ALWGraph(5)
        self.g.add_edge(0, 1, 100)
        self.g.add_edge(1, 2, 6)
        self.g.add_edge(2, 3, 7)
        self.g.add_edge(3, 4, 8)
        self.g.add_edge(4, 1, 9)
        self.g.add_edge(3, 2, 10)
        self.g.add_edge(0, 4, 11)
        self.g.add_edge(0, 2, 12)

    def test_prim(self):
        mst = prim(self.g)
        mst_edges = []
        for x in mst:
            a = x.either()
            b = x.other(a)
            mst_edges.append((a, b))
        self.assertEqual(mst_edges, [(0, 4), (3, 4), (2, 3), (1, 2)])
