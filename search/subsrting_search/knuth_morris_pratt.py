

def build_dfa(pattern: str):
    """
    Build deterministic finite automata for KMP algo
    complexity O(MR) radix * length of pattern
    :param pattern: pattern to search for
    :return: dfa
    """
    radix = 256
    dfa = [[0] * (len(pattern) + 1) for _ in range(radix)]
    dfa[ord(pattern[0])][0] = 1
    x = 0
    j = 1
    while j < len(pattern):
        for c in range(radix):
            dfa[c][j] = dfa[c][x]
        dfa[ord(pattern[j])][j] = j + 1
        x = dfa[ord(pattern[j])][x]
        j += 1
    return dfa


def knuth_morris_pratt(string_to_search: str, pattern: str) -> int:
    """
    KMP algo for substring search
    builds DFA in MR time and searches for substring in N time
    complexity of search O(N)
    :param string_to_search: string to search in
    :param pattern: pattern to search
    :return: position of pattern or -1
    """
    dfa = build_dfa(pattern)
    j = 0
    for i, c in enumerate(string_to_search):
        j = dfa[ord(c)][j]
        if j == len(pattern):
            return i - len(pattern) + 1
    return -1
