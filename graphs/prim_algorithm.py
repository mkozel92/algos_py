from data_structures.binary_heap import BinaryHeap
from graphs.graph_interface import WeightedGraph


def visit(v: int, mh: BinaryHeap, a_graph: WeightedGraph, visited: list):
    """
    visit a vertex as a helper function for Prim's algo
    :param v: a vertex
    :param mh: min heap of heap sorted edges
    :param a_graph: a graph to process
    :param visited: list of visited vertices
    """
    visited[v] = True
    for edge in a_graph.adj(v):
        other = edge.other(v)
        if not visited[other]:
            mh.insert(edge)


def prim(a_graph: WeightedGraph) -> list:
    """
    Prim's algo to compute mst
    builds mst by iteratively adding a shortest edge that has one
    vertex in current mst and the other outside of it
    complexity o(E log E) E times addition to minHeap + E time removal from minHeap
    :param a_graph: graph to process
    :return: list with mst edges
    """
    visited = [False] * a_graph.get_size()
    mst = list()
    mh = BinaryHeap()

    visit(0, mh, a_graph, visited)

    while not mh.is_empty():
        edge = mh.remove()
        w = edge.either()
        v = edge.other(w)
        if not visited[v] or not visited[w]:
            if not visited[v]:
                visit(v, mh, a_graph, visited)
            else:
                visit(w, mh, a_graph, visited)
            mst.append(edge)

    return mst
