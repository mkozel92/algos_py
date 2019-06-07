from data_structures.data_structure_interfaces import Stack
from graphs.graph_interface import Digraph


def recursive_topological_sort(graph: Digraph, vertex: int, a_stack: Stack, visited: list):
    """
    recursive dfs that put all processed vertices on stack
    complexity O(N)
    :param graph: a graph to sort
    :param vertex: starting vertex
    :param a_stack: stack to store topologically ordered vertices
    :param visited: a list of visited vertices
    """
    if visited[vertex]:
        return
    visited[vertex] = True
    for v in graph.adj(vertex):
        recursive_topological_sort(graph, v, a_stack, visited)
    a_stack.push(vertex)


def topological_sort(graph: Digraph, a_stack: Stack):
    """
    store graph vertices on a given stack in topological order
    :param graph: a graph to sort
    :param a_stack: a stack to keep topological sorted vertices
    """
    visited = [False] * graph.get_size()
    for i in range(graph.get_size()):
        if not visited[i]:
            recursive_topological_sort(graph, i, a_stack, visited)
