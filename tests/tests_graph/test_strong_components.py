import unittest

from graphs.adjacency_list_digraph import ALDigraph
from graphs.strong_components import StrongComponents


class TestStrongComponents(unittest.TestCase):

    def setUp(self) -> None:
        self.a_gr = ALDigraph(10)
        self.a_gr.add_edge(1, 2)
        self.a_gr.add_edge(2, 3)
        self.a_gr.add_edge(3, 4)
        self.a_gr.add_edge(4, 1)
        self.a_gr.add_edge(4, 5)
        self.a_gr.add_edge(5, 6)
        self.a_gr.add_edge(6, 5)
        self.a_gr.add_edge(6, 7)

    def test_strong_components(self):
        sc = StrongComponents(self.a_gr)
        sc.compute()
        self.assertEqual(sc.vertex_group, [5, 4, 4, 4, 4, 3, 3, 2, 1, 0])
