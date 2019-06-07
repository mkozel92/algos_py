from typing import Iterable
from graphs.graph_interface import Graph


class AMGraph(Graph):
    """graph represented by adjacency matrix"""

    def __init__(self, num_v: int):
        """
        initialize graph by vertex size
        :param num_v: num of vertices in the graph
        """
        self.v = num_v
        self.graph = [[0] * v] * v

    def add_edge(self, p: int, q: int):
        """
        add edge to the graph between given vertices
        complexity O(1)
        :param p: first vertex
        :param q: second vertex
        """
        assert (p < self.v)
        assert (q < self.v)

        self.graph[p][q] = 1
        self.graph[q][p] = 1

    def adj(self, v) -> Iterable:
        """
        return set of vertices adjacent to given vertex
        complexity O(V)
        :param v: a vertex
        :return: set of vertices adjacent to v
        """
        assert (v < self.v)
        adjacent_vertices = set()
        for i in range(self.v):
            if self.graph[v][i] == 1:
                adjacent_vertices.add(i)
        return adjacent_vertices

    def get_size(self):
        """
        :return: number of vertices in the graph
        """
        return self.v
