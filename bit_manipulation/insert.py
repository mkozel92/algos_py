
def get_bit(a):
    res = ''
    for i in range(32):
        if 2**i & a:
            res = '1' + res
        else:
            res = '0' + res
    return res


def insert(a: int, b: int, from_: int, to_: int) -> int:
    """
    insert bits of b in place of given bits of a
    :param a: first integer
    :param b: second integer
    :param from_: from index
    :param to_: to index
    :return: adjusted int a
    """
    mask = -1 << to_
    mask |= 2 ** from_ - 1
    print(get_bit(mask))
    print(get_bit(a))

    a &= mask
    print(get_bit(a))

    b <<= from_
    a |= b
    print(get_bit(a))
    return a
