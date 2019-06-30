from copy import deepcopy


def bst_sequences(possible_next: list) -> list:
    """
    return list of sequences that could be possibly used to build given binary tree
    :param possible_next: list of all nodes that could be possibly added next to the tree
    this is initially just the root
    :return: list of all possible sequences to build given tree
    """
    sequences = []
    for i in range(len(possible_next)):
        node = possible_next[i]
        new_set = deepcopy(possible_next)
        new_set.pop(i)
        if node.left:
            new_set.append(node.left)
        if node.right:
            new_set.append(node.right)
        for sequence in bst_sequences(new_set):
            sequences.append([node.key] + sequence)
    if not sequences:
        return [[]]
    return sequences

