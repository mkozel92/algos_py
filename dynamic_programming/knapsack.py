

def get_value(dp: list, row: int, col: int) -> int:
    if row < 0 or col < 0:
        return 0
    return dp[row][col]


def knapsack(weights: list, values: list, capacity: int) -> int:
    """
    solve 0/1 knapsack in n^2 time
    :param weights: weights of objects
    :param values: values of objects
    :param capacity: capacity of the knapsack
    :return: best value of knapsack
    """
    num_items = len(weights)
    dp = [capacity * [0] for _ in range(num_items)]

    for item in range(num_items):
        for cap in range(capacity):
            if weights[item] <= cap:
                dp[item][cap] = max(get_value(dp, item - 1, cap), get_value(dp, item - 1,
                                                                            cap - weights[item]) + values[item])
            else:
                dp[item][cap] = get_value(dp, item - 1, cap)

    return dp[-1][-1]
