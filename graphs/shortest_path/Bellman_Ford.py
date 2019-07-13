from graphs.graph_interface import WeightedDigraph


def relax(v: int, a_graph: WeightedDigraph, changes: set, distances: list, edge_to: list):
    """
    relax given vertex
    :param v: vertex to relax
    :param a_graph: graph to process
    :param changes: keep track of updated vertices
    :param distances: distances to vertices
    :param edge_to: paths to vertices
    """
    for edge in a_graph.adj(v):
        if distances[v] + edge.weight < distances[edge.to_vertex()]:
            distances[edge.to_vertex()] = distances[v] + edge.weight
            edge_to[edge.to_vertex()] = v
            changes.add(edge.to_vertex())


def bellman_ford(a_graph: WeightedDigraph, distances: list, edge_to: list):
    """
    Bellman ford algo to find shortest path
    complexity O(EV)
    :param a_graph: graph to search
    :param distances: distances to vertices
    :param edge_to: paths to vertices
    """
    changes = {0}

    while len(changes):
        new_changes = set()
        for v in changes:
            relax(v, a_graph, new_changes, distances, edge_to)
        changes = new_changes.copy()
