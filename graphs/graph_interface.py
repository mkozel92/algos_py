from abc import ABC, abstractmethod


class Graph(ABC):
    """interface for graph implementations"""

    @abstractmethod
    def adj(self, v: int) -> set:
        """
        return set of adjacent vertices to a given vertex
        :param v: a vertex
        """
        pass

    @abstractmethod
    def add_edge(self, v_1: int, v_2: int):
        """
        add new edge connecting given vertices
        :param v_1: first vertex
        :param v_2: second vertex
        """
        pass

    def get_size(self):
        """
        return number of vertices in the graph
        """
        pass


class Digraph(ABC):
    """interface for directed graph"""

    @abstractmethod
    def adj(self, v: int) -> set:
        """
        return set of adjacent vertices to a given vertex
        :param v: a vertex
        """
        pass

    @abstractmethod
    def add_edge(self, v_1: int, v_2: int):
        """
        add new edge connecting given vertices
        :param v_1: first vertex
        :param v_2: second vertex
        """
        pass

    def get_size(self):
        """
        return number of vertices in the graph
        """
        pass

    def reverse(self) -> 'Digraph':
        """
        return a digraph with reversed edges
        """
        pass


class WeightedGraph(ABC):
    """interface for weighted graph"""

    @abstractmethod
    def adj(self, v: int) -> set:
        """
        return set of adjacent vertices to a given vertex
        :param v: a vertex
        """
        pass

    @abstractmethod
    def add_edge(self, v_1: int, v_2: int, weight: float):
        """
        add new edge connecting given vertices
        :param v_1: first vertex
        :param v_2: second vertex
        :param weight: weight of the edge
        """
        pass

    def get_size(self):
        """
        return number of vertices in the graph
        """
        pass
