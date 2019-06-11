

def key_index_sorting(a_list: list, position: int, radix: int):
    """
    sort by counting occurrences of every key
    :param a_list: list to sort
    :param position: position of key in the string
    :param radix: number of available key
    """
    counts = [0] * (radix + 1)
    aux = [None] * len(a_list)

    for x in a_list:
        counts[ord(x[position])] += 1

    for i in range(1, len(counts)):
        counts[i] += counts[i - 1]

    for x in a_list:
        aux[counts[ord(x[position]) - 1]] = x
        counts[ord(x[position]) - 1] += 1

    print(aux)
    for i in range(len(a_list)):
        a_list[i] = aux[i]


def lsd_radix_sort(a_list: list, radix: int):
    """
    radix sort for string sorting
    Complexity O(WN) ..w is length of every string
    :param a_list: a list to sort
    :param radix: max key value
    """
    w = len(a_list[0])

    for position in range(w-1, -1, -1):
        key_index_sorting(a_list, position, radix)
