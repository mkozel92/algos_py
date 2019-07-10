from bitstream import BitStream
from collections import defaultdict

from data_structures.binary_heap import BinaryHeap


class TrieNode(object):
    """Node for a trie for huffman encoding"""

    def __init__(self):
        self.left = None
        self.right = None
        self.char = None
        self.is_leaf = False


def build_trie(a_text: str) -> TrieNode:
    """
    Build a trie representing huffman encoding
    :param a_text: text to use to get character frequencies
    :return: root of given trie
    """
    frequencies = defaultdict(int)
    for char in a_text:
        frequencies[char] += 1

    a_heap = BinaryHeap(compare=lambda x, y: x[0] < y[0])

    for key in frequencies:
        a_node = TrieNode()
        a_node.is_leaf = True
        a_node.char = key
        a_heap.insert((frequencies[key], a_node))

    while a_heap.size() > 1:
        first_count, first_node = a_heap.remove()
        second_count, second_node = a_heap.remove()

        new_node = TrieNode()
        new_node.left = second_node
        new_node.right = first_node

        a_heap.insert((first_count + second_count, new_node))

    root = a_heap.remove()[1]
    return root


def build_encoding_table_rec(a_node: TrieNode, current: list, encoding_table: dict):
    """
    recursive function to get character encodings from given try
    :param a_node: current node
    :param current: current path to node
    :param encoding_table: dict to save results
    """
    # print(current)
    if a_node.is_leaf:
        encoding_table[a_node.char] = current.copy()
    else:
        current.append(True)
        build_encoding_table_rec(a_node.left, current, encoding_table)
        current.append(False)
        build_encoding_table_rec(a_node.right, current, encoding_table)
    if current:
        current.pop(len(current) - 1)


def build_encoding_table(a_node: TrieNode) -> dict:
    """
    build encoding dict using a trie
    :param a_node: root of trie
    :return: dict of encodings for characters
    """
    encoding_table = {}
    current = []
    build_encoding_table_rec(a_node, current, encoding_table)
    return encoding_table


def encode(a_text: str, encoding_table: dict) -> BitStream:
    """
    encode given text
    :param a_text: text to encode
    :param encoding_table: encoding table build using huffman coding
    :return: encoded bitstream
    """
    encoded = BitStream()
    for char in a_text:
        for bit in encoding_table[char]:
            encoded.write(bit, bool)
    return encoded


def decode(bit_stream: BitStream, a_node: TrieNode):
    """
    decode bitstream to a string
    :param bit_stream: bit stream to decode
    :param a_node: root of a trie representing computed huffman encoding
    :return: decoded string
    """
    result = ""
    current = a_node
    while len(bit_stream):
        bit = bit_stream.read(bool, 1)
        if bit[0]:
            current = current.left
        else:
            current = current.right
        if current.is_leaf:
            result += current.char
            current = a_node
    return result
