from collections import defaultdict


def is_permutation(first_string: str, second_string: str) -> bool:
    """
    check if two string are permutation of each other by keeping counts of chars
    complexity O(N)
    :param first_string: string to compare
    :param second_string: string to compare
    :return: True fi they are permutations
    """
    if len(first_string) != len(second_string):
        return false
    count_dict = defaultdict(int)

    for i in range(len(first_string)):
        count_dict[first_string[i]] += 1
        count_dict[second_string[i]] -= 1

    for key in count_dict.keys():
        if count_dict[key] != 0:
            return False

    return True