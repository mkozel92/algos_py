from data_structures.linked_list_stack import LinkedListStack
from graphs.graph_interface import Graph


def dfs_recursive(g: Graph, v: int, visited: list, visited_from: list, from_: int):
    """
    recursive dfs implementation
    complexity O(E + V)
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
        dfs_recursive(g, vertex, visited, visited_from, v)


def dfs_iterative(g: Graph, v: int, visited: list, visited_from: list):
    """
    iterative dfs implementation
    complexity O(E + V)
    :param g: graph
    :param v: starting vertex
    :param visited: list of visited vertices
    :param visited_from: list keeping track of paths to the vertices
    """
    s = LinkedListStack()
    s.push(v)
    visited[v] = True
    visited_from[v] = -1
    while not s.is_empty():
        current_vertex = s.pop()
        for vertex in g.adj(current_vertex):
            if not visited[vertex]:
                visited[vertex] = True
                s.push(vertex)
                visited_from[vertex] = current_vertex
