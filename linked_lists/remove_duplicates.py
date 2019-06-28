from linked_lists.linked_list import LinkedList


def remove_duplicates(a_list: LinkedList):
    """
    removes duplicates from a linked list by keeping track of seen elements
    complexity O(N)
    :param a_list: a linked list to process
    """
    seen = set()
    current = a_list.head
    seen.add(current.data)

    while current.next:
        while current.next.data in seen:
            current.next = current.next.next
        seen.add(current.next.data)
        current = current.next


def remove_duplicates_no_buffer(a_list: LinkedList):
    """
    remove duplicates without using extra space
    complexity O(N^2)
    :param a_list: linked list to process
    """
    current = a_list.head
    while current:
        runner = current
        while runner.next:
            while current.data == runner.next.data:
                runner.next = runner.next.next
            runner = runner.next
        current = current.next



