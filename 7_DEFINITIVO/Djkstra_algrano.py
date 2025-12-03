# ===========================================================
#                    TDA: GRAPH EDGE
# ===========================================================

class GraphEdge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight

    def __repr__(self):
        return f"{self.source.name} --{self.weight}--> {self.destination.name}"


# ===========================================================
#                    TDA: GRAPH NODE
# ===========================================================

class GraphNode:
    def __init__(self, name):
        self.name = name
        self.edges = []
        self.distance = float('inf')
        self.previous = None

    def add_edge(self, destination, weight):
        edge = GraphEdge(self, destination, weight)
        self.edges.append(edge)

    def reset(self):
        self.distance = float('inf')
        self.previous = None

    def __repr__(self):
        return f"GraphNode({self.name})"

    def __lt__(self, other):
        return self.name < other.name


# ===========================================================
#                      TDA: GRAPH
# ===========================================================

class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name):
        if name not in self.nodes:
            self.nodes[name] = GraphNode(name)
        return self.nodes[name]

    def add_edge(self, source_name, destination_name, weight):
        source = self.add_node(source_name)
        destination = self.add_node(destination_name)
        source.add_edge(destination, weight)

    def get_node(self, name):
        return self.nodes.get(name)

    def reset_distances(self):
        for node in self.nodes.values():
            node.reset()

    def __repr__(self):
        return f"Graph(nodes={len(self.nodes)})"


# ===========================================================
#                   TDA: AVL NODE
# ===========================================================

class AVLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.height = 1
        self.left = None
        self.right = None

    def __repr__(self):
        return f"AVLNode(key={self.key}, value={self.value.name})"


# ===========================================================
#              TDA: AVL TREE (PRIORITY QUEUE)
# ===========================================================

class AVLTree:
    def __init__(self):
        self.root = None

    def _get_height(self, node):
        return node.height if node else 0

    def _update_height(self, node):
        node.height = 1 + max(self._get_height(node.left), 
                              self._get_height(node.right))

    def _get_balance_factor(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        self._update_height(y)
        self._update_height(x)

        return x

    def _rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        self._update_height(x)
        self._update_height(y)

        return y

    def insert(self, key, value):
        self.root = self._insert(self.root, key, value)

    def _insert(self, node, key, value):
        if not node:
            return AVLNode(key, value)

        if key < node.key:
            node.left = self._insert(node.left, key, value)
        else:
            node.right = self._insert(node.right, key, value)

        self._update_height(node)

        balance = self._get_balance_factor(node)

        if balance > 1 and key < node.left.key:
            return self._rotate_right(node)

        if balance < -1 and key >= node.right.key:
            return self._rotate_left(node)

        if balance > 1 and key >= node.left.key:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1 and key < node.right.key:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def extract_min(self):
        if not self.root:
            return None
        
        self.root, min_node = self._extract_min(self.root)
        return min_node.key, min_node.value

    def _extract_min(self, node):
        if node.left is None:
            return node.right, node

        node.left, min_node = self._extract_min(node.left)

        self._update_height(node)

        balance = self._get_balance_factor(node)

        if balance < -1:
            right_balance = self._get_balance_factor(node.right)
            if right_balance <= 0:
                node = self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                node = self._rotate_left(node)

        elif balance > 1:
            left_balance = self._get_balance_factor(node.left)
            if left_balance >= 0:
                node = self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                node = self._rotate_right(node)

        return node, min_node

    def is_empty(self):
        return self.root is None

    def __repr__(self):
        return f"AVLTree(empty={self.is_empty()})"


# ===========================================================
#              TDA: DIJKSTRA ALGORITHM
# ===========================================================

class Dijkstra:
    def __init__(self, graph):
        self.graph = graph

    def run(self, start_name):
        self.graph.reset_distances()

        start_node = self.graph.get_node(start_name)
        if not start_node:
            raise ValueError(f"Nodo '{start_name}' no existe en el grafo")

        start_node.distance = 0
        priority_queue = AVLTree()
        priority_queue.insert(0, start_node)

        while not priority_queue.is_empty():
            current_distance, current_node = priority_queue.extract_min()

            if current_distance > current_node.distance:
                continue

            for edge in current_node.edges:
                neighbor = edge.destination
                new_distance = current_node.distance + edge.weight

                if new_distance < neighbor.distance:
                    neighbor.distance = new_distance
                    neighbor.previous = current_node
                    priority_queue.insert(new_distance, neighbor)

    def get_shortest_path(self, destination_name):
        destination = self.graph.get_node(destination_name)
        if not destination:
            return []

        if destination.distance == float('inf'):
            return []

        path = []
        current = destination
        while current is not None:
            path.append(current.name)
            current = current.previous

        path.reverse()
        return path

    def get_distance(self, destination_name):
        node = self.graph.get_node(destination_name)
        return node.distance if node else float('inf')

    def get_all_distances(self):
        return {name: node.distance for name, node in self.graph.nodes.items()}


# ===========================================================
#                    EJEMPLO DE USO
# ===========================================================

if __name__ == "__main__":
    g = Graph()

    g.add_edge("A", "B", 4)
    g.add_edge("A", "C", 2)
    g.add_edge("C", "B", 1)
    g.add_edge("B", "D", 5)
    g.add_edge("C", "D", 8)
    g.add_edge("C", "E", 10)
    g.add_edge("D", "E", 2)
    g.add_edge("D", "F", 6)
    g.add_edge("E", "F", 3)

    dijkstra = Dijkstra(g)

    dijkstra.run("A")

    print("=" * 50)
    print("DISTANCIAS MÍNIMAS DESDE A:")
    print("=" * 50)
    for node_name, distance in dijkstra.get_all_distances().items():
        print(f"{node_name}: {distance}")

    print("\n" + "=" * 50)
    print("CAMINOS MÁS CORTOS:")
    print("=" * 50)
    
    for destination in ["B", "C", "D", "E", "F"]:
        path = dijkstra.get_shortest_path(destination)
        distance = dijkstra.get_distance(destination)
        print(f"A → {destination}: {' → '.join(path)} (distancia: {distance})")