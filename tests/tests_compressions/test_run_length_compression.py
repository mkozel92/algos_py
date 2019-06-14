import unittest

from bitstream import BitStream

from compression.run_length_compression import compress, expand


class TestRunLengthCompression(unittest.TestCase):

    def test_compression(self):
        original_string = "this is some string to compress"
        byte_string = original_string.encode('ascii')

        original_stream = BitStream()
        original_stream.write(byte_string, bytes)
        original_stream_length = len(original_stream)

        compressed_stream = compress(original_stream)
        compressed_stream_length = len(compressed_stream)

        expanded_stream = expand(compressed_stream)
        retrieved_string = expanded_stream.read(bytes)
        retrieved_string = retrieved_string.decode('ascii')

        self.assertNotEqual(original_stream_length, compressed_stream_length)
        self.assertEqual(original_string, retrieved_string)