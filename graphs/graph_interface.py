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
