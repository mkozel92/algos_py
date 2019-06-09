

class Edge(object):
    """implementation of weighted graph edge"""

    def __init__(self, v_1: int, v_2: int, weight: float):
        """
        initialize edge with adjacent vertices and weight
        :param v_1: first vertex
        :param v_2: second vertex
        :param weight: weight of edge
        """
        self.v_1 = v_1
        self.v_2 = v_2
        self.weight = weight

    def either(self) -> int:
        """
        :return: a vertex adjacent to this edge
        """
        return self.v_1

    def other(self, v: int) -> int:
        """
        :param v: a vertex_adjacent to this edge
        :return: other vertex than v
        """
        assert(v == self.v_1 or v == self.v_2)

        if self.v_1 == v:
            return self.v_2
        return self.v_1

    def __lt__(self, other: 'Edge'):
        return self.weight < other.weight

    def __le__(self, other: 'Edge'):
        return self.weight <= other.weight

    def __gt__(self, other: 'Edge'):
        return self.weight > other.weight

    def __ge__(self, other: 'Edge'):
        return self.weight >= other.weight

    def __eq__(self, other: 'Edge'):
        return self.weight == other.weight

    def __ne__(self, other: 'Edge'):
        return self.weight != other.weight


class DirectedEdge(object):
    """implementation of weighted graph directed edge"""

    def __init__(self, from_: int, to_: int, weight: float):
        """
        initialize edge with adjacent vertices and weight
        :param from_: first vertex
        :param to_: second vertex
        :param weight: weight of edge
        """
        self.from_ = from_
        self.to_ = to_
        self.weight = weight

    def from_vertex(self) -> int:
        """
        :return: from vertex adjacent to this edge
        """
        return self.from_

    def to_vertex(self) -> int:
        return self.to_

    def __lt__(self, other: 'Edge'):
        return self.weight < other.weight

    def __le__(self, other: 'Edge'):
        return self.weight <= other.weight

    def __gt__(self, other: 'Edge'):
        return self.weight > other.weight

    def __ge__(self, other: 'Edge'):
        return self.weight >= other.weight

    def __eq__(self, other: 'Edge'):
        return self.weight == other.weight

    def __ne__(self, other: 'Edge'):
        return self.weight != other.weight
