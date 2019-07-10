

def coins(values: list, sum_to: int) -> int:
    """
    count all possible ways how to combine coins of given values
    into desired sum amount
    complexity O(N)
    :param values: coins values
    :param sum_to: sum
    :return num of possible ways to combine coins
    """

    dp = [0] * (sum_to + 1)
    dp[0] = 1

    for coin in values:
        for i in range(len(dp)):
            if i - coin >= 0:
                dp[i] += dp[i - coin]

    return dp[-1]
