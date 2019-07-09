

def multiply(a: int, b: int):
    """
    recursive multiplication without using *
    :param a: first int
    :param b: second int
    :return: result
    """
    if a == 0:
        return 0

    result = 0
    if 1 & a:
        result += b
    a >>= 1

    tmp = multiply(a, b)
    result += tmp + tmp
    return result
