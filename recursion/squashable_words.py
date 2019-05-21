

def remove_from_string(a_string: str, position: int) -> str:
    """
    removes a letter that is on a given position in given string

    :param a_string: a string from which we want to remove a letter
    :param position: position of the letter to remove
    :return: news string
    """
    return a_string[:position] + a_string[position + 1:]


def is_squashable(a_word: str, a_dictionary: set, mem_dict: dict) -> bool:
    """
    Function to determine whether a given word is squashable.
    A word is squashable if it can be reduced to empty string by removing letters from the original string
    in such a way that every newly created word in the process is in a dictionary of valid words

    example: a_dictionary = {'hello', 'hell', 'hel', 'hl', 'l'}
    'hello' can be reduced to empty string through series of valid words and is therefore squashable

    complexity: O(N!)

    :param a_word: the word to examine
    :param a_dictionary: dictionary of valid words
    :param mem_dict: memoized solutions
    :return: whether or not a_word is squashable
    """
    if a_word in mem_dict:
        return mem_dict[a_word]

    if a_word not in a_dictionary:
        return False

    for i in range(len(a_word)):
        new_word = remove_from_string(a_word, i)
        if not new_word or is_squashable(new_word, a_dictionary, mem_dict):
            mem_dict[a_word] = True
            return True

    mem_dict[a_word] = False
    return False
