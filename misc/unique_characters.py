from collections import defaultdict


def has_unique_chars(a_string: str) -> bool:
    """
    checks if given string has all unique characters by storing counts in hash table
    complexity O(N)
    :param a_string: string to check
    :return: True if all chars are unique
    """
    char_dict = defaultdict(int)
    for char in a_string:
        char_dict[char] += 1
        if char_dict[char] > 1:
            return False
    return True


def has_unique_inplace(a_string: str) -> bool:
    """
    check if string has unique characters by sorting given string and checking subsequent chars
    complexity O(N log N)
    :param a_string: string to check
    :return: True if all chars are unique
    """
    a_string = sorted(a_string)
    for i in range(1, len(a_string)):
        if a_string[i] == a_string[i-1]:
            return False
    return True


