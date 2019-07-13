from data_structures.binary_heap import BinaryHeap
from graphs.edge import DirectedEdge
from graphs.graph_interface import WeightedDigraph


def relax(edge: DirectedEdge, mh: BinaryHeap, distances: list, edge_to: list):
    """
    relax edge of a graph -> update distance to a vertex if we found shorter path
    save this path to edge_from list
    :param edge: edge to relax
    :param mh: min heap that keeps closest unexplored vertices
    :param distances: list of current best distances to every vertex
    :param edge_to: list keeping track of paths to vertices
    """

    from_ = edge.from_vertex()
    to_ = edge.to_vertex()

    if distances[from_] + edge.weight < distances[to_]:
        distances[to_] = distances[from_] + edge.weight
        edge_to[to_] = edge
        mh.insert((distances[to_], to_))


def dijkstra(a_graph: WeightedDigraph, distances: list, edge_to: list):
    """
    Dijkstra algo for shortest path in acyclic graph
    complexity O((E + V) log V) for every vertex V remove from binary heap (log V) and for every
    edge E push to binary heap (log V)
    :param a_graph: graph to process
    :param distances: distances to all vertices
    :param edge_to: paths to all vertices
    """
    mh = BinaryHeap()
    mh.insert((0, 0))
    visited = [False] * len(distances)

    while not mh.is_empty():
        distance, vertex = mh.remove()
        if visited[vertex]:
            continue
        for edge in a_graph.adj(vertex):
            relax(edge, mh, distances, edge_to)
        visited[vertex] = True


