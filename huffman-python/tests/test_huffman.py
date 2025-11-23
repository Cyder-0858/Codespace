import pytest
from huffman.encoder import HuffmanEncoder
from huffman.decoder import HuffmanDecoder

def test_huffman_encoding_decoding():
    text = "hello huffman"
    encoder = HuffmanEncoder()
    decoder = HuffmanDecoder()

    # Build frequency table and tree
    frequency_table = encoder.build_frequency_table(text)
    huffman_tree = encoder.build_tree(frequency_table)

    # Encode the text
    encoded_text = encoder.encode(text, huffman_tree)

    # Decode the text
    decoded_text = decoder.decode(encoded_text, huffman_tree)

    # Assert that the decoded text matches the original text
    assert decoded_text == text

def test_empty_string():
    text = ""
    encoder = HuffmanEncoder()
    decoder = HuffmanDecoder()

    # Build frequency table and tree
    frequency_table = encoder.build_frequency_table(text)
    huffman_tree = encoder.build_tree(frequency_table)

    # Encode the text
    encoded_text = encoder.encode(text, huffman_tree)

    # Decode the text
    decoded_text = decoder.decode(encoded_text, huffman_tree)

    # Assert that the decoded text matches the original text
    assert decoded_text == text

def test_single_character():
    text = "aaaaaa"
    encoder = HuffmanEncoder()
    decoder = HuffmanDecoder()

    # Build frequency table and tree
    frequency_table = encoder.build_frequency_table(text)
    huffman_tree = encoder.build_tree(frequency_table)

    # Encode the text
    encoded_text = encoder.encode(text, huffman_tree)

    # Decode the text
    decoded_text = decoder.decode(encoded_text, huffman_tree)

    # Assert that the decoded text matches the original text
    assert decoded_text == text