from random import randint

from sort.sort_utils import swap


def knuth_shuffle(a_list: list):
    """
    performs inplace knuth shuffle
    produces uniformly random permutation of the list
    complexity O(N)
    :param a_list: list to shuffle
    """
    for i in range(len(a_list)):
        j = randint(0, i + 1)
        swap(a_list, i, j)
