from graphs.edge import DirectedEdge
from graphs.graph_interface import WeightedDigraph


class ALWDigraph(WeightedDigraph):
    """graph represented by adjacency list"""

    def __init__(self, num_v):
        """
        init graph by number of vertices
        :param num_v:  num of vertices in the graph
        """
        self.v = num_v
        self.edges = list()
        self.data = [list() for _ in range(self.v)]

    def add_edge(self, v_1: int, v_2: int, weight: float):
        """
        add weighted edge between vertices v_1 and v_2
        complexity O(1)
        :param v_1: a vertex
        :param v_2: a vertex
        :param weight: weight of the edge
        """
        assert (0 <= v_1 < self.v)
        assert (0 <= v_2 < self.v)

        e = DirectedEdge(v_1, v_2, weight)
        self.data[v_1].append(e)
        self.edges.append(e)

    def adj(self, v_1: int) -> list:
        """
        return set of edges adjacent to v_1
        complexity O(1)
        :param v_1: a vertex
        :return: set of vertices adjacent to v_1
        """
        assert (0 <= v_1 < self.v)
        return self.data[v_1]

    def get_size(self):
        """
        :return: number of vertices in the graph
        """
        return self.v

    def get_edges(self) -> list:
        """
        :return: set of all edges in the graph
        """
        return self.edges
