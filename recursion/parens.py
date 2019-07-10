

def parens(n: int, num: int, result: list, current: list):
    """
    get all valid matching for n parantheses
    complexity O(2^N)
    :param n: num of parans
    :param num: current index
    :param result: resulting list
    :param current: current sequence
    """
    if n == -1 and num == 0:
        result.append(current.copy())

    if num < 0 or n < 0:
        return

    current[n] = ')'
    parens(n - 1, num + 1, result, current)

    current[n] = '('
    parens(n - 1, num - 1, result, current)
