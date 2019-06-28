from data_structures.linked_list_stack import LinkedListStack
from linked_lists.linked_list import LinkedList


def is_palindrome(a_list: LinkedList) -> bool:
    """
    check if given list is a palindrome
    complexity O(N)
    :param a_list: list to check
    :return: True if linked list is a palindrome
    """
    a_stack = LinkedListStack()
    current = a_list.head
    runner = a_list.head

    while runner and runner.next:
        a_stack.push(current.data)
        current = current.next
        runner = runner.next.next

    if runner:
        current = current.next

    while current:
        if current.data != a_stack.pop():
            return False
        current = current.next
    return True
