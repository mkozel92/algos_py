from data_structures.data_structure_interfaces import Stack
from data_structures.linked_list_stack import LinkedListStack
from graphs.graph_interface import Digraph


class StrongComponents(object):
    """class to compute connected components of given graph"""

    def __init__(self, g: Digraph):
        """
        init with a graph
        :param g: Graph
        """
        self.g = g
        self.visited = [False] * self.g.get_size()
        self.vertex_group = [0] * self.g.get_size()

    def dfs(self, g: Digraph, v: int, group: int, a_stack: Stack):
        """
        dfs to mark components from the same group
        Complexity O(E + V)
        :param g: a graph to process
        :param v: starting vertex
        :param group: current group number
        :param a_stack: keeps post order
        """
        if self.visited[v]:
            return
        self.visited[v] = True
        self.vertex_group[v] = group

        for vertex in g.adj(v):
            self.dfs(g, vertex, group, a_stack)
        a_stack.push(v)

    def compute(self):
        """
        Assign each vertex to a strong component
        """
        a_stack = LinkedListStack()
        rg = self.g.reverse()
        for i in range(len(self.visited)):
            if not self.visited[i]:
                self.dfs(rg, i, 0, a_stack)

        group = 0
        self.visited = [False] * self.g.get_size()
        for i in a_stack:
            if not self.visited[i]:
                self.dfs(self.g, i, group, LinkedListStack())
                group += 1

    def is_connected(self, p: int, q: int) -> bool:
        """
        check if two vertices are in the same component
        :param p: a vertex
        :param q: a vertex
        :return: True of the vertices are connected
        """
        assert (0 <= p < self.g.get_size())
        assert (0 <= q < self.g.get_size())

        return self.vertex_group[p] == self.vertex_group[q]
