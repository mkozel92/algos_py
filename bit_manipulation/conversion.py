def convert(a: int, b: int) -> int:
    """
    compute number of bits that needs to be flipped to convert a to be
    :param a: first integer
    :param b: second integer
    :return: number of bit flips needed for conversion
    """
    diff = a ^ b
    count = 0
    while diff:
        count += 1
        diff &= diff - 1
    return count
