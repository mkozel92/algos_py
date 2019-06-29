from data_structures.linked_list_stack import LinkedListStack


def move(first_stack: LinkedListStack, second_stack: LinkedListStack, cmp: callable):
    """
    move elements from one stack to another while switching elements based on given comparison method
    :param first_stack: first stack
    :param second_stack: second stack
    :param cmp: comparison function
    :return: False if no elements were switched
    """
    tmp = first_stack.pop()
    switched = False
    while not first_stack.is_empty():
        if cmp(first_stack.peek(), tmp):
            second_stack.push(first_stack.pop())
            switched = True
        else:
            second_stack.push(tmp)
            tmp = first_stack.pop()

    second_stack.push(tmp)
    return switched


def sort_stack(a_stack: LinkedListStack):
    """
    sort elements in given stack using only one additional stack
    complexity o(N^2)
    :param a_stack: a stack to sort
    """
    tmp = LinkedListStack()

    while True:
        move(a_stack, tmp, lambda a, b: a < b)
        switched = move(tmp, a_stack, lambda a, b: a > b)
        if not switched:
            break
