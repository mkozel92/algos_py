def triple_step(num_steps: int) -> int:
    """
    count how many ways you can go up a stairs making 1, 2 or 3 steps
    complexity O(N)
    :param num_steps: how many steps to climb
    :return: num of possible ways to climb the steps
    """
    if num_steps == 0:
        return 1

    dp_list = [0] * (num_steps + 3)
    dp_list[0] = 1
    dp_list[1] = 2
    dp_list[2] = 4

    for i in range(3, len(dp_list)):
        dp_list[i] = dp_list[i - 1] + dp_list[i - 2] + dp_list[i - 3]

    return dp_list[-4]


def triple_step_recursion(num_steps: int, mem_dict: dict) -> int:
    """
    count how many ways you can go up a stairs making 1, 2 or 3 steps
    complexity O(N)
    :param num_steps: how many steps to climb
    :return: num of possible ways to climb the steps
    """
    if num_steps == 0:
        return 1

    if num_steps < 0:
        return 0

    if num_steps in mem_dict:
        return mem_dict[num_steps]

    result = triple_step_recursion(num_steps - 1, mem_dict) \
             + triple_step_recursion(num_steps - 2, mem_dict) \
             + triple_step_recursion(num_steps - 3, mem_dict)
    mem_dict[num_steps] = result
    return result
