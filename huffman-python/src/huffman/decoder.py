class HuffmanDecoder:
    def __init__(self, root):
        self.root = root

    def decode(self, encoded_str):
        decoded_str = ""
        current_node = self.root

        for bit in encoded_str:
            if bit == '0':
                current_node = current_node.left
            else:
                current_node = current_node.right

            if current_node.left is None and current_node.right is None:  # Leaf node
                decoded_str += current_node.char
                current_node = self.root

        return decoded_str