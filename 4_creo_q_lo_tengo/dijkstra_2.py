# -------------------------------------------------------
# TDA: Nodo del AVL
# -------------------------------------------------------
class AVLNode:
    def __init__(self, key, value):
        self.key = key          # clave para ordenar (distancia mínima)
        self.value = value      # valor almacenado (nodo del grafo)
        self.left = None
        self.right = None
        self.height = 1


# -------------------------------------------------------
# TDA: Árbol AVL (usado como cola de prioridad)
# -------------------------------------------------------
class AVLTree:

    # ----------------------------
    # Altura
    # ----------------------------
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    # ----------------------------
    # Factor de balanceo
    # ----------------------------
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # ----------------------------
    # Rotaciones
    # ----------------------------
    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))

        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    # ----------------------------
    # Inserción estándar AVL
    # ----------------------------
    def insert(self, node, key, value):
        if not node:
            return AVLNode(key, value)

        if key < node.key:
            node.left = self.insert(node.left, key, value)
        else:
            node.right = self.insert(node.right, key, value)

        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

        balance = self.get_balance(node)

        # Rotación izquierda-izquierda
        if balance > 1 and key < node.left.key:
            return self.rotate_right(node)

        # Rotación derecha-derecha
        if balance < -1 and key > node.right.key:
            return self.rotate_left(node)

        # Rotación izquierda-derecha
        if balance > 1 and key > node.left.key:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)

        # Rotación derecha-izquierda
        if balance < -1 and key < node.right.key:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)

        return node

    # ----------------------------
    # Obtener menor nodo (cola de prioridad)
    # ----------------------------
    def get_min_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    # ----------------------------
    # Eliminación AVL
    # ----------------------------
    def delete(self, root, key):
        if not root:
            return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            temp = self.get_min_node(root.right)
            root.key = temp.key
            root.value = temp.value
            root.right = self.delete(root.right, temp.key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.rotate_right(root)

        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.rotate_left(root)

        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root


# -------------------------------------------------------
# TDA: Grafo (para Dijkstra)
# -------------------------------------------------------
class GraphNode:
    def __init__(self, name):
        self.name = name
        self.edges = []  # lista de (vecino, peso)

    def add_edge(self, neighbor, weight):
        self.edges.append((neighbor, weight))


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, name):
        self.nodes[name] = GraphNode(name)

    def add_edge(self, src, dst, weight):
        self.nodes[src].add_edge(self.nodes[dst], weight)


# -------------------------------------------------------
# TDA: Dijkstra usando AVL
# -------------------------------------------------------
class DijkstraAVL:
    def __init__(self, graph):
        self.graph = graph
        self.dist = {name: float('inf') for name in graph.nodes}
        self.parent = {name: None for name in graph.nodes}

        self.heap_root = None     # raíz del AVL
        self.heap = AVLTree()     # cola de prioridad

    # insertar distancia en el AVL
    def push(self, dist, node_name):
        self.heap_root = self.heap.insert(self.heap_root, dist, node_name)

    # extraer mínimo del AVL
    def pop(self):
        min_node = self.heap.get_min_node(self.heap_root)
        self.heap_root = self.heap.delete(self.heap_root, min_node.key)
        return min_node.key, min_node.value

    # -------------------------------------------
    # Algoritmo de Dijkstra
    # -------------------------------------------
    def run(self, start):
        self.dist[start] = 0
        self.push(0, start)

        while self.heap_root is not None:
            current_dist, current_name = self.pop()
            current = self.graph.nodes[current_name]

            if current_dist > self.dist[current_name]:
                continue

            for neighbor, weight in current.edges:
                new_dist = current_dist + weight
                if new_dist < self.dist[neighbor.name]:
                    self.dist[neighbor.name] = new_dist
                    self.parent[neighbor.name] = current_name
                    self.push(new_dist, neighbor.name)

        return self.dist, self.parent

    # reconstrucción del camino
    def get_path(self, target):
        path = []
        while target is not None:
            path.append(target)
            target = self.parent[target]
        return list(reversed(path))


# -------------------------------------------------------
# EJEMPLO DE USO
# -------------------------------------------------------
if __name__ == "__main__":
    g = Graph()

    for name in ["A", "B", "C", "D", "E"]:
        g.add_node(name)

    g.add_edge("A", "B", 4)
    g.add_edge("A", "C", 2)
    g.add_edge("C", "B", 1)
    g.add_edge("B", "D", 5)
    g.add_edge("C", "D", 8)
    g.add_edge("D", "E", 6)

    d = DijkstraAVL(g)
    dist, parent = d.run("A")

    print("Distancias mínimas:")
    for node in dist:
        print(node, dist[node])

    print("\nCamino de A a E:")
    print(d.get_path("E"))
