import unittest

from graphs.adjacency_list_graph import ALGraph
from graphs.connected_components import ConnectedComponents


class TestConnectedComponents(unittest.TestCase):

    def setUp(self) -> None:
        self.g = ALGraph(10)
        self.g.add_edge(0, 1)
        self.g.add_edge(0, 5)
        self.g.add_edge(0, 7)
        self.g.add_edge(7, 9)
        self.g.add_edge(7, 8)
        self.g.add_edge(3, 2)
        self.g.add_edge(5, 3)

        self.cc = ConnectedComponents(self.g)
        self.cc.compute()

    def test_connected_components(self):
        self.assertTrue(self.cc.is_connected(0, 1))
        self.assertTrue(self.cc.is_connected(0, 5))
        self.assertTrue(self.cc.is_connected(5, 7))
        self.assertTrue(self.cc.is_connected(2, 5))
        self.assertFalse(self.cc.is_connected(0, 4))
        self.assertFalse(self.cc.is_connected(1, 4))
        self.assertFalse(self.cc.is_connected(6, 4))
        self.assertFalse(self.cc.is_connected(5, 6))
