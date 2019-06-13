

def brute_force_search(string_to_search: str, pattern: str) -> int:
    """
    return position where the match is found
    complexity O(MN)
    :param string_to_search: string to search in
    :param pattern: pattern to search for
    :return: position of the pattern in the string to search in
    """
    for i in range(len(string_to_search) - len(pattern) + 1):
        match_length = 0
        for j in range(len(pattern)):
            if string_to_search[i + j] != pattern[j]:
                break
            match_length += 1
        if match_length == len(pattern):
            return i
    return -1
