import unittest

from compression.huffman import build_trie, build_encoding_table, encode, decode


class TestHuffman(unittest.TestCase):

    def test_huffman(self):
        root = build_trie('this is some sample text')
        encoding_table = build_encoding_table(root)

        original_text = "same text"
        encoded_text = encode(original_text, encoding_table)
        decoded_text = decode(encoded_text, root)
        self.assertEqual(original_text, decoded_text)
