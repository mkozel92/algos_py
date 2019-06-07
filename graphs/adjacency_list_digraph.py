from graphs.graph_interface import Digraph


class ALDigraph(Digraph):
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
        add directed edge between vertices p and q
        complexity O(1)
        :param p: a vertex
        :param q: a vertex
        """
        assert (p < self.v)
        assert (q < self.v)

        self.data[p].add(q)

    def adj(self, p):
        """
        return set of vertices adjacent to p
        complexity O(1)
        :param p: a vertex
        :return: set of vertices adjacent to p
        """
        assert (p < self.v)
        return self.data[p]

    def get_size(self):
        """
        :return: number of vertices in the graph
        """
        return self.v

    def reverse(self) -> Digraph:
        """
        :return: graph with reversed edges
        """
        new_graph = ALDigraph(self.get_size())
        for i in range(self.get_size()):
            for j in self.adj(i):
                new_graph.add_edge(j, i)
        return new_graph





