from data_structures.linked_list_queue import LinkedListQueue


def get_adjacent(current: tuple, a_grid: list) -> list:
    """
    get adjacent accessible neighbours in given grid
    :param current: current location
    :param a_grid: a grid
    :return: list of accessible neighbours
    """
    row = current[0]
    col = current[1]

    result = []
    if row + 1 < len(a_grid) and a_grid[row + 1][col] != -1:
        result.append((row + 1, col))
    if col + 1 < len(a_grid[0]) and a_grid[row][col + 1] != -1:
        result.append((row, col + 1))
    return result


def path_in_grid(a_grid: list) -> list:
    """
    find path in a grid with obstacles
    complexity O(MN)
    :param a_grid: grid to search
    :return: path to the end
    """
    queue = LinkedListQueue()
    paths = {(0, 0): (0, 0)}
    visited = set()

    queue.enqueue((0, 0))
    visited.add((0, 0))
    while not queue.is_empty():
        current = queue.dequeue()
        for adj in get_adjacent(current, a_grid):
            if adj not in visited:
                queue.enqueue(adj)
                visited.add(adj)
                paths[adj] = current

    path = []
    current = (len(a_grid) - 1, len(a_grid[0]) - 1)
    if current not in paths:
        return []

    while paths[current] != current:
        path.append(paths[current])
        current = paths[current]

    path.reverse()
    return path
