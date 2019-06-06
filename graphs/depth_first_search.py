from graphs.adjacency_list_graph import ALGraph


def dfs_paths(g: ALGraph, v: int, visited: list, visited_from: list, from_: int):
    """
    recursive dfs implementation
    :param g: graph
    :param v: starting vertex
    :param visited: list of visited vertices
    :param visited_from: list keeping track of paths to the vertices
    :param from_: from which vertex the recursive call comes from
    """
    if visited[v]:
        return
    visited[v] = True
    visited_from[v] = from_
    for vertex in g.adj(v):
        dfs_paths(g, vertex, visited, visited_from, v)
