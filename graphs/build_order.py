from data_structures.data_structure_interfaces import Stack
from data_structures.linked_list_stack import LinkedListStack
from graphs.adjacency_list_digraph import ALDigraph
from graphs.graph_interface import Digraph


def top_sort(a_graph: Digraph, a_stack: Stack, visited: list, vertex: int):
    """
    topologically sort given graph
    :param a_graph: a graph to sort
    :param a_stack: stack to store sorted vertices
    :param visited: list of visited vertices
    :param vertex: current vertex to process
    """
    if visited[vertex]:
        return
    visited[vertex] = True
    for v in a_graph.adj(vertex):
        top_sort(a_graph, a_stack, visited, v)
    a_stack.push(vertex)


def build_order(projects: list, dependencies: list) -> Stack:
    """
    find build order given list of project and their dependencies
    :param projects: project to sort
    :param dependencies: project dependencies
    :return: sorted project in a stack
    """
    graph = ALDigraph(len(projects))
    a_stack = LinkedListStack()
    visited = [False] * len(projects)
    for d in dependencies:
        graph.add_edge(d[0], d[1])
    for i in range(len(visited)):
        if not visited[i]:
            top_sort(graph, a_stack, visited, i)
    return a_stack
