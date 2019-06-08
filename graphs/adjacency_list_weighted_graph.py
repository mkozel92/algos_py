from graphs.graph_interface import WeightedGraph


class ALWGraph(WeightedGraph):
    """graph represented by adjacency list"""

    def __init__(self, num_v):
        """
        init graph by number of vertices
        :param num_v:  num of vertices in the graph
        """
        self.v = num_v
        self.data = [set() for _ in range(self.v)]

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

        e = Edge(v_1, v_2, weight)
        self.data[v_1].add(e)
        self.data[v_2].add(e)

    def adj(self, v_1: int) -> set:
        """
        return set of vertices adjacent to v_1
        complexity O(N)
        :param v_1: a vertex
        :return: set of vertices adjacent to v_1
        """
        assert (0 <= v_1 < self.v)
        return set([e.other(v_1) for e in self.data[v_1]])

    def get_size(self):
        """
        :return: number of vertices in the graph
        """
        return self.v
