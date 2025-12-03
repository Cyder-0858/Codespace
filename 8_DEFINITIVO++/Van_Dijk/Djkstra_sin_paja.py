# ===========================================================
#                    TDA: GRAPH EDGE
# ===========================================================

class GraphEdge:
    def __init__(self, source, destination, weight):
        self.source = source
        self.destination = destination
        self.weight = weight


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
        self.edges.append(GraphEdge(self, destination, weight))

    def reset(self):
        self.distance = float('inf')
        self.previous = None


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


# ===========================================================
#              TDA: AVL TREE (PRIORITY QUEUE)
# ===========================================================

class AVLTree:
    def __init__(self):
        self.root = None

    def _height(self, node):
        return node.height if node else 0

    def _update_height(self, node):
        node.height = 1 + max(self._height(node.left), self._height(node.right))

    def _balance(self, node):
        return self._height(node.left) - self._height(node.right) if node else 0

    def _rotate_right(self, y):
        x = y.left
        y.left = x.right
        x.right = y
        self._update_height(y)
        self._update_height(x)
        return x

    def _rotate_left(self, x):
        y = x.right
        x.right = y.left
        y.left = x
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
        balance = self._balance(node)

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
        if not node.left:
            return node.right, node
        node.left, min_node = self._extract_min(node.left)
        self._update_height(node)
        balance = self._balance(node)

        if balance < -1:
            if self._balance(node.right) <= 0:
                node = self._rotate_left(node)
            else:
                node.right = self._rotate_right(node.right)
                node = self._rotate_left(node)
        elif balance > 1:
            if self._balance(node.left) >= 0:
                node = self._rotate_right(node)
            else:
                node.left = self._rotate_left(node.left)
                node = self._rotate_right(node)

        return node, min_node

    def is_empty(self):
        return self.root is None


# ===========================================================
#              TDA: DIJKSTRA ALGORITHM
# ===========================================================

class Dijkstra:
    def __init__(self, graph):
        self.graph = graph

    def run(self, start_name):
        self.graph.reset_distances()
        start = self.graph.get_node(start_name)
        if not start:
            raise ValueError(f"Nodo '{start_name}' no existe")

        start.distance = 0
        pq = AVLTree()
        pq.insert(0, start)

        while not pq.is_empty():
            dist, node = pq.extract_min()
            
            if dist > node.distance:
                continue

            for edge in node.edges:
                neighbor = edge.destination
                new_dist = node.distance + edge.weight

                if new_dist < neighbor.distance:
                    neighbor.distance = new_dist
                    neighbor.previous = node
                    pq.insert(new_dist, neighbor)

    def get_path(self, destination_name):
        dest = self.graph.get_node(destination_name)
        if not dest or dest.distance == float('inf'):
            return []

        path = []
        current = dest
        while current:
            path.append(current.name)
            current = current.previous
        return path[::-1]

    def get_distance(self, destination_name):
        node = self.graph.get_node(destination_name)
        return node.distance if node else float('inf')


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

    print("DISTANCIAS MÍNIMAS DESDE A:")
    for name in g.nodes:
        print(f"{name}: {g.get_node(name).distance}")

    print("\nCAMINOS MÁS CORTOS:")
    for dest in ["B", "C", "D", "E", "F"]:
        path = dijkstra.get_path(dest)
        dist = dijkstra.get_distance(dest)
        print(f"A → {dest}: {' → '.join(path)} (distancia: {dist})")