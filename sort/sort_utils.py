from typing import Any


def less(element_a: Any, element_b: any) -> bool:
    """
     compares two elements
    :param element_a: the first element
    :param element_b: the second element
    :return: True if the first element is strictly lower the the second element
    """
    return element_a < element_b


def swap(a_list: list, first_index: int, second_index: int):
    """
    swaps elements in a list on given indices

    :param a_list: a list in which we perform the swaps
    :param first_index: index of first element
    :param second_index: index of second element
    """
    a_list[first_index], a_list[second_index] = a_list[second_index], a_list[first_index]
