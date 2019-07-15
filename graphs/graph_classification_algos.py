from graphs.adjacency_list_digraph import ALDigraph
from graphs.adjacency_list_graph import ALGraph


def is_bipartite(a_vertex: int, a_graph: ALGraph, current_group: int, assigned_group: list) -> bool:
    """
    check if graph is bipartite
    Complexity O(E + V)
    :param a_vertex: currently processed vertex
    :param a_graph: a graph to check
    :param current_group: group of current vertex
    :param assigned_group: assigned groups
    :return: True if graph is bipartite
    """
    if assigned_group[a_vertex] == -1:
        assigned_group[a_vertex] = current_group
    elif assigned_group[a_vertex] != current_group:
        return False
    else:
        return True

    for v in a_graph.adj(a_vertex):
        if not is_bipartite(v, a_graph, (current_group + 1) % 2, assigned_group):
            return False

    return True


def has_cycle(a_vertex: int, a_graph: ALDigraph, currently_processed: set, visited: list) -> bool:
    """
    check if given graph has a cycle
    complexity O (E + V)
    :param a_vertex: currently processed vertex
    :param a_graph: graph to check
    :param currently_processed: set of currently processed vertices
    :param visited: list of visited vertices
    :return: True if graph has a cycle
    """
    if visited[a_vertex]:
        if a_vertex in currently_processed:
            return True
        else:
            return False

    visited[a_vertex] = True
    currently_processed.add(a_vertex)

    for v in a_graph.adj(a_vertex):
        if has_cycle(v, a_graph, currently_processed, visited):
            return True

    currently_processed.remove(a_vertex)
    return False


def has_euler_path(a_graph: ALGraph):
    """
    check if graph has an Euler Tour
    :param a_graph: graph to check
    :return: True if the graph has an Euler tour
    """
    for edges in a_graph.data:
        if len(edges) % 2 == 1:
            return False
    return True

