

def float_to_bin(a_float: float) -> str:
    """
    convert decimal part of given float into bit representation
    :param a_float: a float to convert
    :return: string with bit representation
    """
    result = ['0'] * 32
    for i in range(32):
        a_float *= 2
        if a_float > 1:
            result[i] = '1'
            a_float -= 1
    return ''.join(result)
