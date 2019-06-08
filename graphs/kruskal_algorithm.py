from dynamic_connectivity.weighted_quick_union import WeightedQuickUnion
from graphs.graph_interface import WeightedGraph


def kruskal(a_graph: WeightedGraph) -> list:
    """
    kruskal algorithm to compute mst of a graph
    1. sort edges by weights O(E log E)
    2. for each edge try to add the edge to mst
       but add only if the new edge would not create a cycle.
       A cycle is created when the new edge connects two
       already connected vertices.
       We can keep track of this using Quick union algo.
       O(E log E) ..for each edge E check QU if connected (log E)
       and if not add to mst and connect in QU (log E)
    complexity (E log E)
    :param a_graph: a graph
    :return: list containing mst edges
    """
    edges = list(a_graph.get_edges())
    edges.sort()
    mst = list()

    wqu = WeightedQuickUnion(len(edges))

    for edge in edges:
        v_1 = edge.either()
        v_2 = edge.other(v_1)

        if not wqu.connected(v_1, v_2):
            wqu.union(v_1, v_2)
            mst.append(edge)

    return mst
