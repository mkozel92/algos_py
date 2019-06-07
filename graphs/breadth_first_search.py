from data_structures.linked_list_queue import LinkedListQueue
from graphs.graph_interface import Graph


def bfs_iterative(g: Graph, v: int, visited: list, visited_from: list):
    """
    iterative bfs implementation
    complexity O(E + V)
    :param g: graph
    :param v: starting vertex
    :param visited: list of visited vertices
    :param visited_from: list keeping track of paths to the vertices
    """
    q = LinkedListQueue()
    q.enqueue(v)
    visited[v] = True
    visited_from[v] = -1
    while not q.is_empty():
        current_vertex = q.dequeue()
        for vertex in g.adj(current_vertex):
            if not visited[vertex]:
                visited[vertex] = True
                q.enqueue(vertex)
                visited_from[vertex] = current_vertex
