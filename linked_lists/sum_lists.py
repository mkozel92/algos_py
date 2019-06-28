from linked_lists.linked_list import LinkedList


def sum_list_lsd(first_list: LinkedList, second_list: LinkedList) -> int:
    """
    sum two numbers represented by linked lists holding lsd ordered digits
    complexity O(N)
    :param first_list: first list
    :param second_list: second list
    :return: int representing the sum
    """
    result = 0
    carry = 0
    order = 1

    current_0 = first_list.head
    current_1 = second_list.head

    while current_0 and current_1:
        result += ((current_0.data + current_1.data + carry) % 10) * order
        carry = (current_0.data + current_1.data + carry) // 10
        order *= 10
        current_1 = current_1.next
        current_0 = current_0.next

    for current in [current_1, current_0]:
        while current:
            result += ((current.data + carry) % 10) * order

            carry = current.data + carry // 10
            order *= 10
            current = current.next

    return result
