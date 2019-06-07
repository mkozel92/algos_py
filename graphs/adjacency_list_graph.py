from graphs.graph_interface import Graph


class ALGraph(Graph):
    """graph represented by adjacency list"""

    def __init__(self, num_v):
        """
        init graph by number of vertices
        :param num_v:  num of vertices in the graph
        """
        self.v = num_v
        self.data = [set() for _ in range(self.v)]

    def add_edge(self, p: int, q: int):
        """
        add edge between vertices p and q
        complexity O(1)
        :param p: a vertex
        :param q: a vertex
        """
        assert (p < self.v)
        assert (q < self.v)

        self.data[p].add(q)
        self.data[q].add(p)

    def adj(self, p):
        """
        return set of vertices adjacent to p
        complexity O(1)
        :param p: a vertex
        :return: set of vertices adjacent to p
        """
        assert (p < self.v)
        return self.data[p]
