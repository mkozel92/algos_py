from collections import defaultdict


def group_anagrams(a_list: list):
    """
    group together anagrams in given list
    complexity O(Nk log k)
    :param a_list: list to process
    """
    anagram_groups = defaultdict(set)
    for s in a_list:
        anagram_groups[''.join(sorted(s))].add(s)

    i = 0
    for key in anagram_groups:
        for word in anagram_groups[key]:
            a_list[i] = word
            i += 1
