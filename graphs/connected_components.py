from graphs.graph_interface import Graph


class ConnectedComponents(object):
    """class to compute connected components of given graph"""

    def __init__(self, g: Graph):
        """
        init with a graph
        :param g: Graph
        """
        self.g = g
        self.visited = [False] * self.g.v
        self.vertex_group = [0] * self.g.v

    def dfs(self, v: int, group: int):
        """
        dfs to mark components from the same group
        Complexity O(E + V)
        :param v: starting vertex
        :param group: current group number
        """
        if self.visited[v]:
            return
        self.visited[v] = True
        self.vertex_group[v] = group

        for vertex in self.g.adj(v):
            self.dfs(vertex, group)

    def compute(self):
        """
        Assign each vertex to a connected component
        """
        group = 0
        for i in range(len(self.visited)):
            if not self.visited[i]:
                self.dfs(i, group)
                group += 1

    def is_connected(self, p: int, q: int) -> bool:
        """
        check if two vertices are in the same component
        :param p: a vertex
        :param q: a vertex
        :return: True of the vertices are connected
        """
        assert (p < self.g.v)
        assert (q < self.g.v)

        return self.vertex_group[p] == self.vertex_group[q]
