def same_diagonal(pos_1: int, pos_2: int):
    """
    check if two position share the same diagonal
    :param pos_1: first position
    :param pos_2: second position
    :return: true if share same diagonal
    """
    row_1 = pos_1 // 8
    col_1 = pos_1 % 8

    row_2 = pos_2 // 8
    col_2 = pos_2 % 8

    row_2_rev = 8 - pos_2 // 8
    row_1_rev = 8 - pos_1 // 8

    if row_1 - col_1 == row_2 - col_2:
        return True
    if row_1_rev - col_1 == row_2_rev - col_2:
        return True
    return False


def place_queen(place: int, available_places: set) -> set:
    """
    return all new available places after placing a queen at given position
    :param place: place new queen here
    :param available_places: current available positions
    :return: remaining available positions
    """
    new_available_places = set()
    for p in available_places:
        if p % 8 != place % 8 and p // 8 != place // 8 and not same_diagonal(p, place):
            new_available_places.add(p)
    return new_available_places


def eight_queens(queens_to_place: int, available_places: set, mem_dict: dict):
    """
    count ways to place 8 queens on a chess board
    complexity O(8^N)
    :param queens_to_place: remaining queens to place
    :param available_places: set of available places
    :param mem_dict: memoized results
    :return: num of possible ways
    """
    if not len(available_places) and queens_to_place > 0:
        return 0

    if queens_to_place == 0:
        return 1

    if (queens_to_place, str(available_places)) in mem_dict:
        return mem_dict[(queens_to_place, str(available_places))]

    count = 0
    for place in available_places:
        if place // 8 != queens_to_place - 1:
            continue
        new_places = place_queen(place, available_places)
        count += eight_queens(queens_to_place - 1, new_places, mem_dict)

    mem_dict[(queens_to_place, str(available_places))] = count
    return count
