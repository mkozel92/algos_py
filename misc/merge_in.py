def merge_in(list_a: list, list_b: list):
    """
    merge list b into list a given there in enough space on the end of a
    :param list_a: first list
    :param list_b: second list
    """
    end_a = 0

    while list_a[end_a] is not None:
        end_a += 1
    end_a -= 1

    assert (end_a + len(list_b) < len(list_a))

    a_index = end_a
    b_index = len(list_b) - 1

    for k in range(len(list_a) - 1, -1, -1):
        if b_index < 0 or (a_index >= 0 and list_a[a_index] > list_b[b_index]):
            list_a[k] = list_a[a_index]
            a_index -= 1
        else:
            list_a[k] = list_b[b_index]
            b_index -= 1
