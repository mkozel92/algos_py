from typing import Set


def get_permutations(a_string: str) -> Set:
    """
    gets sets of all the permutations of given string
    complexity O(N!)
    :param a_string: input string
    :return: set of unique permutations of the input string
    """
    if len(a_string) == 1:
        return set(a_string)

    perm_set = set()
    for c in a_string:
        new_string = a_string.replace(c, '', 1)
        for perm in get_permutations(new_string):
            perm_set.add(c + perm)
    return perm_set
