

def replace_whitespaces(a_text: list):
    """
    replace spaces by url symbol of a space %20
    :param a_text: test to adjust
    """
    i = len(a_text) - 1
    j = len(a_text) - 1

    while a_text[j] == ' ':
        j -= 1

    while j >= 0:
        if a_text[j] != ' ':
            a_text[i] = a_text[j]
            i -= 1
            j -= 1
        else:
            j -= 1
            for char in '02%':
                a_text[i] = char
                i -= 1
