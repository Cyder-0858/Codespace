class HuffmanEncoder:
    def __init__(self):
        self.frequency_table = {}
        self.huffman_tree = None
        self.codes = {}

    def build_frequency_table(self, text):
        for char in text:
            if char in self.frequency_table:
                self.frequency_table[char] += 1
            else:
                self.frequency_table[char] = 1

    def build_tree(self):
        from heapq import heappop, heappush
        from collections import defaultdict

        heap = [[weight, [char, ""]] for char, weight in self.frequency_table.items()]
        heappush(heap, [1, ["", ""]])  # Add a dummy node for empty string

        while len(heap) > 1:
            lo = heappop(heap)
            hi = heappop(heap)
            for pair in lo[1:]:
                pair[1] = '0' + pair[1]
            for pair in hi[1:]:
                pair[1] = '1' + pair[1]
            heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])

        self.huffman_tree = sorted(heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

    def encode(self, text):
        self.build_frequency_table(text)
        self.build_tree()
        self.codes = {char: code for char, code in self.huffman_tree}
        return ''.join(self.codes[char] for char in text)