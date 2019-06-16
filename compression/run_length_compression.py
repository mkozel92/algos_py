from bitstream import BitStream
from numpy import int8


def count_bits(bit_stream: BitStream, which_bit: bool, max_count: int) -> int:
    """
    count consecutive number of same bits
    :param bit_stream: a stream of bits
    :param which_bit: which bits to count
    :param max_count: max allowed number of same consecutive
    :return: count of same consecutive bits in given stream
    """
    count = 0
    which_bit = '1' if which_bit else '0'
    bit = str(bit_stream)[0]
    while bit == which_bit and count < max_count and len(bit_stream):
        bit_stream.read(bool, 1)
        count += 1
        if len(bit_stream):
            bit = str(bit_stream)[0]
    return count


def compress(bit_stream: BitStream) -> BitStream:
    """
    compress a bit stream using run length encoding
    -> replace replace series of same consecutive bit by they number
    00001110000111 -> 4343 -> 100011100011
    f the bits are not in long consecutive series of same bits the
    compressed file can end up being bigger then original
    :param bit_stream: bit stream to compress
    :return: compressed stream
    """
    compressed = BitStream()
    bit = True
    while len(bit_stream):
        count = count_bits(bit_stream, bit, 256)
        compressed.write(count, int8)
        bit = not bit
    return compressed


def expand(bit_stream: BitStream) -> BitStream:
    """
    expand compressed bit stresm
    :param bit_stream: bitstream to expand
    :return: original stream before compression
    """
    expanded = BitStream()
    bit = True
    while len(bit_stream):
        count = bit_stream.read(int8, 1)[0]
        for _ in range(count):
            expanded.write(bit, bool)
        bit = not bit
    return expanded
