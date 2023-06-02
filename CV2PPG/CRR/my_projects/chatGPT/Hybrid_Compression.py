import huffman
import lzw
import ppm
import arithmetic_coding


def compress(data):
    # Step 1: Use PPM to predict the probability of each symbol in the data
    model = ppm.build_model(data)

    # Step 2: Use Huffman coding to compress the data based on the predicted symbol probabilities
    huffman_encoded = huffman.encode(data, model)

    # Step 3: Use LZW compression to further compress the Huffman encoded data
    lzw_encoded = lzw.compress(huffman_encoded)

    # Step 4: Use arithmetic coding to compress the LZW encoded data
    arithmetic_encoded = arithmetic_coding.compress(lzw_encoded)

    return arithmetic_encoded


def decompress(compressed_data):
    # Step 1: Use arithmetic coding to decompress the data
    lzw_encoded = arithmetic_coding.decompress(compressed_data)

    # Step 2: Use LZW decompression to decompress the data
    huffman_encoded = lzw.decompress(lzw_encoded)

    # Step 3: Use Huffman decompression to decompress the data
    data = huffman.decode(huffman_encoded, model)

    return data