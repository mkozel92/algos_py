def longest_common_subsequence(first_string: str, second_string: str) -> int:
    """
    get length of longest common subsequence of two strings
    :param first_string: a string
    :param second_string: a string
    :return: len of longest common soubsequence
    """
    dp = [[0] * (len(second_string) + 1) for _ in range(len(first_string) + 1)]

    for row in range(1, len(first_string) + 1):
        for col in range(1, len(second_string) + 1):
            if first_string[row - 1] == second_string[col - 1]:
                dp[row][col] = 1 + dp[row - 1][col - 1]
            else:
                dp[row][col] = max(dp[row - 1][col], dp[row][col - 1])

    return dp[-1][-1]


def longest_common_subsequence_rec(first_string: str, second_string: str, i: int, j: int, mem: dict):
    """
        get length of longest common subsequence of two strings
        :param first_string: a string
        :param second_string: a string
        :param i: current index in first string
        :param j: current index in second string
        :param mem: memoized results
        :return: len of longest common soubsequence
        """

    if i < 0 or j < 0:
        return 0

    if (i, j) in mem:
        return mem[(i, j)]
    match = 0
    if first_string[i] == second_string[j]:
        match = 1 + longest_common_subsequence_rec(first_string, second_string, i - 1, j - 1, mem)

    first_skip = longest_common_subsequence_rec(first_string, second_string, i - 1, j, mem)
    second_skip = longest_common_subsequence_rec(first_string, second_string, i, j - 1, mem)

    mem[(i, j)] = max(match, first_skip, second_skip)

    return mem[(i, j)]
