# Contenido del archivo /huffman-python/huffman-python/src/main.py

import sys
from huffman.encoder import HuffmanEncoder
from huffman.decoder import HuffmanDecoder

def main():
    # Leer la cadena de texto del usuario
    text = input("Introduce una cadena de texto para codificar: ")

    # Crear una instancia del codificador de Huffman
    encoder = HuffmanEncoder()
    encoded_text, tree = encoder.encode(text)
    print(f"Texto codificado: {encoded_text}")

    # Crear una instancia del decodificador de Huffman
    decoder = HuffmanDecoder(tree)
    decoded_text = decoder.decode(encoded_text)
    print(f"Texto decodificado: {decoded_text}")

if __name__ == "__main__":
    main()