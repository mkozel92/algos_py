from collections import defaultdict


def is_palindrome_permutation(a_string: str) -> bool:
    """
    check if given string is a permutation of a palindrome
    complexity O(N)
    :param a_string: string to check
    :return: True if given string is a permutation of a palindrome
    """
    count_dict = defaultdict(int)
    for char in a_string:
        count_dict[char] += 1

    num_odd = 0
    for key in count_dict.keys():
        if count_dict[key] % 2 == 1:
            num_odd += 1
        if num_odd > 1:
            return False
    return True
