

def longest_sequence(a: int) -> int:
    """
    longest sequence of 1 bits that can be created by flipping one bit
    :param a: int to process
    :return: lenght of the sequence
    """
    previous_count = 0
    current_count = 0
    longest = 0

    for i in range(32):
        if 2**i & a:
            current_count += 1
        else:
            if 2**(i+1) & a:
                previous_count = current_count
            else:
                previous_count = 0
            current_count = 0

        longest = max(longest, current_count + previous_count + 1)
    return longest
