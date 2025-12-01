class Graph:
    def __init__(self, items, capacity):
        self.items = items
        self.capacity = capacity
        self.start = Node(0, 0, 0)
        self.nodes = [self.start]

    def build(self):
        queue = [self.start]

        while queue:
            current = queue.pop(0)

            # si ya consideramos todos los objetos, no expandimos más
            if current.index == len(self.items):
                continue

            item = self.items[current.index]

            # ----------------------------------------------------
            # Opción 1: NO TOMAR (skip)
            # ----------------------------------------------------
            skip_node = Node(
                current.index + 1,
                current.weight,
                current.priority
            )

            skip_node.parent = current
            skip_node.action = "skip"

            self.nodes.append(skip_node)
            current.add_edge(Edge(skip_node, "skip"))
            queue.append(skip_node)

            # ----------------------------------------------------
            # Opción 2: TOMAR (take) si el peso lo permite
            # ----------------------------------------------------
            if current.weight + item.weight <= self.capacity:

                take_node = Node(
                    current.index + 1,
                    current.weight + item.weight,
                    current.priority + item.priority
                )

                take_node.parent = current
                take_node.action = "take"

                self.nodes.append(take_node)
                current.add_edge(Edge(take_node, "take"))
                queue.append(take_node)
